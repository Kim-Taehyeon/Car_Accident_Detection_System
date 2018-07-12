# -*- coding: utf-8 -*-


## Raspberry Pi 1 code
## - Frame Capture, RPi2 transmission

import os
import cv2
import RPi.GPIO as GP
from time import sleep
import requests


## Function of transmission to Raspberry Pi 2
## < same Internet connection >

def Transmission(count):                            ## 'count' is captured picture's number
    url = 'http://192.168.0.27:5000/upload'         ## RaspberryPi 2 Network
    image_file = '/home/pi/captured%d.png'% (count)
    print ('image_file', image_file)
    files = {'image':open(image_file, 'rb') }

    post_location = {'c1':'1'}                      ## 'Place1' = location of CCTV
    r = requests.post(url, files = files, data=post_location)
    print(r.text)


## Camera function
def Camera(count):                                 ## 'count' is captured picture's number

    btn_pin = 4                                     ## Start Button pin number
    GP.setmode(GP.BCM)
    GP.setup(btn_pin, GP.IN, pull_up_down=GP.PUD_DOWN)

    while GP.input(btn_pin) == 1:                   ## Clikced Button
        while True:
            cap = cv2.VideoCapture(0)

            while cap.isOpened():
                ret, frame = cap.read()
                cv2.namedWindow('camera')
                cv2.imshow('camera', frame)
                cv2.waitKey(1)

                if (count) % 1 == 0:                ## image store
                    cv2.imwrite('/home/pi/image%d.png' % (count), frame)
                    Transmission(count)

                if (count) >= 1:                    ## image remove
                    os.remove('/home/pi/image%d.png' % (count - 1))
                sleep(0.9)
                count += 1


a = 0
camera(a)


