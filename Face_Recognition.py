import cv2
import numpy as np
import os
import time
import RPi.GPIO as GPIO
import xlwt
from xlwt import Workbook
from datetime import datetime

from time import sleep

GPIO.setwarnings(False)
os.chdir("/home/heyjueun/opencv-3.3.0/data/haarcascades")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/heyjueun/Desktop/Face-Recognition-using-Raspberry-Pi/trainer/trainer.yml')
cascadePath = "/home/heyjueun/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

timeout = time.time() + 60*1 # 1min
LED_PIN = 14

BUTTON_PIN1 = 5
BUTTON_PIN2 = 6
BUTTON_PIN3 = 26
BUTTON_PIN4 = 25 #enter

redPin = 12
greenPin = 19
bluePin = 8

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)

GPIO.setup(BUTTON_PIN1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


def initialize(sec):
    GPIO.output(17, False)
    GPIO.output(22, False)
    GPIO.output(23, False)
    GPIO.output(24, False)
    time.sleep(sec)
    #GPIO.cleanup()

def right_turn(sec):
    GPIO.output(17, False)
    GPIO.output(22, True)
    GPIO.output(23, True)
    GPIO.output(24, False)
    time.sleep(sec)
    #GPIO.cleanup()
    
def left_turn(sec):
    GPIO.output(17, True)
    GPIO.output(22, False)
    GPIO.output(23, False)
    GPIO.output(24, True)
    time.sleep(sec)
    #gpio.cleanup()
    
def reverse(sec):
    GPIO.output(17, True)
    GPIO.output(22, False)
    GPIO.output(23, True)
    GPIO.output(24, False)
    time.sleep(sec)
    #GPIO.cleanup()
    
def forward(sec):
    GPIO.output(17, False)
    GPIO.output(22, True)
    GPIO.output(23, False)
    GPIO.output(24, True)
    time.sleep(sec)
    #GPIO.cleanup()

def turnOff():
    #GPIO.setmode(GPIO.BCM)
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)

def red():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)

def green():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.LOW)
    
def blue():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.HIGH)

def white():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.HIGH)

def setPassword(Password_Setting, Password):
    while Password_Setting:
        blue()
        button1 = GPIO.input(BUTTON_PIN1)
        button2 = GPIO.input(BUTTON_PIN2)
        button3 = GPIO.input(BUTTON_PIN3)
        button4 = GPIO.input(BUTTON_PIN4)
        if button1 == False:
            print('button 1 pressed')
            Password += '1'
            time.sleep(0.2)
            
        if button2 == False:
            print('button 2 pressed')
            Password += '2'
            time.sleep(0.2)
            
        if button3 == False:
            print('button 3 pressed')
            Password += '3'
            time.sleep(0.2)
            
        if button4 == False:
            print('ENTER pressed')
            print('Your password is set to : ' , Password)
            Password_Setting = False
            white()
            time.sleep(0.5)
            turnOff()
            time.sleep(0.5)
            white()
            time.sleep(0.5)
            turnOff()
            time.sleep(0.5)
            
            
    return Password

def password(Password_Checking, checkPW, Password) :
    while Password_Checking:
        button1 = GPIO.input(BUTTON_PIN1)
        button2 = GPIO.input(BUTTON_PIN2)
        button3 = GPIO.input(BUTTON_PIN3)
        button4 = GPIO.input(BUTTON_PIN4)
        if button1 == False:
            print('button 1 pressed')
            checkPW += '1'
            time.sleep(0.2)
            
        if button2 == False:
            print('button 2 pressed')
            checkPW += '2'
            time.sleep(0.2)
            
        if button3 == False:
            print('button 3 pressed')
            checkPW += '3'
            time.sleep(0.2)
            
        if button4 == False:
            print('ENTER pressed')
            Password_Checking = False
            print("Password you entered : ", checkPW)
            print(checkPW)
            print(Password)
            if checkPW == Password :
                green()
                print("attendance checked!")
                checkPW = ''
                sleep(2)
                turnOff()
                reverse(1)
                initialize(2)
                return True
            else:
                print("Failed to check attendance")
                red()
                checkPW = ''
                sleep(2)
                turnOff()
                reverse(1)
                initialize(2)
                return False
            time.sleep(0.2)

def faceRecognition(Password_Checking, checkPW, Password):
    now = datetime.today().strftime('%Y-%m-%d')
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')

    col = 2
    sheet1.write(0, 0, 'Attendance')

    #iniciate id counter
    id = 0

    # names related to ids: example ==> KUNAL: id=1,  etc
    names = ['None', 'Haesun', 'Jueun', 'Haesun', 'Jueun', 'W']

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while Password_Checking:
        if  time.time() > timeout:
            break
        
        input_state = GPIO.input(LED_PIN)
        if input_state == False:
            print('Captured')
            print(id)
            if password(Password_Checking, checkPW, Password):          
                sheet1.write(col, 0, id)
                col += 1
                time.sleep(0.2)
            
        
        ret, img =cam.read()
        #img = cv2.flip(img, -1) # Flip vertically
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )

        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)

        cv2.imshow('camera',img)

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break

    # Do a bit of cleanup
    print("\n Exiting Program")
    now = now+'.xls'
    wb.save(now)
    cam.release()
    cv2.destroyAllWindows()
    os.system('python3 test_email.py ')
    
if __name__ == "__main__":
    initialize(2)
    turnOff()
    checkPW = ''
    Password = ''
    Password_Checking = True
    Password_Setting = True
    GPIO.setmode(GPIO.BCM)

    Password = setPassword(Password_Setting, Password)
    turnOff()
    faceRecognition(Password_Checking, checkPW, Password)
