import cv2
import sys
import pyttsx
import speech
import time

face_cascade = cv2.CascadeClassifier('E:\\OpenCv_new\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('E:\\OpenCv_new\\opencv\\sources\\data\\haarcascades\\haarcascade_eye.xml')
count=0
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    time.sleep(10)
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Resize Image 
    minisize = (frame.shape[1],frame.shape[0])
    miniframe = cv2.resize(frame, minisize)
    
    # Store detected frames in variable name faces
    faces =  face_cascade.detectMultiScale(miniframe)

    for f in faces:
        x, y, w, h = [ v for v in f ]
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,255))
        #Save just the rectangle faces in SubRecFaces
        sub_face = frame[y:y+h, x:x+w]
        if len(faces) == 1:
                FaceFileName = "G:\\Python27\\faces\\gos\\img" + str(count) + ".jpg"
                count=count+1
                cv2.imwrite(FaceFileName, sub_face)
        #Display the image 
        cv2.imshow('Result',frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if count==1:
        speech.say("Image stored in database.")
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
