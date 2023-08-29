from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
    

root = Tk() # GUI window.
root.title('Student Management System')
root.iconbitmap('student-icon.ico')
root.geometry('900x550+200+120') # widthxheight+xpadding+ypadding..
root.configure(bg='LightPink')
#Load an image in the script
img= (Image.open("image1.png"))
#Resize the Image using resize method
resized_image= img.resize((150,150))
new_image= ImageTk.PhotoImage(resized_image)
label1 = Label(root,image=new_image, bg='LightPink')
label1.grid(padx=120,pady=120)

frame1 = Frame(root,relief='groove',bg='PaleVioletRed',borderwidth=3)
frame1.place(x=40,y=270,width=350,height=250)

def addstudent(): 
   
   
    def added(): 
       
        id = idval.get()
        name = nameval.get()
        Number= numberval.get()
        email = emailval.get()
        Gender = genderval.get()
        dob = dobval.get()
        adress = adressval.get()
        try:
            str1 = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(str1,(id,name,Number,email,Gender,dob,adress))
            con.commit()
            res = messagebox.askyesnocancel("messageinfo",'Data added Succesfully.')
            if(res==True):
                idval.set('')
                nameval.set('')
                numberval.set('')
                emailval.set('')
                genderval.set('')
                dobval.set('')
                adressval.set('')
           
        except:
            y = messagebox.showerror("erroemessage","Student Id already exists.Try another Id")
        str = 'select * from studentdata'
        mycursor.execute(str)
        data = mycursor.fetchall() # fetches all data from database table.
        dbtable.delete(*dbtable.get_children())
        for i in data:
            val = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
            dbtable.insert('',END,values=val)
       
        
     
    new2 = Toplevel()
    new2.grab_set() # it prevents working with main window until we close the top level window...
    new2.geometry('380x330')
    new2.config(bg='PaleVioletRed')
    new2.iconbitmap('student-icon.ico')
    new2.title('Add Student')
    # database connection...............................#
    
    #..................................................#
    id = Label(new2,text='Student Id:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    id.place(x = 10,y=30)
    name = Label(new2,text='Student Name:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    name.place(x = 10,y=60)
    Number = Label(new2,text='Mobile Number:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    Number.place(x = 10,y=90)
    email = Label(new2,text='Email Address:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    email.place(x = 10,y=120)
    Gender = Label(new2,text='Gender:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    Gender.place(x = 10,y=150)
    dob = Label(new2,text='Date Of Birth:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    dob.place(x = 10,y=180)
    adress = Label(new2,text='Address:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    adress.place(x = 10,y=210)
    idval = IntVar()
    identry = Entry(new2,width=35,textvariable=idval)
    identry.place(x = 130, y = 32)
    nameval = StringVar()
    nameentry = Entry(new2,width=35,textvariable=nameval)
    nameentry.place(x=130,y=62)
    numberval = StringVar()
    numberentry = Entry(new2,width=35,textvariable=numberval)
    numberentry.place(x = 130, y = 92)
    emailval = StringVar()
    emailentry = Entry(new2,width=35,textvariable=emailval)
    emailentry.place(x=130,y=122)
    genderval = StringVar()
    genderentry = Entry(new2,width=35,textvariable=genderval)
    genderentry.place(x=130,y=152)
    dobval = StringVar()
    dobentry = Entry(new2,width=35,textvariable=dobval)
    dobentry.place(x=130,y=182)
    adressval = StringVar()
    adressentry = Entry(new2,width=35,textvariable=adressval)
    adressentry.place(x=130,y=212)
    submitbutton = Button(new2,text='Submit',command=added,font=('Arial','13','bold'),fg='Red')
    submitbutton.place(x = 110, y = 250)

def searchstudent(): 
    def searchdb():
        id = idvalue.get()
        name = nameval.get()
        Number= numberval.get()
        email = emailval.get()
        Gender = genderval.get()
        dob = dobval.get()
        adress = adressval.get()
        if(id!=0):
            str = 'select * from studentdata where StudentId=%s'
            mycursor.execute(str,(id))
            data = mycursor.fetchall() # fetches all data from database table.
            dbtable.delete(*dbtable.get_children())
            for i in data:
              val = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
              dbtable.insert('',END,values=val)
        elif(name!=''):
            str = 'select * from studentdata where StudentName=%s'
            mycursor.execute(str,(name))
            data = mycursor.fetchall() # fetches all data from database table.
            dbtable.delete(*dbtable.get_children())
            for i in data:
              val = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
              dbtable.insert('',END,values=val)
        elif(Number!=''):
            str = 'select * from studentdata where MobileNumber=%s'
            mycursor.execute(str,(Number))
            data = mycursor.fetchall() # fetches all data from database table.
            dbtable.delete(*dbtable.get_children())
            for i in data:
              val = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
              dbtable.insert('',END,values=val)
        elif(email!=''):
            str = 'select * from studentdata where Email=%s'
            mycursor.execute(str,(email))
            data = mycursor.fetchall() # fetches all data from database table.
            dbtable.delete(*dbtable.get_children())
            for i in data:
              val = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
              dbtable.insert('',END,values=val)
        elif(Gender!=''):
            str = 'select * from studentdata where Gender=%s'
            mycursor.execute(str,(Gender))
            data = mycursor.fetchall() # fetches all data from database table.
            dbtable.delete(*dbtable.get_children())
            for i in data:
              val = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
              dbtable.insert('',END,values=val)
        elif(dob!=''):
            str = 'select * from studentdata where BirthDate=%s'
            mycursor.execute(str,(dob))
            data = mycursor.fetchall() # fetches all data from database table.
            dbtable.delete(*dbtable.get_children())
            for i in data:
              val = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
              dbtable.insert('',END,values=val)
        elif(adress!=''):
            str = 'select * from studentdata where Address=%s'
            mycursor.execute(str,(adress))
            data = mycursor.fetchall() # fetches all data from database table.
            dbtable.delete(*dbtable.get_children())
            for i in data:
              val = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
              dbtable.insert('',END,values=val)
    new2 = Toplevel()
    new2.grab_set() # it prevents working with main window until we close the top level window...
    new2.geometry('380x330')
    new2.config(bg='PaleVioletRed')
    new2.iconbitmap('student-icon.ico')
    new2.title('Search Student')
    id = Label(new2,text='Student Id:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    id.place(x = 10,y=30)
    name = Label(new2,text='Student Name:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    name.place(x = 10,y=60)
    Number = Label(new2,text='Mobile Number:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    Number.place(x = 10,y=90)
    email = Label(new2,text='Email Address:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    email.place(x = 10,y=120)
    Gender = Label(new2,text='Gender:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    Gender.place(x = 10,y=150)
    dob = Label(new2,text='Date Of Birth:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    dob.place(x = 10,y=180)
    adress = Label(new2,text='Address:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    adress.place(x = 10,y=210)
    idvalue = IntVar()
    identry = Entry(new2,width=35,textvariable=idvalue)
    identry.place(x = 130, y = 32)
    nameval = StringVar()
    nameentry = Entry(new2,width=35,textvariable=nameval)
    nameentry.place(x=130,y=62)
    numberval = StringVar()
    numberentry = Entry(new2,width=35,textvariable=numberval)
    numberentry.place(x = 130, y = 92)
    emailval = StringVar()
    emailentry = Entry(new2,width=35,textvariable=emailval)
    emailentry.place(x=130,y=122)
    genderval = StringVar()
    genderentry = Entry(new2,width=35,textvariable=genderval)
    genderentry.place(x=130,y=152)
    dobval = StringVar()
    dobentry = Entry(new2,width=35,textvariable=dobval)
    dobentry.place(x=130,y=182)
    adressval = StringVar()
    adressentry = Entry(new2,width=35,textvariable=adressval)
    adressentry.place(x=130,y=212)
    submitbutton = Button(new2,text='Search',command=searchdb,font=('Arial','13','bold'),fg='Red')
    submitbutton.place(x = 110, y = 250)
    
def deletestudent():
    cc = dbtable.focus()
    content = dbtable.item(cc)
    x = content['values'][0]
    str1  = 'delete from studentdata where StudentId=%s'
    mycursor.execute(str1,(x))
    con.commit()
    messagebox.showinfo("info","Data deleted successfully.")
    str = 'select * from studentdata'
    mycursor.execute(str)
    data = mycursor.fetchall() # fetches all data from database table.
    dbtable.delete(*dbtable.get_children())
    for i in data:
            val = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
            dbtable.insert('',END,values=val)
    
def updatestudent(): 
    def update(): 
        id = idval.get()
        name = nameval.get()
        Number= numberval.get()
        email = emailval.get()
        Gender = genderval.get()
        dob = dobval.get()
        adress = adressval.get()
        str = 'update studentdata set StudentId=%s,StudentName=%s,MobileNumber=%s,Email=%s,Gender=%s,BirthDate=%s,Address=%s where StudentId=%s'
        mycursor.execute(str,(id,name,Number,email,Gender,dob,adress,id))
        con.commit()
        x = messagebox.showinfo("info","Data updated successfully.")
        str1 = 'select * from studentdata'
        mycursor.execute(str1)
        data = mycursor.fetchall() # fetches all data from database table.
        dbtable.delete(*dbtable.get_children())
        for i in data:
              val = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
              dbtable.insert('',END,values=val)
        
    new2 = Toplevel()
    new2.grab_set() # it prevents working with main window until we close the top level window...
    new2.geometry('380x330')
    new2.config(bg='PaleVioletRed')
    new2.iconbitmap('student-icon.ico')
    new2.title('Update Student')
    id = Label(new2,text='Student Id:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    id.place(x = 10,y=30)
    name = Label(new2,text='Student Name:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    name.place(x = 10,y=60)
    Number = Label(new2,text='Mobile Number:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    Number.place(x = 10,y=90)
    email = Label(new2,text='Email Address:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    email.place(x = 10,y=120)
    Gender = Label(new2,text='Gender:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    Gender.place(x = 10,y=150)
    dob = Label(new2,text='Date Of Birth:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    dob.place(x = 10,y=180)
    adress = Label(new2,text='Address:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    adress.place(x = 10,y=210)
    idval = IntVar()
    identry = Entry(new2,width=35,textvariable=idval)
    identry.place(x = 130, y = 32)
    nameval = StringVar()
    nameentry = Entry(new2,width=35,textvariable=nameval)
    nameentry.place(x=130,y=62)
    numberval = StringVar()
    numberentry = Entry(new2,width=35,textvariable=numberval)
    numberentry.place(x = 130, y = 92)
    emailval = StringVar()
    emailentry = Entry(new2,width=35,textvariable=emailval)
    emailentry.place(x=130,y=122)
    genderval = StringVar()
    genderentry = Entry(new2,width=35,textvariable=genderval)
    genderentry.place(x=130,y=152)
    dobval = StringVar()
    dobentry = Entry(new2,width=35,textvariable=dobval)
    dobentry.place(x=130,y=182)
    adressval = StringVar()
    adressentry = Entry(new2,width=35,textvariable=adressval)
    adressentry.place(x=130,y=212)
    submitbutton = Button(new2,text='Update',command=update,font=('Arial','13','bold'),fg='Red')
    submitbutton.place(x = 110, y = 250)
    cc = dbtable.focus()
    content = dbtable.item(cc)
    x = content['values']
    idval.set(x[0])
    nameval.set(x[1])
    numberval.set(x[2])
    emailval.set(x[3])
    genderval.set(x[4])
    dobval.set(x[5])
    adressval.set(x[6])

def showall(): 
    str1 = 'select * from studentdata'
    mycursor.execute(str1)
    data = mycursor.fetchall() # fetches all data from database table.
    dbtable.delete(*dbtable.get_children())
    for i in data:
              val = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
              dbtable.insert('',END,values=val)




addbutton = Button(frame1,text='Add Student',command=addstudent,font=('Arial','13','bold'),fg='OrangeRed')
addbutton.place(x = 10,y = 10)
searchbutton = Button(frame1,text='Search Student',command=searchstudent,font=('Arial','13','bold'),fg='OrangeRed')
searchbutton.place(x = 190,y = 10)
Deletebutton = Button(frame1,text='Delete Student',command=deletestudent,font=('Arial','13','bold'),fg='OrangeRed')
Deletebutton.place(x = 5,y = 65)
Updatebutton = Button(frame1,text='Update Student',command=updatestudent,font=('Arial','13','bold'),fg='OrangeRed')
Updatebutton.place(x = 190,y = 65)
showbutton = Button(frame1,text='Show all data',command=showall,font=('Arial','13','bold'),fg='OrangeRed')
showbutton.place(x = 90,y = 130)
exitbutton = Button(frame1,text='Exit',command=root.quit,font=('Arial','13','bold'),fg='OrangeRed')
exitbutton.place(x = 130, y = 190)


headerframe = Frame(root,relief='groove',bg='LightPink',borderwidth=0)
headerframe.place(x=210,y=10,width=450,height=100)
headerlabel = Label(headerframe,text='StudentManagementSystem',font=('chiller','38','italic bold'),bg='LightPink',fg='OrangeRed')
headerlabel.grid(pady=2,padx=10)

def connectdatabase():
    def submitdb(): 
        global con,mycursor
        user = userval.get()
        password = passwordval.get() 
        host  = hostval.get()
        # print(user,password)
        try:                         # connecting to mysql server..
            user = userval.get()
            password = passwordval.get()
            host = hostval.get()
            con = pymysql.connect(user=user,password=password,host=host)
            mycursor = con.cursor()
            messagebox.showinfo("logininfo","login success,connected to the database.")
        except:
            messagebox.showerror("error message","Invalid Credentials.Try again!!")
            return
        try:
            str1 = 'create database studentmanagementsystem'
            mycursor.execute(str1)
            str2 = 'use studentmanagementsystem'
            mycursor.execute(str2)
            str3 = 'create table studentdata(StudentId int,StudentName varchar(30),MobileNumber varchar(12),Email varchar(30),Gender varchar(10),BirthDate varchar(20),Address varchar(100))'
            mycursor.execute(str3)
           
        except:
            str2 = 'use studentmanagementsystem'
            mycursor.execute(str2)
            str4 = 'alter table studentdata modify column StudentId int not null'
            mycursor.execute(str4)
            str5 = 'alter table studentdata modify column StudentId int primary key'
            mycursor.execute(str5)
            
        
            
           
            
    new1 = Toplevel()
    new1.grab_set() # it prevents working with main window until we close the top level window...
    new1.geometry('400x200')
    new1.config(bg='PaleVioletRed')
    new1.title('Connect Database')
    new1.iconbitmap('student-icon.ico')
    userlable = Label(new1,text='UserName:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    userlable.place(x = 10,y=30)
    passwordlable = Label(new1,text='Password:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    passwordlable.place(x = 10,y=60)
    hostlable = Label(new1,text='Host:',font=('Arial','10','bold'),fg='OrangeRed',bg='lavender')
    hostlable.place(x = 10,y=90)
    userval = StringVar()
    userentry = Entry(new1,width=40,textvariable=userval,show='*')
    userentry.place(x = 130, y = 32)
    passwordval = StringVar()
    passwordentry = Entry(new1,width=40,textvariable=passwordval,show='*' )
    passwordentry.place(x=130,y=62)
    hostval = StringVar()
    hostentry = Entry(new1,width=40,textvariable=hostval)
    hostentry.place(x = 130, y = 92)
    submitbutton = Button(new1,text='Submit',command=submitdb,font=('Arial','13','bold'),fg='Red')
    submitbutton.place(x = 130, y = 140)


frame2 = Frame(root,relief='solid',borderwidth=1)
frame2.place(x=420,y=90,width=450,height=450)
style = ttk.Style()
style.configure('Treeview.Heading',foreground='blue',bg='Pink',font=('Arial','10','bold'))
style.configure('Treeview',foreground='OrangeRed',font=('Arial','10','bold'))
Scrol_x = Scrollbar(frame2,orient=HORIZONTAL) # used to create scrollbar ..
Scrol_y = Scrollbar(frame2,orient=VERTICAL)
    
dbtable = Treeview(frame2,columns=('StudentId','StudentName','MobileNumber','Email','Gender','BirthDate','Address'),xscrollcommand=Scrol_x.set,yscrollcommand=Scrol_y.set)
    
Scrol_x.pack(side=BOTTOM,fill='x')
Scrol_y.pack(side=RIGHT,fill='y')
Scrol_x.config(command=dbtable.xview)
Scrol_y.config(command=dbtable.yview)
dbtable.heading('StudentId', text='StudentId') #headings...
dbtable.heading('StudentName', text='StudentName')
dbtable.heading('MobileNumber', text='MobileNumber')
dbtable.heading('Email', text='Email')
dbtable.heading('Gender', text='Gender')
dbtable.heading('BirthDate', text='BirthDate')
dbtable.heading('Address', text='Address')
dbtable.column('StudentId', width='100')   #columns...
dbtable.column('StudentName', width='300')
dbtable.column('MobileNumber', width='130')
dbtable.column('Email', width='250')
dbtable.column('Gender', width='100')
dbtable.column('BirthDate',width='130')
dbtable.column('Address', width='500')
dbtable['show'] = 'headings' # display only headings..
dbtable.pack(expand=1,fill='both',padx=0)
    
    
        
connectbutton = Button(root,text='Connect to database',font=('Arial','14','bold'),bg='white',fg='OrangeRed',activebackground='yellow',command=connectdatabase) # database connector..
connectbutton.place(x = 670, y=27)

root.mainloop()

