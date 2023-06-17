from cProfile import label
from cgitb import text
from lib2to3.pytree import LeafPattern
from operator import le
from os import curdir
from sre_constants import JUMP
from tkinter import *
import sqlite3
import cv2
import face_recognition
import os
from cv2 import destroyAllWindows

from numpy import delete, disp, number


global conn,cur
conn = sqlite3.connect('database.db')
cur = conn.cursor()


def upgrade():
   
    print(emp_id,fname,lname,emailname,phoneno)
    cur.execute("Update employees2108 set first_name = '"+fname.get()+"',last_name ='"+lname.get()+"',email = '"+emailname.get()+"',phoneno = '"+phoneno.get()+"' where empid ='"+emp_id.get()+"'")
    conn.commit()
    cur.execute("select * from employees2108")
    print(cur.fetchall())
    conn.commit()
    fram.destroy()
    disptable()

def takePhoto():
    cam = cv2.VideoCapture(0)
    
    img_counter = 0
    while True:
        nothing = 0

def stuVerify():

    cur.execute("insert into employees2108 values ('"+stu_empid_entry.get()+"','"+stu_first_name_entry.get()+"','"+stu_second_name_entry.get()+"','"+stu_email_entry.get()+"','"+stu_phone_entry.get()+"')")
    conn.commit()
    fram.destroy()
    disptable()

def delcontent():
    cur.execute("delete from employees2108 where empid = '"+del_empid.get()+"'")
    conn.commit()
    fram.destroy()
    disptable()

def addtable():
    global add_stu_window, stu_first_name_entry
    global stu_second_name_entry
    global stu_email_entry
    global stu_phone_entry
    global stu_empid_entry
    global stu_submit_button
    
    #cur.execute("CREATE TABLE STUDENT_DETAILS(first_name text, second_name text, email text, id text, password text, ph_num integer)")
    #conn.commit()
    #cur.execute("CREATE TABLE counts(count_type text, count1 integer)")
    #conn.commit()
    #cur.execute("INSERT INTO counts VALUES('student_user_id_count', 9999)")
    #conn.commit()
    #cur.execute("SELECT * FROM counts")
    #print(cur.fetchall())
    #cur.execute("DELETE FROM counts")
    #conn.commit()
    cur.execute("SELECT * FROM employees2108")
    print(cur.fetchall())
    add_stu_window = Tk()
    add_stu_window.title("Add Students")

    stu_empid_label = Label(add_stu_window, text= " Employee Id :").grid(row=1, column=1)
    stu_empid_entry = Entry(add_stu_window, text="Employee Id")
    stu_empid_entry.grid(row=1, column=2, padx=11, pady=11)

    stu_first_name_label = Label(add_stu_window, text = "First name : ")
    stu_first_name_label.grid(row=2, column=1)
    stu_first_name_entry = Entry(add_stu_window, text="First Name")
    stu_first_name_entry.grid(row=2, column=2, padx=11, pady=11)

    
    stu_second_name_label = Label(add_stu_window, text= "Last name").grid(row=3, column=1)
    stu_second_name_entry = Entry(add_stu_window, text="Last name")
    stu_second_name_entry.grid(row=3, column=2, padx=11, pady=11)

    stu_email_label = Label(add_stu_window, text= " Email :").grid(row=4, column=1)
    stu_email_entry = Entry(add_stu_window, text="Email")
    stu_email_entry.grid(row=4, column=2, padx=11, pady=11)

    stu_phone_label = Label(add_stu_window, text= " Mobile number :").grid(row=5, column=1)
    stu_phone_entry = Entry(add_stu_window,  text="Phone number")
    stu_phone_entry.grid(row=5, column=2, padx=11, pady=11)


    stu_submit_button = Button(add_stu_window, text="Submit",command=stuVerify).grid(row=7, column=2)
    cancelbtn = Button(add_stu_window,text='Cancel',fg='white',bg='red',command=add_stu_window.destroy).grid(row=7,column=4)
    


def updtable():
    enter = Tk()
    enterfram = Frame(enter,border=10)
    enterfram.grid(padx=70,pady=50)
    enter.title('Entry Data')
    global emp_id,fname,lname,emailname,phoneno

    emp_idl = Label(enterfram, text= " Employee Id :").grid(row=1, column=1)
    emp_id = Entry(enterfram, text="Employee Id")
    emp_id.grid(row=1, column=2, padx=11, pady=11)

    fnamel = Label(enterfram, text = "First name : ")
    fnamel.grid(row=2, column=1)
    fname = Entry(enterfram, text="First Name")
    fname.grid(row=2, column=2, padx=11, pady=11)

    
    lnamel = Label(enterfram, text= "Last name").grid(row=3, column=1)
    lname = Entry(enterfram, text="Last name")
    lname.grid(row=3, column=2, padx=11, pady=11)

    emaill = Label(enterfram, text= " Email :").grid(row=4, column=1)
    emailname = Entry(enterfram, text="Email")
    emailname.grid(row=4, column=2, padx=11, pady=11)

    phonenol = Label(enterfram, text= " Mobile number :").grid(row=5, column=1)
    phoneno = Entry(enterfram,  text="Phone number")
    phoneno.grid(row=5, column=2, padx=11, pady=11)

    apply = Button(enterfram,text='Add',bg='green',fg='white',command=upgrade).grid(row=8,column=2,pady=11,padx=11)  
    update_btn = Button(enterfram,text='cancel',bg='red',fg='white',command=enter.destroy).grid(row=10,column=2,pady=11,padx=11)
    # delete_btn = Button(fram,text='Delete',bg='red',fg='white',command=deletetable).grid(row=8,column=20,pady=18,padx=20)
    
    # destroyAllWindows()
    # disptable()

def deletetable():
    global del_empid
    delwin = Tk()
    delframe = Frame(delwin,border=10)
    delframe.grid(padx=70,pady=50)
    delwin.title('Entry Data')

    delempidl = Label(delframe,text='Enter the employee id you want to remove').grid(row=1,column=1)
    del_empid = Entry(delframe,text='Employee Id')
    del_empid.grid(row=2,column=1)

    reove = Button(delframe,text='Remove',bg='red',fg='white',command=delcontent).grid(row=3,column=1,pady=11,padx=11)  
    cancelbt = Button(delframe,text='cancel',bg='green',fg='white',command=delwin.destroy).grid(row=4,column=2,pady=11,padx=11)

def disptable():
    
    global display,fram
    display = Tk()
    fram = Frame(display,border=10)
    fram.grid(padx=100,pady=100)
    display.title('Tables')
    # cur.execute("Insert into employees2108 values ('101','Sughosh','Rathod','101@gmail.com',1011011011)")
    # conn.commit()
    cur.execute("Select * from employees2108")  
    output = cur.fetchall()
    conn.commit()
    rw = 2
    Label(fram,text='Emp Id').grid(row=1,column=1)
    Label(fram,text='First Name').grid(row=1,column=2)
    Label(fram,text='Last Name').grid(row=1,column=3)
    Label(fram,text='Email').grid(row=1,column=4)
    Label(fram,text='Phone Number').grid(row=1,column=5)
    for i in output:
        col = 1
        for j in i:
            Label(fram,text=j).grid(row=rw,column=col)
            col += 1
        rw += 1
    rw = 2
    
    add_btn = Button(fram,text='Add',bg='green',fg='white',command=addtable).grid(row=4,column=20,pady=18,padx=20)  
    update_btn = Button(fram,text='Update',bg='blue',fg='white',command=updtable).grid(row=6,column=20,pady=18,padx=20)
    delete_btn = Button(fram,text='Delete',bg='red',fg='white',command=deletetable).grid(row=8,column=20,pady=18,padx=20)
    
    display.mainloop()
    cap.release()
    cv2.destroyAllWindows()

def read_img(path):
    img = cv2.imread(path)
    (h,w) = img.shape[:2]
    width = 500
    ratio = width / float(w)
    height = int(h * ratio)
    return cv2.resize(img,(width,height))
          
known_encodings = []
known_names = []
known_dir = 'known'
tolerance = 0.5
MODEL = 'cnn'

for file in os.listdir(known_dir):
    img  = read_img(known_dir + '/' + file)
    img_enc = face_recognition.face_encodings(img)[0]
    known_encodings.append(img_enc)
    known_names.append(file.split('.')[0])

cap = cv2.VideoCapture(0)

root = Tk()
user_id = StringVar()
passw = StringVar()
ref_label = Label(root, text="Admin Login").grid(columnspan=9, pady=10)
login_frame = Frame(root, border=5)
login_frame.grid(padx=50, pady=30)
root.title("Admin Login")
user_id_label =  Label(login_frame, text="User Id             :").grid(row=0,column=5, pady=11)
user_id_text_box = Entry(login_frame, text="Enter the User Id ", textvariable=user_id).grid(row=0, column=6, pady=11)
user_id_pass =  Label(login_frame, text="Password            :").grid(row=1,column=5)
user_id_pass_box = Entry(login_frame, text="Enter the Password :", textvariable=passw,show='*').grid(row=1, column=6)


def login():
    recognized = False
    if(user_id.get() == 'Admin123') and (passw.get() == '12345'):
        i = 0
        while cap.isOpened() and i < 2:
            ret,img = cap.read()
                
            print('Processing')
            locations = face_recognition.face_locations(img,model=MODEL)
            img_enc = face_recognition.face_encodings(img,locations)
                
            img  = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
            for face_enc,face_loc in zip(img_enc,locations):
                results = face_recognition.compare_faces(known_encodings,face_enc,tolerance)
                match = None
                if True in results:
                    match = known_names[results.index(True)]
                    print("Match Found :",match)
                    recognized = True

                    top_left = (face_loc[3],face_loc[0])
                    bottom_right = (face_loc[1],face_loc[2])
                      
                    cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)

                    top_left = (face_loc[3],face_loc[2])
                    bottom_right = (face_loc[1],face_loc[2]+22)
                    cv2.rectangle(img,top_left,bottom_right,(0,255,0),cv2.FILLED)
                    cv2.putText(img,match,(face_loc[3]+10,face_loc[2]+15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                cv2.imshow('window',img)
            i += 1
            
            if recognized == True:
                Label(login_frame, text="Login  successfull !!!!!").grid(row=3, column=5,columnspan=2)
                disptable()
                root.destroy()
            
            if i==3:
                Label(login_frame, text="!!!!!! Action Denied !!!!!").grid(row=3, column=5,columnspan=2)
                
                root.destroy()
                root.destroy
    else:
        Label(login_frame,text='Access Denied. Invalid UserName/Password',fg='red').grid(row=4,column=5)

login_submit = Button(login_frame, text="Submit", bg="blue", fg="white", command=login).grid(row=2, column=5, columnspan=2, pady=18)

root.mainloop()