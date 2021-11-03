import RPi.GPIO as GPIO
import time
from PCF8591 import *

class Stepper:
  def __init__(self,address):
    self.pins = [18,21,22,23]
    for pin in pins:
      GPIO.setup(pin, GPIO.OUT, initial=0)
    self.sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
    self.state = 0 
    self.led = 16
    self.GPIO.setmode(GPIO.BCM)
    self.GPIO.setup(led, GPIO.OUT)

  def delay_us(self,tus): # use microseconds to improve time resolution
    self.endTime = time.time() + float(tus)/ float(1E6)
    while time.time() < self.endTime: #is this right
      pass

  def halfstep(self,dir):
    # dir = +/- 1 (ccw / cw)
    self.state += dir
    if self.state > 7: self.state = 0
    elif self.state < 0: self.state =  7
    for pin in range(4):    # 4 pins that need to be energized
      GPIO.output(self.pins[pin], self.sequence[self.state][pin])
    self.delay_us(1000)  #need this here?

  def moveSteps(self,steps, dir):
    # move the actuation sequence a given number of half steps
    for step in range(steps):
      self.halfstep(dir)

  def goAngle(self,angle):
    GPIO.output(led, 0)
    self.moveSteps(angle,1)

  def zero():
    GPIO.output(led, GPIO.HIGH) # set output to 3.3V
    self.sensor = photo.light()
    while sensor > 200:
      moveSteps(360,1)
      #move the motor using
    GPIO.output(led, 0) # set output to 0V
    time.sleep(0.1)
    #zero() – turn the motor until the photoresistor is occluded by the cardboard piece. Only actuate the LED while the zeroing process is ongoing.




#self.photo = photo(0x48) #change




  
GPIO.cleanup() 
