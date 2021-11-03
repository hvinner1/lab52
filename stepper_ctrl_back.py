#!/usr/bin/python3
# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output
#controls the led and motor steps
import RPi.GPIO as GPIO
import time
from PCF import *
from step import *
import json
GPIO.setmode(GPIO.BCM)


while True:
    with open("lab5.txt", 'r') as f:
      datas = json.load(f)
      slider = float(datas['angle'])
      sub = float(datas['change'])
      zero = float(datas['Zero'])
      if sub == 1:
        stepper.goAngle(slider)
        #call angle.stepper
        time.sleep(0.1)
      elif zero == 1: #should this be if
        stepper.zero()