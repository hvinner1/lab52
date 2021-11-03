import RPi.GPIO as GPIO
import time
from PCF import *


# current position in stator sequence

'''class photo(PCF8591):

  def __init__(self,address):
    self.PCF8591 = PCF8591(0x48) #try only numbs
   

  def light(self):  
    try:
      self.light = self.PCF8591.read(0)
    except Exception as e:
        print ("Error: %s \n" % e)
    return self.light
    
 '''

def delay_us(tus): # use microseconds to improve time resolution
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:
    pass



class Stepper:
  def __init__(self):
      self.ledPin = 16
      self.pins = [21,20,16,12] # controller inputs: in1, in2, in3, in4
      # i changed the pins because of my circuit, you can change them back
      GPIO.setmode(GPIO.BCM)
      for pin in self.pins:
        GPIO.setup(pin, GPIO.OUT, initial=0)
      GPIO.setup(self.ledPin, GPIO.OUT, initial=0)
      self.sequence = [[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
             [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
      self.state = 0  # current position in stator sequence
      self.current = 0
      self.stepAngle = 2*4*512/360

  def goAngle(self, angle):
    #GPIO.setmode(GPIO.BCM)
    self.moveSteps(angle,1)

    
  def halfstep(self, dir):
  # dir = +/- 1 (ccw / cw)
    global state
    self.state += dir
    if self.state > 7: self.state = 0
    elif self.state < 0: self.state =  7
    for pin in range(4):    # 4 pins that need to be energized
        GPIO.output(self.pins[pin], self.sequence[self.state][pin])
    delay_us(1000)

  def moveSteps(self, steps, dir):
  # move the actuation sequence a given number of half steps
    for step in range(steps):
       self.halfstep(dir)
       
    
  def zero(self):
    GPIO.output(led, 1) # set output to 3.3V
    sensor = photo.light()
    while sensor > 200:
      self.moveSteps(360,1)
      #move the motor using
    GPIO.output(led, 0) # set output to 0V
    time.sleep(0.1)
    #zero() – turn the motor un
  
  GPIO.cleanup()
  
a = Stepper()
a.goAngle(200)
