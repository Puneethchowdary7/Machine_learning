from tkinter import * # Used to create the GUI
from tkinter import ttk # This module contains widgets
import os, sys
from PIL import Image # This module is used to deal with images

# 
class Face_recognition_system: 
    def __init__(self,root):
        self.root = root
        self.root.geometry("1280x800+0+0")
        self.root.title("Face Recogniton System")




if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_system(root)
    root.mainloop()