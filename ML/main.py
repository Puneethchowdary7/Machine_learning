from cProfile import label
from tkinter import * # Used to create the GUI
from tkinter import ttk # This module contains widgets
import os, sys
from turtle import width
from PIL import Image,ImageTk
from matplotlib import image
from criminal import Criminal# This module is used to deal with images
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
        
        img2= Image.open("images/techface.png")
        img2= img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2= ImageTk.PhotoImage(img2)
        
        second_lbl= Label(self.root,image= self.photoimg2)
        second_lbl.place(x=500,y=0,width=500,height=130)
        
        img3= Image.open("images/cam2.jpg")
        img3= img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3= ImageTk.PhotoImage(img3)
        
        third_lbl= Label(self.root,image= self.photoimg3)
        third_lbl.place(x=1000,y=0,width=500,height=130)
        #-----------------------------------------------------------------
        #Background image
        img4= Image.open("images/dj.jpg")
        img4= img4.resize((1530,710),Image.ANTIALIAS)
        self.bgimg= ImageTk.PhotoImage(img4)
        
        bgimg_lbl= Label(self.root,image= self.bgimg)
        bgimg_lbl.place(x=0,y=120,width=1530,height=800)
        
        
        
        
        
        #------------------------------------------------------------------
        #TITLE
        title_lbl = Label(bgimg_lbl,text="CRIMINAL RECOGNITION SYSTEM SOFTWARE",font=('times new roman',35,"bold"),bg="navy",fg="orange")
        title_lbl.place(x=-5,y=0,width=1530,height=60)
        #---------
        # IMAGE BUTTONS
    
        #Criminal database button
        img5= Image.open("images/pabloescobar.jpg")
        img5= img5.resize((190,190),Image.ANTIALIAS)
        self.btnimg1= ImageTk.PhotoImage(img5)
        
        btn1= Button(bgimg_lbl,image=self.btnimg1,command=self.criminal_database,cursor="hand")
        btn1.place(x=350,y=100,width=185,height=185)
        
        btn1_1= Button(bgimg_lbl,text="Criminal Details",command=self.criminal_database,cursor="hand",font=('times new roman',20,"bold"),fg="white",highlightbackground='red',bg='blue')
        btn1_1.place(x=350,y=285,width=180,height=40)
        
        
        #Detect Face button
        img6= Image.open("images/detect.webp")
        img6= img6.resize((185,185),Image.ANTIALIAS)
        self.btnimg2= ImageTk.PhotoImage(img6)
        
        btn2= Button(bgimg_lbl,image=self.btnimg2,cursor="hand")
        btn2.place(x=700,y=100,width=185,height=185)
        
        btn2_1= Button(bgimg_lbl,text="Face Detector",cursor="hand",font=('times new roman',20,"bold"),fg="white",highlightbackground='red',bg='blue')
        btn2_1.place(x=700,y=285,width=180,height=40)
        
        #Help Desk button
        img6= Image.open("images/helpdesk.png")
        img6= img6.resize((185,185),Image.ANTIALIAS)
        self.btnimg2= ImageTk.PhotoImage(img6)
        
        btn2= Button(bgimg_lbl,image=self.btnimg2,cursor="hand")
        btn2.place(x=1000,y=100,width=185,height=185)
        
        btn2_1= Button(bgimg_lbl,text="Help Desk",cursor="hand",font=('times new roman',20,"bold"),fg="white",highlightbackground='red',bg='blue')
        btn2_1.place(x=1000,y=285,width=180,height=40)
        #================
       
        #Train Data button
        img5= Image.open("images/processing.jpeg")
        img5= img5.resize((190,190),Image.ANTIALIAS)
        self.btnimg1= ImageTk.PhotoImage(img5)
        
        btn1= Button(bgimg_lbl,image=self.btnimg1,cursor="hand")
        btn1.place(x=350,y=400,width=185,height=185)
        
        btn1_1= Button(bgimg_lbl,text="Train Data",cursor="hand",font=('times new roman',20,"bold"),fg="white",highlightbackground='red',bg='blue')
        btn1_1.place(x=350,y=585,width=180,height=40)
        
        
        #Photos button
        img6= Image.open("images/photos.jpg")
        img6= img6.resize((185,185),Image.ANTIALIAS)
        self.btnimg2= ImageTk.PhotoImage(img6)
        
        btn2= Button(bgimg_lbl,image=self.btnimg2,cursor="hand")
        btn2.place(x=700,y=400,width=185,height=185)
        
        btn2_1= Button(bgimg_lbl,text="Photos",cursor="hand",font=('times new roman',20,"bold"),fg="white",highlightbackground='red',bg='blue')
        btn2_1.place(x=700,y=585,width=180,height=40)
        
        #Exit Button
        img6= Image.open("images/exit.png")
        img6= img6.resize((185,185),Image.ANTIALIAS)
        self.btnimg2= ImageTk.PhotoImage(img6)
        
        btn2= Button(bgimg_lbl,image=self.btnimg2,cursor="hand")
        btn2.place(x=1000,y=400,width=185,height=185)
        
        btn2_1= Button(bgimg_lbl,text="Exit",cursor="hand",font=('times new roman',20,"bold"),fg="white",highlightbackground='red',bg='blue')
        btn2_1.place(x=1000,y=585,width=180,height=40)
        
    # ----------Giving functionality to the buttons
    def criminal_database(self):
        self.new_window = Toplevel(self.root)
        self.app = Criminal(self.new_window)
        
    
    
    
    

if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_system(root)
    root.mainloop()
    