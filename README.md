# Face Recognition Attendance Check Robot

**Team Members: Haesun Lee and Jueun Lee**

**Georgia Institute of Technology**

Watch our video presentation and demo:

Presentation (5min): 

Demonstration (2min): https://youtu.be/0pqdkLO-uRU


![Robot Picture](/Car_front.jpeg)


## Table of Content
* [Project Idea](#project-idea)
* [Parts List](#parts-list)
* [Schematic and Connection Guide](#schematic-and-connection-guide)
* [Source Code](#source-code)
* [Future Direction](#future-direction)

## Project Idea
Attending in class helps students to fully understand the content. If we miss the class, it is hard to catch up what is covered in class. And if this kind of situation happens repeatly, student might be fail the class. But it is hard for both professor and students to do the attendance check manually. And there is chance to do the fake attendance check. 

Our idea for the ECE-4180(Spring 2022)'s final project is to build a Attendance check robot. The professor will first set the password for its day, and let student know the password. Once the password is set properly, the robot will turn on its camera and recognize the student's face according to the collected data previously. Student will then press the white button to enter the password. If the student entered the correct password given by the professor, the green RGB light will turned on, and student's name data will be updated to the attendace xls sheet. If the student fails to enter the correct password, the red RGB light will be turned on, and student's name will not be updated in attendance xls sheet. After entering the password, the robot will move approximately 12 inchs so that next student will be able to do the attendance check. After the certain collection time(demo will be 2 mins) has passed, our robot will automatically send the attendance sheet through the professor’s email in xls format. 


![](/Flowchart.png)
Flow chart of our robot.

## Parts List

Electronics:
* 1 Raspberry pi 4, Click [here](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X/ref=asc_df_B07TC2BK1X/?tag=&linkCode=df0&hvadid=380145854123&hvpos=&hvnetw=g&hvrand=1077202658962757536&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9010778&hvtargid=pla-818643320764&ref=&adgrpid=85982211068&th=1) to view the parts
* 2 DC Motors : ROB-13302, Click [here](https://www.digikey.com/en/products/detail/sparkfun-electronics/ROB-13302/5684382?utm_adgroup=Motors%20-%20AC%2C%20DC&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Motors%2C%20Solenoids%2C%20Driver%20Boards%2FModules_NEW&utm_term=&utm_content=Motors%20-%20AC%2C%20DC&gclid=Cj0KCQjw06OTBhC_ARIsAAU1yOVcqJy4c90pXfKolLJ4Rutqnd1u-5OmbhpIltpJvcxZlV09HCguXmYaAgrDEALw_wcB) to view the parts
* USB Web Cam, Click [here](https://www.amazon.com/Microphone-Streaming-Computer-Conferencing-Recording/dp/B087WT6L6B/ref=asc_df_B087WT6L6B/?tag=&linkCode=df0&hvadid=416694317409&hvpos=&hvnetw=g&hvrand=2414832459710564432&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9010778&hvtargid=pla-910393941550&ref=&adgrpid=94693386435&th=1) to view the parts
* 4 Push Button : 1825967-1, Click [here](https://www.te.com/usa-en/product-1825967-1.html?te_bu=Cor&te_type=srch&te_campaign=ggl_usa_cor-ggl-usa-srch-smbmktg-fy22-googlefeed_sma_sma-2210_2&elqCampaignId=115724&mkwid=RVA2RxlB%7Cpcrid%7C386964346949%7Cpkw%7C%7Cpmt%7C%7Cpdv%7Cc%7Cslid%7C%7Cproductid%7C1825967-1%7Cpgrid%7C78782457963%7Cptaid%7Cpla-825855726955%7C&utm_content=RVA2RxlB%7Cpcrid%7C386964346949%7Cpkw%7C%7Cpmt%7C%7Cpdv%7Cc%7Cslid%7C%7Cproductid%7C1825967-1%7Cpgrid%7C78782457963%7Cptaid%7Cpla-825855726955&gclid=Cj0KCQjw06OTBhC_ARIsAAU1yOWL_PZpx7OY7mFoOoDWu_ioH8U2DmBBL420hPBMHMKxV6d-SQ9NfEIaAmPPEALw_wcB) to view the parts
* Dual H Bridge Motor Speed Controller : L298, Click [here](https://www.amazon.com/Qunqi-Controller-Module-Stepper-Arduino/dp/B014KMHSW6/ref=asc_df_B014KMHSW6/?tag=hyprod-20&linkCode=df0&hvadid=167139094796&hvpos=&hvnetw=g&hvrand=11158928515254836671&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9010778&hvtargid=pla-306436938191&psc=1) to view the parts
* RGB LED : NTE30159, Click [here](https://www.digikey.com/en/products/detail/nte-electronics,-inc/NTE30159/11646909?utm_adgroup=LED%20Indication%20-%20Discrete&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Optoelectronics_NEW&utm_term=&utm_content=LED%20Indication%20-%20Discrete&gclid=Cj0KCQjw06OTBhC_ARIsAAU1yOWaY7CehT0WcODW6JuO_wdBfqbyAnw7uwhoDNt-fKgAvCb0sfBnuMIaAkY0EALw_wcB) to view the parts
* Power Supply : HW-131, Click [here](https://www.cafago.com/en/p-e8575.html) to view the parts
* Resistors : 330ohm, Click [here](https://www.sparkfun.com/products/14490) to view the parts
* Jumper Wires(M/M and M/F) : Click [here](https://www.sparkfun.com/products/124) [here](https://www.sparkfun.com/products/12794) to view the parts


Non-electronics:
* A desk
* Students
* Professor
* A curious mind

## Schematic and Connection Guide

#### Device Setup
Here's a few pictures of our fully assembled device.
![](/Car_side_cross.jpeg)
![](/Car_side.jpeg)

The main software tools that we are going to use for our final project are OpenCV (an open-source computer vision package) to first collect the student’s face data and recognize the student face by training the data. 


#### Schematic


#### Connection Table for Uncommon Components
| Raspberry pi | L293 Motor Driver | DC Motors | Push Buttons | RGB LED | USB Cam | Power Supply |
|--------------|-------------------|-----------|--------------|---------|---------|--------------|
|              |                   |           |              |         |         |              |
|              |                   |           |              |         |         |              |
|              |                   |           |              |         |         |              |
|              |                   |           |              |         |         |              |
|              |                   |           |              |         |         |              |
|              |                   |           |              |         |         |              |
|              |                   |           |              |         |         |              |
|              |                   |           |              |         |         |              |
|              |                   |           |              |         |         |              |
|              |                   |           |              |         |         |              |
|              |                   |           |              |         |         |              |
|              |                   |           |              |         |         |              |
|              |                   |           |              |         |         |              |
|              |                   |           |              |         |         |              |
|              |                   |           |              |         |         |              |
|              |                   |           |              |         |         |              |

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

## Future Direction



