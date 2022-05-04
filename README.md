# Face Recognition Attendance Check Robot

**Team Members: Haesun Lee and Jueun Lee**

**Georgia Institute of Technology**

Watch our video presentation and demo:

Presentation Video (5min):

Presentation Slide : https://docs.google.com/presentation/d/1dY4bCMGJTAA4-nHcASC5jcGp0Mmf3YF5dnUtclSm6NY/edit?usp=sharing

Demonstration (2min): https://youtu.be/0pqdkLO-uRU


![Robot Picture](/Car_front.jpeg)


## Table of Content
* [Project Idea](#project-idea)
* [Software Flow chart](#software-flow-chart)
* [Parts List](#parts-list)
* [Schematic and Connection Guide](#schematic-and-connection-guide)
* [Source Code](#source-code)
* [Future Direction](#future-direction)
* [Authors](#authors)
* [Version](#version)

## Project Idea
Attending in class helps students to fully understand the content. If we miss the class, it is hard to catch up what is covered in class. And if this kind of situation happens repeatly, student might be fail the class. But it is hard for both professor and students to do the attendance check manually. And there is chance to do the fake attendance check. 

Our idea for the ECE-4180(Spring 2022)'s final project is to build a Attendance check robot. The professor will first set the password for its day, and let student know the password. Once the password is set properly, the robot will turn on its camera and recognize the student's face according to the collected data previously. Student will then press the white button to enter the password. If the student entered the correct password given by the professor, the green RGB light will turned on, and student's name data will be updated to the attendace xls sheet. If the student fails to enter the correct password, the red RGB light will be turned on, and student's name will not be updated in attendance xls sheet. After entering the password, the robot will move approximately 12 inchs so that next student will be able to do the attendance check. After the certain collection time(demo will be 2 mins) has passed, our robot will automatically send the attendance sheet through the professor’s email in xls format. 

## Software Flow chart
This is our software flow chart of our robot.
![](/Flowchart.png)

## Parts List

#### Electronics:
* 1 Raspberry pi 4, Click [here](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X/ref=asc_df_B07TC2BK1X/?tag=&linkCode=df0&hvadid=380145854123&hvpos=&hvnetw=g&hvrand=1077202658962757536&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9010778&hvtargid=pla-818643320764&ref=&adgrpid=85982211068&th=1) to view the parts
* 2 DC Motors : ROB-13302, Click [here](https://www.digikey.com/en/products/detail/sparkfun-electronics/ROB-13302/5684382?utm_adgroup=Motors%20-%20AC%2C%20DC&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Motors%2C%20Solenoids%2C%20Driver%20Boards%2FModules_NEW&utm_term=&utm_content=Motors%20-%20AC%2C%20DC&gclid=Cj0KCQjw06OTBhC_ARIsAAU1yOVcqJy4c90pXfKolLJ4Rutqnd1u-5OmbhpIltpJvcxZlV09HCguXmYaAgrDEALw_wcB) to view the parts
* USB Web Cam, Click [here](https://www.amazon.com/Microphone-Streaming-Computer-Conferencing-Recording/dp/B087WT6L6B/ref=asc_df_B087WT6L6B/?tag=&linkCode=df0&hvadid=416694317409&hvpos=&hvnetw=g&hvrand=2414832459710564432&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9010778&hvtargid=pla-910393941550&ref=&adgrpid=94693386435&th=1) to view the parts
* 4 Push Button : 1825967-1, Click [here](https://www.te.com/usa-en/product-1825967-1.html?te_bu=Cor&te_type=srch&te_campaign=ggl_usa_cor-ggl-usa-srch-smbmktg-fy22-googlefeed_sma_sma-2210_2&elqCampaignId=115724&mkwid=RVA2RxlB%7Cpcrid%7C386964346949%7Cpkw%7C%7Cpmt%7C%7Cpdv%7Cc%7Cslid%7C%7Cproductid%7C1825967-1%7Cpgrid%7C78782457963%7Cptaid%7Cpla-825855726955%7C&utm_content=RVA2RxlB%7Cpcrid%7C386964346949%7Cpkw%7C%7Cpmt%7C%7Cpdv%7Cc%7Cslid%7C%7Cproductid%7C1825967-1%7Cpgrid%7C78782457963%7Cptaid%7Cpla-825855726955&gclid=Cj0KCQjw06OTBhC_ARIsAAU1yOWL_PZpx7OY7mFoOoDWu_ioH8U2DmBBL420hPBMHMKxV6d-SQ9NfEIaAmPPEALw_wcB) to view the parts
* Dual H Bridge Motor Speed Controller : L298, Click [here](https://www.amazon.com/Qunqi-Controller-Module-Stepper-Arduino/dp/B014KMHSW6/ref=asc_df_B014KMHSW6/?tag=hyprod-20&linkCode=df0&hvadid=167139094796&hvpos=&hvnetw=g&hvrand=11158928515254836671&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9010778&hvtargid=pla-306436938191&psc=1) to view the parts
* RGB LED : NTE30159, Click [here](https://www.digikey.com/en/products/detail/nte-electronics,-inc/NTE30159/11646909?utm_adgroup=LED%20Indication%20-%20Discrete&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Optoelectronics_NEW&utm_term=&utm_content=LED%20Indication%20-%20Discrete&gclid=Cj0KCQjw06OTBhC_ARIsAAU1yOWaY7CehT0WcODW6JuO_wdBfqbyAnw7uwhoDNt-fKgAvCb0sfBnuMIaAkY0EALw_wcB) to view the parts
* Power Supply : HW-131, Click [here](https://www.cafago.com/en/p-e8575.html) to view the parts
* Resistors : 330ohm, Click [here](https://www.sparkfun.com/products/14490) to view the parts
* Jumper Wires(M/M and M/F) : Click [here](https://www.sparkfun.com/products/124) [here](https://www.sparkfun.com/products/12794) to view the parts


#### Non-electronics:
* A desk
* Students
* Professor
* A curious mind

## Block Diagram
This is our block diagram of our robot
![diagram](https://user-images.githubusercontent.com/78533448/166670569-dde1be02-0111-4150-ba7b-ccee6c5cd6e9.jpg)

## Schematic and Connection Guide
Here's a few pictures of our fully assembled device.
![](/Car_side_cross.jpeg)
![](/Car_side.jpeg)

#### Schematic
![schematic](https://user-images.githubusercontent.com/78533448/166670311-8cd390a1-4448-4bbd-89e3-76e2feed1486.png)

#### Connection Table for Uncommon Components
| Raspberry pi | L293 Motor Driver | DC Motors | Push Buttons | RGB LED | USB Cam | Power Supply |
|--------------|-------------------|-----------|--------------|---------|---------|--------------|
|     3V       |                   |           |              |         |         |              |
|     5V       |       Vin         |           |              |         |         |     5V       |
|     GND      |       GND         |           |     GND      |   GND   |         |     GND      |
|              |       OUT1        |     +     |              |         |         |              |
|              |       OUT2        |     -     |              |         |         |              |
|              |       OUT3        |     +     |              |         |         |              |
|              |       OUT4        |     -     |              |         |         |              |
|    GPIO17    |       IN1         |           |              |         |         |              |
|    GPIO22    |       IN2         |           |              |         |         |              |
|    GPIO23    |       IN3         |           |              |         |         |              |
|    GPIO24    |       IN4         |           |              |         |         |              |
|    GPIO11    |       ENA1        |           |              |         |         |              |
|              |       ENA2        |           |              |         |         |              |
|    GPIO5     |                   |           |     1 (+)    |         |         |              |
|    GPIO6     |                   |           |     2 (+)    |         |         |              |
|    GPIO26    |                   |           |     3 (+)    |         |         |              |
|    GPIO25    |                   |           |   ENTER (+)  |         |         |              |
|    GPIO14    |                   |           |    CAPTURE   |         |         |              |
|    GPIO12    |                   |           |              |   RED   |         |              |
|    GPIO19    |                   |           |              |  GREEN  |         |              |
|    GPIO8     |                   |           |              |  BLUE   |         |              |


(Note: Use of external 5v power is REQUIRED, because we need enough current to drive servos.

## How to Run 
First, we need to install OpenCv and Numpy for the face recognition.
* Installation Guide for [OpenCV and Numpy](https://singleboardbytes.com/647/install-opencv-raspberry-pi-4.htm)

After installing all the libraries, we need to get the student's face data by running : 
<pre><code>python3 Face_Data_collect.py</code></pre>

Next, we need to train our robot with the data that we have collected bu running :
<pre><code>python3 Face_Recognition.py</code></pre>

Finally, our robot is ready to recognize student face. Try running :
<pre><code>python3 Face_Recognition.py</code></pre>

## Source Code

Code to move our robot forward :
~~~py
def forward(sec):
    GPIO.output(17, False)
    GPIO.output(22, True)
    GPIO.output(23, False)
    GPIO.output(24, True)
    time.sleep(sec)
    #GPIO.cleanup()
~~~

Code for professor to set the password :
~~~py
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
~~~

Code to check if student enters the correct password :
~~~py
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
~~~

Code for face recognition & updating student's name in attendance sheet :
~~~py
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
~~~

Code for sending attendance sheet to professor's email :
~~~py
fromaddr = "myemailaddress@gmail.com"
toaddr = "professoremailaddress@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Today's attendance"

body = "Today's attendance"

msg.attach(MIMEText(body, 'plain'))

now = datetime.today().strftime('%Y-%m-%d')
now = now +'.xls'

filename = now
path = '/home/heyjueun/opencv-3.3.0/data/haarcascades/'
path = path + now
attachment = open(path, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(fromaddr, "password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
~~~

## Future Direction
We thought it will be good to have a screen so that student is able to see if his/her face is being recognized, so we will be adding the raspberry pi touch display pad. Also, instead of sending the attendance sheet to the professor, it might be more efficient if we have the database for the student's attendance.

## Authors
* Haesun Lee
* Jueun Lee

## Version
* 1.0 V


