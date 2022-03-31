from cProfile import label
from tkinter import * # Used to create the GUI
from tkinter import ttk # This module contains widgets
import os, sys
from turtle import width
from PIL import Image,ImageTk
from matplotlib import image# This module is used to deal with images
from tkmacosx import Button

# 
class Face_recognition_system: 
    def __init__(self,root):
        self.root = root
        self.root.geometry("1430x800+0+0")
        self.root.title("Face Recogniton System")
        
        # IMAGES 
        img= Image.open("images/cam1.jpg")
        img= img.resize((500,130),Image.ANTIALIAS)
        self.photoimg1= ImageTk.PhotoImage(img)
        
        first_lbl= Label(self.root,image= self.photoimg1)
        first_lbl.place(x=0,y=0,width=500,height=130)
        
        img2= Image.open("images/cam2.jpg")
        img2= img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2= ImageTk.PhotoImage(img2)
        
        second_lbl= Label(self.root,image= self.photoimg2)
        second_lbl.place(x=500,y=0,width=500,height=130)
        #-----------------------------------------------------------------
        #Background image
        img4= Image.open("images/geometry.jpg")
        img4= img4.resize((1530,710),Image.ANTIALIAS)
        self.bgimg= ImageTk.PhotoImage(img4)
        
        bgimg_lbl= Label(self.root,image= self.bgimg)
        bgimg_lbl.place(x=0,y=150,width=1530,height=710)
        
        #------------------------------------------------------------------
        #TITLE
        title_lbl = Label(bgimg_lbl,text="CRIMINAL RECOGNITION SYSTEM SOFTWARE",font=('times new roman',35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        #---------
        # IMAGE BUTTONS
        #Criminal database button
        img5= Image.open("images/pabloescobar.jpg")
        img5= img5.resize((185,185),Image.ANTIALIAS)
        self.btnimg1= ImageTk.PhotoImage(img5)
        
        btn1= Button(bgimg_lbl,image=self.btnimg1,cursor="hand")
        btn1.place(x=180,y=100,width=185,height=185)
        
        btn1_1= Button(bgimg_lbl,text="Criminal Details",cursor="hand",font=('times new roman',20,"bold"),fg="red",highlightbackground='green',bg='blue')
        btn1_1.place(x=180,y=285,width=180,height=40)
        
        
        #Detect Face button
        img6= Image.open("images/techhuman.jpg")
        img6= img6.resize((185,185),Image.ANTIALIAS)
        self.btnimg2= ImageTk.PhotoImage(img6)
        
        btn2= Button(bgimg_lbl,image=self.btnimg2,cursor="hand")
        btn2.place(x=600,y=100,width=185,height=185)
        
        btn2_1= Button(bgimg_lbl,text="Train Faces",cursor="hand",font=('times new roman',20,"bold"),fg="red",highlightbackground='green',bg='blue')
        btn2_1.place(x=600,y=285,width=180,height=40)
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_system(root)
    root.mainloop()
    