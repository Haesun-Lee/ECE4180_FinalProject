# Face Recognition Attendance Check Robot

**Team Members: Haesun Lee and Jueun Lee**

**Georgia Institute of Technology**

Watch our video presentation and demo:

Presentation (5min): https://youtu.be/BhbdnVkSK4Q

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


![block diagram](https://github.com/oscargao98/4180_Final_Project/blob/main/block_final.png)
Block diagram of our device.

## Parts List

Electronics:
* 1 Raspberry pi 4, Click [here](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X/ref=asc_df_B07TC2BK1X/?tag=&linkCode=df0&hvadid=380145854123&hvpos=&hvnetw=g&hvrand=1077202658962757536&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9010778&hvtargid=pla-818643320764&ref=&adgrpid=85982211068&th=1) to view the parts
* 2 DC Motors : ROB-13302, Click [here](https://www.digikey.com/en/products/detail/sparkfun-electronics/ROB-13302/5684382?utm_adgroup=Motors%20-%20AC%2C%20DC&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Motors%2C%20Solenoids%2C%20Driver%20Boards%2FModules_NEW&utm_term=&utm_content=Motors%20-%20AC%2C%20DC&gclid=Cj0KCQjw06OTBhC_ARIsAAU1yOVcqJy4c90pXfKolLJ4Rutqnd1u-5OmbhpIltpJvcxZlV09HCguXmYaAgrDEALw_wcB) to view the parts
* USB Web Cam, Click [here](https://www.amazon.com/Microphone-Streaming-Computer-Conferencing-Recording/dp/B087WT6L6B/ref=asc_df_B087WT6L6B/?tag=&linkCode=df0&hvadid=416694317409&hvpos=&hvnetw=g&hvrand=2414832459710564432&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9010778&hvtargid=pla-910393941550&ref=&adgrpid=94693386435&th=1) to view the parts
* 4 Push Button : 1825967-1, Click [here](https://www.te.com/usa-en/product-1825967-1.html?te_bu=Cor&te_type=srch&te_campaign=ggl_usa_cor-ggl-usa-srch-smbmktg-fy22-googlefeed_sma_sma-2210_2&elqCampaignId=115724&mkwid=RVA2RxlB%7Cpcrid%7C386964346949%7Cpkw%7C%7Cpmt%7C%7Cpdv%7Cc%7Cslid%7C%7Cproductid%7C1825967-1%7Cpgrid%7C78782457963%7Cptaid%7Cpla-825855726955%7C&utm_content=RVA2RxlB%7Cpcrid%7C386964346949%7Cpkw%7C%7Cpmt%7C%7Cpdv%7Cc%7Cslid%7C%7Cproductid%7C1825967-1%7Cpgrid%7C78782457963%7Cptaid%7Cpla-825855726955&gclid=Cj0KCQjw06OTBhC_ARIsAAU1yOWL_PZpx7OY7mFoOoDWu_ioH8U2DmBBL420hPBMHMKxV6d-SQ9NfEIaAmPPEALw_wcB) to view the parts
* Power Supply: HW-131, Click [here](https://www.cafago.com/en/p-e8575.html) to view the parts
* Resistors : 330ohm, Click [here](https://www.sparkfun.com/products/14490) to view the parts
* Jumper Wires(M/M and M/F) : Click [here](https://www.sparkfun.com/products/124) [here] (https://www.sparkfun.com/products/12794) to view the parts

Non-electronics:
* A desk
* A mini-shelf
* A water container
* A plant
* A curious mind

## Schematic and Connection Guide

#### Device Setup
Here's a few pictures of our fully assembled device.
![](https://github.com/oscargao98/4180_Final_Project/blob/main/ds1.png)
![](https://github.com/oscargao98/4180_Final_Project/blob/main/ds2.png)
![](https://github.com/oscargao98/4180_Final_Project/blob/main/ds3.png)
Two mbed LPC 1768 microcontrollers are used to control all the components. Servo 1 controls the pipe that allows water to flow through and water the flower.Servo 2 is attached to a cardboard, which functions as a shade. A water level sensor is taped onto the inner wall of a water container using waterproof tape. An ambient light sensor is placed facing the window to sense the sunlight level. A breadboard, consisting of an uLCD screen, six push buttons, and a speaker, is sticked onto the side of the self. 
#### Schematic
![](https://github.com/oscargao98/4180_Final_Project/blob/main/sch_new.png)

#### Connection Table for Uncommon Components
| Mbed1       |  Water Level | SEN-13322 | TEMT-6000 | NeoMatrix |HW-131|HS-442 #1| Mbed2 |
|-------------|--------------|-----------|-----------|-----------|------|---------|-------|
|             |              |           |           | +5V       | 5V   | red     |       |
| 3.3V = Vdd  |  +           | VCC       | VCC       |           |      |         |       |
| Gnd         |  -           | GND       | GND       | GND       | GND  | brown   |       |
| p5          |              |           |           | DIN       |      |         |       |
| p20         |  S           |           |           |           |      |         |       |
| p19         |              | SIG       |           |           |      |         |       |
| p18         |              |           | SIG       |           |      |         |       |
|             |              |           |           |           |      | yellow  |  p23  |

(Note: Use of external 5v power is REQUIRED, because we need enough current to drive servos and the LED array. Connect everything to a common ground.)

## Source Code
All source code is included in this repository. Run it by importing the repository into the MBed Cloud Compiler. Make sure to included all the libraries.

(Note: Make sure to import 1_garden for MBed1 and 2_garden for Mbed2, respectively.)

main.ccp for Mbed1

```cpp
#include "mbed.h"
#include "uLCD_4DGL.h"
#include "PinDetect.h"
#include "rtos.h"
#include "NeoMatrix.h"
#include "Speaker.h"
#define LED_COUNT 24 // uses a 24-led ring
#define YELLOW 0xFFFF00

enum Light_Mode{BRIGHT, NORMAL, SHADE};
const int offset = 3;

uLCD_4DGL uLCD(p9,p10,p11); // serial tx, serial rx, reset pin;
Serial pc(USBTX, USBRX); // tx, rx
Timeout countdown; // for alarm duration
Light_Mode mode = NORMAL;
Timeout snooze;

// pb
PinDetect button1(p12,PullUp);
PinDetect button2(p13,PullUp);
PinDetect button3(p14,PullUp);
PinDetect button4(p15,PullUp);
PinDetect button5(p16,PullUp);
PinDetect button6(p17,PullUp);

// sensors
AnalogIn waterSensor(p20);
AnalogIn moistureSensor(p19);
AnalogIn lightSensor(p18);

// outputs
Speaker speaker(p21);
PwmOut led(p25);
PwmOut led1(LED1);

// led panel
NeoArr array(p5, 1);

// global variables
Mutex myMut;
Mutex LED_mutex;
//volatile int button1_push = 0;
//volatile int button2_push = 0;
volatile float setWaterLevel = 0;
volatile float setMoistLevel = 0.0;
volatile float setLightLevelHigh = 0.5;
volatile float setLightLevelLow = 0.2;
int led_enable = 0;
//volatile float shadePosition = 0.0;

volatile float moisture_requirement = 0.6;
int x_light_low, x_light_high, x_moist;
// debug varibles

// sensor readings
volatile float water = 0.0;
volatile float light = 0.0;
volatile float moist = 0.0;

// callback functinos for 2 pushbuttons
void Button1_Callback (void){
    setLightLevelLow -= .1;
    setLightLevelLow = setLightLevelLow>0? setLightLevelLow:0;
    setLightLevelHigh = setLightLevelLow + 0.3;
}
void Button2_Callback (void){
    setLightLevelHigh += .1;
    setLightLevelHigh = setLightLevelHigh<1? setLightLevelHigh:1;
    setLightLevelLow = setLightLevelHigh - 0.3;
}

void Button3_Callback (void){
    // Increase moisture_requirement
    moisture_requirement += .1;
    moisture_requirement = (moisture_requirement < 0.9) ? moisture_requirement:0.9;
}

void Button4_Callback (void){
    // Decrease moisture_requirement
    moisture_requirement -= .1;
    moisture_requirement = (moisture_requirement > 0.1) ? moisture_requirement:0.1;
}

DigitalOut Shade(p23);
DigitalOut Pipe(p24);
void Button5_Callback (void){
    // Manually Water
    Pipe = 1;
}
void Button5_Callback2 (void){
    // Manually Water
    Pipe = 0;
}

int LED_enable = 1;
void Button6_Callback (void){
    // Turn off/on LED
    LED_enable = !LED_enable;
}

// move the servos
void motors_function(void const *argument){
    while(1){
        moist = moistureSensor.read();
        if (moist < moisture_requirement){
            Pipe = 1;
            Thread::wait(2000);
            Pipe = 0;
        }
        Thread::wait(10000);
    }    
}    

void light_function(void const *argument){
    while(1) {
        LED_mutex.lock();
        light = lightSensor.read();
        LED_mutex.unlock();
        if (light > setLightLevelHigh) {
            array.fillScreen(0,0,0,0);
            array.write();
            Shade = 1;    // Use the shade
        }
        else if (light<setLightLevelLow && LED_enable) {
            array.fillScreen(0,255,255,255);
            array.write();
            Shade = 0;     // Hide the shade
        }
        else {
            array.fillScreen(0,0,0,0);
            array.write();
            Shade = 0;     // Hide the shade
        }
        Thread::wait(2000);
    }
}

int main() {
    uLCD.printf("\n\rstart printing\n");
    uLCD.cls();
//    speaker.period(1.0/800.0);
    
    // led array init
    array.setBrightness(.2);    // set brightness to 0.1
    array.clear();

    // attach button callbacks
    button1.attach_deasserted(&Button1_Callback);
    button1.setSampleFrequency();
    button2.attach_deasserted(&Button2_Callback);
    button2.setSampleFrequency();
    button3.attach_deasserted(&Button3_Callback);
    button3.setSampleFrequency();
    button4.attach_deasserted(&Button4_Callback);
    button4.setSampleFrequency();
    button5.attach_deasserted(&Button5_Callback);
    button5.attach_asserted(&Button5_Callback2);
    button5.setSampleFrequency();
    button6.attach_deasserted(&Button6_Callback);
    button6.setSampleFrequency();

    // attach threads
    Thread motors(motors_function);
    Thread light_thread(light_function);
    
    int alert = 1;

    while(1) {
        water = waterSensor.read();
        moist = moistureSensor.read();
        LED_mutex.lock();
        light = lightSensor.read();
        LED_mutex.unlock();
        myMut.lock();

        // Draw a bar to display light level
        uLCD.locate(0,1);
        uLCD.printf("LIGHT: %f\n",light);
        uLCD.rectangle(15, 15+offset, 112, 32+offset, WHITE);
        uLCD.filled_rectangle(16, 16+offset, 111, 31+offset, BLACK);
        if (light > 0.9)
            uLCD.filled_rectangle(16, 16+offset, 16 + floor((light/1.0f) * 96), 31+offset, RED);
        else if (light > setLightLevelHigh)
            uLCD.filled_rectangle(16, 16+offset, 16 + floor((light/1.0f) * 96), 31+offset, YELLOW);
        else if (light < setLightLevelLow)
            uLCD.filled_rectangle(16, 16+offset, 16 + floor((light/1.0f) * 96), 31+offset, YELLOW);
        else
            uLCD.filled_rectangle(16, 16+offset, 16 + floor((light/1.0f) * 96), 31+offset, GREEN);
        x_light_low = 16 + floor((setLightLevelLow/1.0f) * 96);
        x_light_high = 16 + floor((setLightLevelHigh/1.0f) * 96);
        uLCD.line(x_light_low, 16+offset, x_light_low, 31+offset, WHITE);
        uLCD.line(x_light_high, 16+offset, x_light_high, 31+offset, WHITE);
        
        // Draw a bar to display moisture level  
        uLCD.locate(0,5);
        uLCD.printf("MOISTURE: %f\n", moist);
        uLCD.rectangle(15, 47+offset, 112, 64+offset, WHITE);
        uLCD.filled_rectangle(16, 48+offset, 111, 63+offset, BLACK);
        if (moist > moisture_requirement)
            uLCD.filled_rectangle(16, 48+offset, 16 + floor((moist/1.0f) * 96), 63+offset, GREEN);
        else if (moist < 0.2)
            uLCD.filled_rectangle(16, 48+offset, 16 + floor((moist/1.0f) * 96), 63+offset, RED);
        else
            uLCD.filled_rectangle(16, 48+offset, 16 + floor((moist/1.0f) * 96), 63+offset, YELLOW);
        x_moist = 16 + floor((moisture_requirement/1.0f) * 96);
        uLCD.line(x_moist, 48+offset, x_moist, 63+offset, WHITE);
        
        // Draw a bar to display water level
        uLCD.locate(0,9);
        uLCD.printf("WATER: %f\n", water);
        uLCD.rectangle(15, 79+offset, 112, 96+offset, WHITE);
        uLCD.filled_rectangle(16, 80+offset, 111, 95+offset, BLACK);
        if (water > 0.4)
            uLCD.filled_rectangle(16, 80+offset, 16 + floor((water/1.0f) * 96), 95+offset, GREEN);
        else if (water > 0.2)
            uLCD.filled_rectangle(16, 80+offset, 16 + floor((water/1.0f) * 96), 95+offset, YELLOW);
        else
            uLCD.filled_rectangle(16, 80+offset, 16 + floor((water/1.0f) * 96), 95+offset, RED);
        myMut.unlock();
        if (water<.2&&alert){
             led = 1;
             speaker.PlayNote(969.0, 2, 0.5);
             alert = 0;
        } else if (water<.2){led = !led;}
        Thread::wait(100); // every .1 second
    }
}
```

main.cpp for Mbed2

```cpp
#include "mbed.h"
#include "Servo.h"

Servo Pipe(p24);
Servo Shade(p23);
PwmOut led1(LED1);
PwmOut led2(LED2);
Serial pc(USBTX, USBRX); // tx, rx
DigitalIn Shade_sig(p21);
DigitalIn Pipe_sig(p22);


int main(){
    wait(1);
    while(1){
        if (Shade_sig) {
            Shade = 0.2;
        }
        else {
            Shade = 1.0;
        }
            
        if (Pipe_sig) {
            Pipe = 0.9;
        }
        else {
            Pipe = 0.2;
        }
        wait(1);
    }
    
}
```



