import tkinter as tk
from PIL import ImageTk,Image,ImageOps
import time
import customtkinter as ctk

import mismagius
import user

class console:    
    def __init__(self):

        maincolor = "purple2"
        subcolor = "#30004B"
        darkcolor = "#1E032C"
        pastelcolor = "mediumpurple1"
        pastel_darkcolor = "#4A2B5C"
        hovorcolor = "purple3"

        self.size = "850x900"
        self.base = ctk.CTk(fg_color=darkcolor)
        self.base.geometry(self.size)
        self.base.title("ProjectMismagius for AI Solutions - v0.1 Console ")
        self.base.resizable(width=False,height=False)
        ctk.set_default_color_theme("dark-blue")

        self.frame1 = ctk.CTkFrame(
            master=self.base,
            fg_color=subcolor
        )
        self.exitbutton = ctk.CTkButton(master=self.frame1,width=120,height=40,text="おわる",command=lambda:self.base.destroy(),fg_color="red",hover_color="maroon")
        self.exitbutton.pack(padx=10,pady=20)
        self.movebutton = ctk.CTkButton(master=self.frame1,width=120,height=40,text="うえ",command=lambda:self.moveup(),fg_color=maincolor,hover_color=hovorcolor)
        self.movebutton.pack(padx=10,pady=20)
        self.movedbutton = ctk.CTkButton(master=self.frame1,width=120,height=40,text="した",command=lambda:self.movedown(),fg_color=maincolor,hover_color=hovorcolor)
        self.movedbutton.pack(padx=10,pady=20)
        self.reversebutton = ctk.CTkButton(master=self.frame1,width=120,height=40,text="ふりかえる",command=lambda:self.reverse(),fg_color=maincolor,hover_color=hovorcolor)
        self.reversebutton.pack(padx=10,pady=20)
        self.pushbutton = ctk.CTkButton(master=self.frame1,width=120,height=40,text="おくる",command=lambda:self.push(),fg_color=maincolor,hover_color=hovorcolor)
        self.pushbutton.pack(padx=10,pady=20,side=tk.BOTTOM)
        
        self.frame1.pack(side=tk.LEFT,padx=10,pady=10,fill=tk.Y)

        self.frame2 = ctk.CTkFrame(
            master=self.base,
            fg_color=subcolor
        )
        self.frame2.pack(side=tk.RIGHT,padx=10,pady=10,fill=tk.BOTH)
        
        self.canvas = ctk.CTkCanvas(self.frame2,bg=darkcolor,width=750,height=500)
        
        self.Mismagiusimage = Image.open("./img/mismagius.png")
        self.Sprigatitoimg = ImageTk.PhotoImage(self.Mismagiusimage)
        self.mismagius = mismagius.Mismagius()
        
        self.mismagius.setModelPosX(425) #初期値：425（中央）
        self.mismagius.setModelPosY(250) #初期値：250（中央）
        self.User = user.user()
        self.imgid = self.canvas.create_image(
            self.mismagius.getModelPosX(),
            self.mismagius.getModelPosY(),
            image=self.Sprigatitoimg
        )
        self.outlabel = ctk.CTkLabel(self.frame2,text="出力",text_color=pastelcolor)
        self.outputbox = ctk.CTkTextbox(self.frame2,width=600,height=200,fg_color=pastel_darkcolor,corner_radius=15)
        self.outputbox.configure(state="disabled")
        self.inlabel = ctk.CTkLabel(self.frame2,text="入力",text_color=pastelcolor)
        self.inputbox = ctk.CTkTextbox(self.frame2,width=600,height=50,fg_color=pastel_darkcolor,corner_radius=15)
        self.canvas.pack(padx=10,pady=10)
        self.outlabel.pack(padx=5,pady=3)
        self.outputbox.pack(padx=5,pady=3)
        self.inlabel.pack(padx=5,pady=3)
        self.inputbox.pack(padx=5,pady=3)

    def moveup(self):
        for i in range(10):
            self.canvas.move(self.imgid,0,-5)
            self.canvas.update()
            time.sleep(0.03)
        self.mismagius.setModelPosY(self.mismagius.getModelPosY()-50)
    def movedown(self):
        for i in range(10):
            self.canvas.move(self.imgid,0,5)
            self.canvas.update()
            time.sleep(0.03)
        self.mismagius.setModelPosY(self.mismagius.getModelPosY()+50)
    def reverse(self):
            self.canvas.delete(self.imgid)
            self.Mismagiusimage = ImageOps.mirror(self.Mismagiusimage)
            self.Mismagiusimg = ImageTk.PhotoImage(self.Mismagiusimage)
            self.imgid = self.canvas.create_image(
                self.mismagius.getModelPosX(),
                self.mismagius.getModelPosY(),
                image=self.Mismagiusimg
            )    

    def push(self):
        text = self.inputbox.get("1.0","end")
        if not text.isspace():
            text = text.replace("\n","")
            self.inputbox.delete("1.0","end")
            self.insertoutput(self.User.getUserName()+":"+text)
            self.mismagius.send(text)
            self.insertoutput(self.mismagius.getModelName()+":"+self.mismagius.getSendMessage())

    def insertoutput(self,text):
            self.outputbox.configure(state="normal")
            self.outputbox.insert("end",text+"\n")
            self.outputbox.configure(state="disabled")