import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setwarnings(False)


BUTTON_PIN1 = 5
BUTTON_PIN2 = 6
BUTTON_PIN3 = 26
BUTTON_PIN4 = 25 #enter

redPin = 12
greenPin = 19
bluePin = 8
#set pins as outputs
GPIO.setmode(GPIO.BCM)

GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)

GPIO.setup(BUTTON_PIN1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def turnOff():
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
            else:
                print("Failed to check attendance")
                red()
                checkPW = ''
                sleep(2)
                turnOff()
            time.sleep(0.2)
            
            
if __name__ == "__main__":
    turnOff()
    checkPW = ''
    Password = ''
    Password_Checking = True
    Password_Setting = True
    
    Password = setPassword(Password_Setting, Password)
    turnOff()
    while True:
        password(Password_Checking, checkPW, Password)
