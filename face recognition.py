from turtle import width
import face_recognition
import sqlite3
import cv2
import os
from tkinter import *
# from google.colab.patches import cv2_imshow

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
    if(user_id.get() == 'Admin123') and (passw.get() == '12345'):
        if recognized == True:
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
          torelance = 0.1
          MODEL = 'cnn'

          for file in os.listdir(known_dir):
            img  = read_img(known_dir + '/' + file)
            img_enc = face_recognition.face_encodings(img)[0]
            known_encodings.append(img_enc)
            known_names.append(file.split('.')[0])

          cap = cv2.VideoCapture(0)

          while cap.isOpened():
              ret,img = cap.read()

              print('Processing')
              locations = face_recognition.face_locations(img,model=MODEL)
              img_enc = face_recognition.face_encodings(img,locations)
              
              img  = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
              for face_enc,face_loc in zip(img_enc,locations):
                  results = face_recognition.compare_faces(known_encodings,face_enc)
                  match = None
                  if True in results:
                      match = known_names[results.index(True)]
                      print("Match Found :",match)
                      
                      top_left = (face_loc[3],face_loc[0])
                      bottom_right = (face_loc[1],face_loc[2])
                      
                      cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)

                      top_left = (face_loc[3],face_loc[2])
                      bottom_right = (face_loc[1],face_loc[2]+22)
                      cv2.rectangle(img,top_left,bottom_right,(0,255,0),cv2.FILLED)
                      cv2.putText(img,match,(face_loc[3]+10,face_loc[2]+15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
              img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
              cv2.imshow('window',img)
              # cv2.waitKey(10000)
              
              if cv2.waitKey(1) & 0xFF == ord('q'):
                  break
          cap.release()
          cv2.destroyAllWindows()
                      
        Label(login_frame, text="Login  successfull !!!!!").grid(row=3, column=5,columnspan=2)

login_submit = Button(login_frame, text="Submit", bg="blue", fg="white", command=login).grid(row=2, column=5, columnspan=2, pady=18)

conn = sqlite3.connect("database.db")
cur = conn.cursor()
# cur.execute("CREATE TABLE Employees2108(empid text,first_name text,last_name text,email text,phoneno integer)")
# conn.commit()
# cur.execute("INSERT INTO EMPLOYEES2108 VALUES ('102','Sughosh','Rathod','101@gmail.com',1011011011)")
# conn.commit()
cur.execute("select * from employees2108;")
output = cur.fetchall()
print(output)
# cur.execute("delete from employees2108 where empid='101'")
conn.commit()

# unknown_dir = 'unknown'
# for file in os.listdir(unknown_dir):
#   print('PRocessing',file)
#   img = read_img(unknown_dir+'/'+file)
#   img_enc = face_recognition.face_encodings(img)[0]

#   results = face_recognition.compare_faces(known_encodings,img_enc)

#   # print(face_recognition.face_distance(known_encodings,img_enc))

#   for i in range(len(results)):
#     if results[i] == True:
#       name = known_names[i]
#       (top,right,bottom,left) = face_recognition.face_locations(img)[0]
#       cv2.rectangle(img,(left,top-20),(right,bottom),(0,255,0),2)
#       cv2.putText(img,name,(left,bottom+20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),2)
#       cv2.imshow('feed',img)
  
  # if True in results:
  #   continue
  # else:
  #   (top,right,bottom,left) = face_recognition.face_locations(img)[0]
  #   cv2.rectangle(img,(left,top-20),(right,bottom),(0,255,0),2)
  #   cv2.putText(img,'unknown',(left,bottom+20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),2)
  #   cv2_imshow(img)

# unknown_dir = 'unknown'
# for file in os.listdir(unknown_dir):
#     print('PRocessing',file)
#     img = read_img(unknown_dir+'/'+file)
#     locations = face_recognition.face_locations(img,model=MODEL)
#     img_enc = face_recognition.face_encodings(img,locations)
    
#     img  = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
#     for face_enc,face_loc in zip(img_enc,locations):
#         results = face_recognition.compare_faces(known_encodings,face_enc)
#         match = None
#         if True in results:
#             match = known_names[results.index(True)]
#             print("Match Found :",match)
            
#             top_left = (face_loc[3],face_loc[0])
#             bottom_right = (face_loc[1],face_loc[2])
            
#             cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)

#             top_left = (face_loc[3],face_loc[2])
#             bottom_right = (face_loc[1],face_loc[2]+22)
#             cv2.rectangle(img,top_left,bottom_right,(0,255,0),cv2.FILLED)
#             cv2.putText(img,match,(face_loc[3]+10,face_loc[2]+15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
#     img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#     cv2.imshow(file,img)
#     cv2.waitKey(0)
# cv2.destroyAllWindows(file)

  # print(face_recognition.face_distance(known_encodings,img_enc))

#   for i in range(len(results)):
#     if results[i] == True:
#       name = known_names[i]
#       (top,right,bottom,left) = face_recognition.face_locations(img)[0]
#       cv2.rectangle(img,(left,top-20),(right,bottom),(0,255,0),2)
#       cv2.putText(img,name,(left,bottom+20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),2)
#       cv2.imshow('feed',img)
  
#   if True in results:
#     continue
#   else:
#     (top,right,bottom,left) = face_recognition.face_locations(img)[0]
#     cv2.rectangle(img,(left,top-20),(right,bottom),(0,255,0),2)
#     cv2.putText(img,'unknown',(left,bottom+20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),2)
#     cv2_imshow(img)
  
# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     ret,img = cap.read()

#     print('PRocessing')
#     locations = face_recognition.face_locations(img,model=MODEL)
#     img_enc = face_recognition.face_encodings(img,locations)
    
#     img  = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
#     for face_enc,face_loc in zip(img_enc,locations):
#         results = face_recognition.compare_faces(known_encodings,face_enc)
#         match = None
#         if True in results:
#             match = known_names[results.index(True)]
#             print("Match Found :",match)
            
#             top_left = (face_loc[3],face_loc[0])
#             bottom_right = (face_loc[1],face_loc[2])
            
#             cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)

#             top_left = (face_loc[3],face_loc[2])
#             bottom_right = (face_loc[1],face_loc[2]+22)
#             cv2.rectangle(img,top_left,bottom_right,(0,255,0),cv2.FILLED)
#             cv2.putText(img,match,(face_loc[3]+10,face_loc[2]+15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
#     img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#     cv2.imshow('window',img)
#     # cv2.waitKey(10000)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

  # print(results)

root.mainloop()