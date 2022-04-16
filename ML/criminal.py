
from ast import Delete
from cProfile import label
from email import message
from email.errors import MalformedHeaderDefect
import string
from sys import builtin_module_names
from tkinter import *
from tkinter import ttk
from tkinter import font
from tokenize import String
from turtle import bgcolor, color, update, width     # Used to create stylish widgets
from PIL import Image, ImageTk  # Pillow is used to deal with images 
from matplotlib import image
from matplotlib.pyplot import fill, get, table, text
from numpy import character, delete
from pyparsing import White
from sklearn.linear_model import Ridge    
import mysql.connector 
from tkinter import messagebox


class Criminal:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1430x800+0+0") # Defining the window size
        self.root.title("CRIMINAL INFORMATION DATABASE") # window title
        
        
        #variables  which are used to get the input data
        self.var_case_Id = StringVar()
        self.var_Criminal_No = StringVar()
        self.var_name = StringVar()
        self.var_nickname = StringVar()
        self.var_arrest_date = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birthmark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()
        
        
        lbl_title = Label(self.root,text ="CRIMINAL INFORMATION DATABASE",font=('times new roman',40,'bold'),bg='orange',fg='navy')
        lbl_title.place(x=0,y=0,width=1500,height=70)
        
        # Police logo
        img_logo = Image.open('images/police_logo.png')
        img_logo = img_logo.resize((60,60),Image.ANTIALIAS) 
        self.photo_logo = ImageTk.PhotoImage(img_logo)
        
        self.logo = Label(self.root, image= self.photo_logo)
        self.logo.place(x= 300,y=5,width=60,height=60)

        #Image frame
        img_frame=Frame(self.root,bd=3,relief=RIDGE,bg='blue')
        img_frame.place(x=0,y=70, width=1440,height=130)
        
        # Images inside the frame
        img_1 = Image.open('images/criminal.jpg')
        img_1 = img_1.resize((540,160),Image.ANTIALIAS)
        self.photo_1 = ImageTk.PhotoImage(img_1)
        
        self.img_1 = Label(img_frame, image= self.photo_1)
        self.img_1.place(x=-60,y=0,width=540,height=160)
        
        img_2 = Image.open('images/handcuffs.jpg')
        img_2= img_2.resize((540,160),Image.ANTIALIAS)
        self.photo_2 = ImageTk.PhotoImage(img_2)
        
        self.img_2 = Label(img_frame, image= self.photo_2)
        self.img_2.place(x=450,y=0,width=540,height=160)
        
        img3= Image.open("images/cam2.jpg")
        img3= img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3= ImageTk.PhotoImage(img3)
        
        self.img_3= Label(img_frame,image= self.photoimg3)
        self.img_3.place(x=980,y=0,width=500,height=130)
        
        # Main Frame below the image frame
        Main_frame = Frame(self.root,bd=3,relief=RIDGE,bg='purple')
        Main_frame.place(x=5,y=205,width=1425,height=670)
        
        # Upper Frame
        upper_frame = LabelFrame(Main_frame,bd=3,relief=RIDGE,text='Criminal information',font=('times new roman',20,'bold'),fg='red',bg='white')
        upper_frame.place(x=7,y=7,width=1410,height=330)
        
        #Labels
        #CASE ID
        caseid = Label(upper_frame,text='Case ID: ',font=('arial',15,'bold'))
        caseid.grid(row=0,column=0,padx=2,sticky=W)
        #case ID Entry
        caseentry= ttk.Entry(upper_frame,textvariable=self.var_case_Id,width=22,font=('arial',15,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)
        
        #CRIMINAL NUMBER
        lbl_criminal_no = Label(upper_frame,text='Criminal No:',font=('arial',15,'bold'))
        lbl_criminal_no.grid(row=0,column=2,padx=2,pady=7,sticky=W)
        #Criminal Number Entry
        criminal_num_entry= ttk.Entry(upper_frame,textvariable=self.var_Criminal_No,width=22,font=('arial',15,'bold'))
        criminal_num_entry.grid(row=0,column=3,padx=2,pady=7)
        
        #CRIMINAL NAME
        lbl_criminal_name = Label(upper_frame,text='Criminal Name:',font=('arial',15,'bold'))
        lbl_criminal_name.grid(row=1,column=0,padx=2,pady=7,sticky=W)
        #Criminal Name Entry
        criminal_name_entry= ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',15,'bold'))
        criminal_name_entry.grid(row=1,column=1,padx=2,pady=7)
        
        #NICK NAME
        lbl_nickname = Label(upper_frame,text='Nick Name:',font=('arial',15,'bold'))
        lbl_nickname.grid(row=1,column=2,padx=2,pady=7,sticky=W)
        #Nickname Entry
        nickname_entry= ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=('arial',15,'bold'))
        nickname_entry.grid(row=1,column=3,padx=2,pady=7)
        
        #ARREST DATE
        lbl_arrestDate = Label(upper_frame,text='Arrest Date:',font=('arial',15,'bold'))
        lbl_arrestDate.grid(row=2,column=0,padx=2,pady=7,sticky=W)
        #Date Entry
        arrestDate_entry= ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=22,font=('arial',15,'bold'))
        arrestDate_entry.grid(row=2,column=1,padx=2,pady=7)
        
        #DATE OF CRIME COMMITTED
        lbl_date_of_crime = Label(upper_frame,text='Date of crime:',font=('arial',15,'bold'))
        lbl_date_of_crime.grid(row=2,column=2,padx=2,pady=7,sticky=W)
        #Date Entry
        arrest_date_entry= ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=22,font=('arial',15,'bold'))
        arrest_date_entry.grid(row=2,column=3,padx=2,pady=7)
    
        #ADDRESS
        lbl_address = Label(upper_frame,text='Address:',font=('arial',15,'bold'))
        lbl_address.grid(row=3,column=0,padx=2,pady=7,sticky=W)
        #Address Entry
        address_entry= ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',15,'bold'))
        address_entry.grid(row=3,column=1,padx=2,pady=7)
        
        #AGE
        lbl_age = Label(upper_frame,text='Age:',font=('arial',15,'bold'))
        lbl_age.grid(row=3,column=2,padx=2,pady=7,sticky=W)
        #Age Entry
        age_entry= ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('arial',15,'bold'))
        age_entry.grid(row=3,column=3,padx=2,pady=7)
        
        #OCCUPATION
        lbl_age = Label(upper_frame,text='Occupation:',font=('arial',15,'bold'))
        lbl_age.grid(row=4,column=0,padx=2,pady=7,sticky=W)
        #occupation Entry
        age_entry= ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=('arial',15,'bold'))
        age_entry.grid(row=4,column=1,padx=2,pady=7)
        
        
        #BIRTHMARK
        lbl_birthmark = Label(upper_frame,text='Birth Marks:',font=('arial',15,'bold'))
        lbl_birthmark.grid(row=4,column=2,padx=2,pady=7,sticky=W)
        #birthmark Entry
        birthmark_entry= ttk.Entry(upper_frame,textvariable=self.var_birthmark,width=22,font=('arial',15,'bold'))
        birthmark_entry.grid(row=4,column=3,padx=2,pady=7)
        
        
        #CRIME TYPE
        lbl_crimeType = Label(upper_frame,text='Crime Type:',font=('arial',15,'bold'))
        lbl_crimeType.grid(row=0,column=4,padx=2,pady=7,sticky=W)
        #crime type Entry
        crimeType_entry= ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=22,font=('arial',15,'bold'))
        crimeType_entry.grid(row=0,column=5,padx=2,pady=7)
        
        #FATHER NAME
        lbl_fatherName = Label(upper_frame,text='Father Name:',font=('arial',15,'bold'))
        lbl_fatherName.grid(row=1,column=4,padx=2,pady=7,sticky=W)
        #father name Entry
        father_entry= ttk.Entry(upper_frame,textvariable=self.var_father_name,width=22,font=('arial',15,'bold'))
        father_entry.grid(row=1,column=5,padx=2,pady=7)
        
        #GENDER
        lbl_gender = Label(upper_frame,text='Gender :',font=('arial',15,'bold'))
        lbl_gender.grid(row=2,column=4,padx=2,pady=7,sticky=W)
        
        #Radio butten gender Frame
        radio_frame_gender = Frame(upper_frame,bd=2,relief=RIDGE)
        radio_frame_gender.place(x=800,y=90,width=190,height=30)
        #Buttons
        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=('arial',15,'bold'))
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        
        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='female',font=('arial',15,'bold'))
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)
        
        
        #MOST WANTED Radio button
        lbl_wanted = Label(upper_frame,text='Most Wanted :',font=('arial',15,'bold'))
        lbl_wanted.grid(row=3,column=4,padx=2,pady=7,sticky=W)  
        
        #Radio butten wanted Frame
        radio_frame_wanted = Frame(upper_frame,bd=2,relief=RIDGE)
        radio_frame_wanted.place(x=800,y=130,width=190,height=30)  
        
        #Buttons
        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=('arial',15,'bold'))
        yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        
        No=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='No',value='no',font=('arial',15,'bold'))
        No.grid(row=0,column=1,pady=2,padx=5,sticky=W)    
        
        #BUTTONS FRAME
        button_frame =Frame(upper_frame,bd=2,relief=RIDGE)
        button_frame.place(x=5,y=225,width=675,height=45)
        
        #Adding buttons into buttons frame
        #save button
        btn_add = Button(button_frame,command=self.add_data,text='Save Record',font=('arial',15,'bold'),width= 14,fg='green')
        btn_add.grid(row=0,column=0,padx=0,pady=5)
        #Update
        btn_update = Button(button_frame,command=self.update_data,text='Update',font=('arial',15,'bold'),width= 14,fg='green',bg='blue')
        btn_update.grid(row=0,column=1,padx=0,pady=5)
        #Delete
        btn_delete = Button(button_frame,command=self.delete_data,text='Delete',font=('arial',15,'bold'),width= 14,fg='green')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)
        #Clear
        btn_clear = Button(button_frame,command=self.clear_data,text='Clear',font=('arial',15,'bold'),width= 14,fg='green')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)
        
        #Image inside upper Frame
        cbi_logo = Image.open('images/cbilogo.png')
        cbi_logo = cbi_logo.resize((470,245),Image.ANTIALIAS)
        self.cbiphoto = ImageTk.PhotoImage(cbi_logo)
        
        self.cbi_logo = Label(upper_frame, image= self.cbiphoto,bg='white')
        self.cbi_logo.place(x=1000,y=0,width=400,height=245)
    
        
        #------------------------LOWER FRAME -------------------------------------
        lower_frame = LabelFrame(Main_frame,bd=3,relief=RIDGE,text='Criminal information Table',font=('times new roman',20,'bold'),fg='red')
        lower_frame.place(x=7,y=340,width=1410,height=300)
        
        #Search Frame
        search_frame = LabelFrame(lower_frame,bd=3,relief=RIDGE,text='Search Criminal',font=('times new roman',20,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1410,height=80)
        
        #search lable
        lbl_search_by = Label(search_frame,font=("arial",15,"bold"),text='Search By : ',bg='yellow',fg='black')
        lbl_search_by.grid(row=0,column=0,sticky=W,padx=5)
        
        #COMBO BOX
        self.var_search_data = StringVar()
        combo_search_box = ttk.Combobox(search_frame,font=("arial",15,"bold"),width=18,state='readonly')
        combo_search_box["value"]=("Select Option","Case_id","Criminal_no")
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)
        
        # Search box entry
        self.var_search = StringVar()
        search_box_entry= ttk.Entry(search_frame,width=22,font=('arial',15,'bold'))
        search_box_entry.grid(row=0,column=2,padx=5,sticky=W)
        
        #Search Button
        searchButton = Button(search_frame,command=self.search_data,text='Search',font=('arial',15,'bold'),width= 14,fg='green')
        searchButton.grid(row=0,column=3,padx=3,pady=5)
        #All buttom
        show_btn= Button(search_frame,command=self.fetch_data,text='Show All',font=('arial',15,'bold'),width= 14,fg='green')
        show_btn.grid(row=0,column=4,padx=3,pady=5)
        
        #AGENCY NAME
        lbl_agencyName = Label(search_frame,text='CENTRAL BUREAU OF INVESTIGATION',font=('arial',25,'bold'),bg='white',fg='purple')
        lbl_agencyName.grid(row=0,column=5,padx=15,pady=0)
        
        # Table Frame inside lower frame
        table_frame= Frame(lower_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=3,y=73,width=1400,height=200)
        
        #Scroll Bar
        scroll_x= ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.criminal_table = ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)
        
        self.criminal_table.heading("1",text='CaseId')
        self.criminal_table.heading("2",text='CrimeNo')
        self.criminal_table.heading("3",text='Criminal Name')
        self.criminal_table.heading("4",text='Nickname')
        self.criminal_table.heading("5",text='ArrestDate')
        self.criminal_table.heading("6",text='DateOfCrime')
        self.criminal_table.heading("7",text='Address')
        self.criminal_table.heading("8",text='Age')
        self.criminal_table.heading("9",text='Occupation')
        self.criminal_table.heading("10",text='Birth Mark')
        self.criminal_table.heading("11",text='Crime Type')
        self.criminal_table.heading("12",text='Father Name')
        self.criminal_table.heading("13",text='Gender')
        self.criminal_table.heading("14",text='Wanted')
        
        self.criminal_table['show']='headings'
        
        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)
        
        self.criminal_table.pack(fill=BOTH,expand=1)
        
        self.fetch_data()
    
    
    
    # Adding data function
    def add_data(self):
        if self.var_case_Id.get()=="":
            messagebox.showerror('Error',"All Fields are required")
        else:
            try:
                conn = mysql.connector.connect(host ="localhost",username="root",password="Bnpchowdary7@2002",database= "management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_case_Id.get(),self.var_Criminal_No.get(),self.var_name.get(),self.var_nickname.get(),self.var_arrest_date.get(),self.var_date_of_crime.get(),self.var_address.get(),self.var_age.get(),self.var_occupation.get(),self.var_birthmark.get(),self.var_crime_type.get(),self.var_father_name.get(),self.var_gender.get(),self.var_wanted.get()))                                                                         
                conn.commit()
                self.fetch_data()  #calling fetch_data function
                self.clear_data() # calling clear_data function
                conn.close()
                messagebox.showinfo('success','Criminal record has been added successfully')
            except Exception as es:
                messagebox.showerror('Error',f"Due To{str(es)}")     
            
                
    # Fetching data from the database
    def fetch_data(self):
        conn = mysql.connector.connect(host ="localhost",username="root",password="Bnpchowdary7@2002",database= "management")
        my_cursor = conn.cursor()
        my_cursor.execute('select * from criminal')
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()    
        
    #get cursor
    
    def get_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content = self.criminal_table.item(cursor_row)
        data = content['values']
        
        self.var_case_Id.set(data[0])   
        self.var_Criminal_No.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthmark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12]) 
        self.var_wanted.set(data[13])
        
    #Update button functionality
    def update_data(self):
        if self.var_case_Id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                update= messagebox.askyesno('Update',"Are you sure to update this criminal record")
                if update>0:
                    conn = mysql.connector.connect(host ="localhost",username="root",password="Bnpchowdary7@2002",database= "management")
                    my_cursor = conn.cursor()
                    my_cursor.execute('update criminal set Criminal_no=%s,criminal_name=%s,Nick_name=%s,arrest_date=%s,dateOfCrime=%s,address=%s,age=%s,occupation=%s,birthmark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s where Case_id=%s',(
                    
                                                                                                                                                                                                                                                    self.var_Criminal_No.get(),
                                                                                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                                                                                    self.var_nickname.get(),
                                                                                                                                                                                                                                                    self.var_arrest_date.get(),
                                                                                                                                                                                                                                                    self.var_date_of_crime.get(),
                                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                                    self.var_age.get(),
                                                                                                                                                                                                                                                    self.var_occupation.get(),
                                                                                                                                                                                                                                                    self.var_birthmark.get(),
                                                                                                                                                                                                                                                    self.var_crime_type.get(),
                                                                                                                                                                                                                                                    self.var_father_name.get(),
                                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                                    self.var_wanted.get(),
                                                                                                                                                                                                                                                    self.var_case_Id.get(),
                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                 ))
                    
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()# calling fetch data function
                self.clear_data() #calling clear data function
                conn.close()
                messagebox.showinfo('Success','Successfully Updated the Record')
            except Exception as es:
                messagebox.showerror("Error",f'Due To {str(es)}')
                
            
    #delete button functionality
    def delete_data(self):
        if self.var_case_Id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                Delete= messagebox.askyesno('Delete',"Are you sure to Delete this criminal record")
                if Delete>0:
                    conn = mysql.connector.connect(host ="localhost",username="root",password="Bnpchowdary7@2002",database= "management")
                    my_cursor = conn.cursor()   
                    sql='delete from criminal where Case_id=%s'
                    value=(self.var_case_Id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data() #calling the clear function
                conn.close()
                messagebox.showinfo('Success','Successfully Deleted the Record')
            except Exception as es:
                messagebox.showerror("Error",f'Due To {str(es)}')
                
    #Clear Button Functionality
    def clear_data(self):
        self.var_case_Id.set("")   
        self.var_Criminal_No.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthmark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("") 
        self.var_wanted.set("")
        
    #search Button functionality
    def search_data(self):
        if self.var_search_data.get()=='':
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host ="localhost",username="root",password="Bnpchowdary7@2002",database= "management")
                my_cursor=conn.cursor()
                my_cursor.execute('select * from criminal where ' +str(self.var_search_data.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')
            
        
                
                
                
        
            
        
if __name__ == "__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()