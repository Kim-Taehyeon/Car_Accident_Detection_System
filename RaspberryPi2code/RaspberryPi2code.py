#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from PIL import Image
import cv2
from time import sleep
import threading
import requests
import json
import RPi.GPIO as GPIO
import tkinter as tk
from math import *

## LED pin number and LED Set up
red_led = 24
green_led = 18
yellow_led = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)

a = 0       ## using for File number
b = 1       ## Clicked Button
ledc = 0    ## ledcontrol
path = ''   ## file location

## Nanonet Transmission function

def NanonetTrans(path):                        ## 'path' is file location
    url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/d38ea5b1-79d6-44c3-894f-0faf02ebd960/LabelUrls/'

    ## API Communication URL

    data = {'file': open(path, 'rb')}

    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('3w4fUst0f2mW89IUdpl5nmSQYbIF-X95kuFH-yDyH_h', ''),
                             files=data)

    print(response.text)                       ## Print Result of Nanonet
    Nanonets_save = json.loads(response.text)  ## response.text -> dictionary
    Nanonets_value = Nanonets_save['result'][0]['prediction']
    print(Nanonets_value)

    if len(Nanonets_value) == 0:               ## No Accident
        print(0)
        return 0

    else:                                      ## Accident
        car_accident_score = Nanonets_value[0]['score']     ## 'car_accident_score' is probability
        print(car_accident_score)
        return car_accident_score






##  Detection function

def detect_accident(path2):


    ##  Server thread create

    class ClientThread(threading.Thread):
        def __init__(self, num):
            super(ClientThread,self).__init__()
            #threading.Thread.__init__(self)
            self._stopper = threading.Event()
        def run(self):
            while True and not self.stopped:
                sleep(1)
        def stop(self):
            self._stopper.set()
        def stopped(self):
            return self._stopper.isSet()


    threads = []
    num = 0

    ## Detection Condition

    def DetectionCondi():
        global b
        global ledc

        if nano >= 0.7:
            print('사 고 감 지')

            if b == 1:
                cv2.namedWindow('image', cv2.WINDOW_NORMAL)
                c = cv2.imread(path)
                cv2.imshow('image', c)
                print('show')
                cv2.waitKey(1)
                print('finish')

                ##  If detction -> Red Light

                if ledc == 0:
                    GPIO.output(red_led, GPIO.HIGH)
                    GPIO.output(green_led, GPIO.LOW)
                    GPIO.output(yellow_led, GPIO.LOW)
                    print('red_led success')

        else:  ## If not detection -> No Light
            GPIO.output(red_led, GPIO.LOW)
            GPIO.output(green_led, GPIO.LOW)
            GPIO.output(yellow_led, GPIO.LOW)
            print('Peace')
        sleep(5)


    ## Detection_accident Main function

    while True:
        global path
        global b

        if num % 5:
            newthread = ClientThread(num)
            newthread.start()
            threads.append(newthread)

            if num is not 0:
                #threads[int(num/5)-1].stop()
                threads[int(num/5)-1].join()

        print ('detect_accident', path)     ## Detection + file location

        nano = nanonetslearn(path)          ## Transmission, return 0 or car_accident_score
        num += 1
        print(nano)

        Detectioncondi()

    for t in threads:
        t.join()


## Server thread Main function

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    global path     ## 'path' is file location
    global a        ## 'a' is file number
    if request.method == 'GET':
        return 'Hello GET'

    elif request.method == 'POST':
        if 'image' not in request.files:
            return 'no file'

        file = request.files['image']
        path = ('C:/pythonpic/image%d.png' % a)
        file.save(path)

        print(request.form['c1'])       ## 'c1' is Raspberry Pi1's location
        detal= request.form['c1']

        a = a + 1
        if a  == 5:                     ## after 5 reception Go Nanonet
            t = threading.Thread(target=detect_accident, args=(path,))
            t.daemon = True
            t.start()
        return 'upload image'



    #########################       Server End      #####################

    #########################       GUI Start          ##################



## Accident Yes

def acciyes():
    global b            ## Clicked Button
    global ledc         ## Control LED



    ##  Second GUI create
    toplevel = tk.Toplevel(window)
    toplevel.title('accident control')
    toplevel.geometry('400x100+100+100')

    # # 체크박스창 이미지제거
    # img2 = ''
    # s = tk.PhotoImage(file = img2)
    # label3 = tk.Label(toplevel, image = s, width = 760, height = 450)
    # label3.pack(side = 'left')

    # CheckBox function
    def select2():
        checkbutton2.select()
        checkbutton3.deselect()
        ledc=2
        GPIO.output(red_led, GPIO.LOW)
        GPIO.output(green_led, GPIO.LOW)
        GPIO.output(yellow_led, GPIO.HIGH)
        print('yellow_led success')

    def select3():
        checkbutton2.deselect()
        checkbutton3.select()
        ledc=3
        GPIO.output(red_led, GPIO.LOW)
        GPIO.output(green_led, GPIO.HIGH)
        GPIO.output(yellow_led, GPIO.LOW)
        print('green_led success')


    CheckVariety_2 = tk.IntVar()
    CheckVariety_3 = tk.IntVar()

    checkbutton2 = tk.Checkbutton(toplevel, text = '출동',
                                  variable = CheckVariety_2, command = select2)
    checkbutton3 = tk.Checkbutton(toplevel, text = '완료',
                                  variable = CheckVariety_3, command = select3)

    # CheckBox location

    checkbutton2.place(x = 0, y = 20)
    checkbutton3.place(x = 0, y = 40)

    toplevel.mainloop()


## Main Window create

window = tk.Tk()
window.title("Emergency Monitor - 인천광역시 연수구 송도동")
window.geometry('1200x800+100+100')

## GUI With Server
t = threading.Thread(target=app.run, args=('0.0.0.0',))
t.daemon = True
t.start()

## Yeonsu-gu map create

img = 'C:/projectmonitor/map1.png'
map = tk.PhotoImage(file = img)
label2 = tk.Label(window, image = map, width = 1101, height = 800)
label2.place(x = 320, y = 0)

## Red Button create

butimg = 'C:/projectmonitor/redicon.png'
butt = tk.PhotoImage(file = butimg)
button = tk.Button(window, overrelief = 'solid', command = acciyes,
                       image = butt)
button.place(x = 700, y = 400)

## Initialize Check Box create

def Initializef():
    checkbutton1.select()
    GPIO.output(red_led, GPIO.LOW)
    GPIO.output(green_led, GPIO.LOW)
    GPIO.output(yellow_led, GPIO.LOW)
    GPIO.cleanup()

CheckVariety_1 = tk.IntVar()

checkbutton1 = tk.Checkbutton(window, text='초기화',
                              variable=CheckVariety_1, command = Initializef)

checkbutton1.place(x = 0, y = 0)


window.mainloop()


