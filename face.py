
from turtle import width
import face_recognition
import sqlite3
import cv2
import os

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

unknown_dir = 'unknown'
for file in os.listdir(unknown_dir):
    print('PRocessing',file)
    img = read_img(unknown_dir+'/'+file)
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
    cv2.imshow(file,img)
    cv2.waitKey(0)
cv2.destroyAllWindows(file)