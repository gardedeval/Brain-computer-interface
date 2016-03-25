from i2clibraries import i2c_hmc5883l
import time
import math
import sys
import socket

hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1)
hmc5883l.setContinuousMode()

#try:
import RPi.GPIO as GPIO
#except RuntimeError:
#	print("ERROR")



GPIO.setmode(GPIO.BOARD)
def backward():
    GPIO.setup(7,GPIO.OUT)
    GPIO.output(7,GPIO.LOW)

    GPIO.setup(11,GPIO.OUT)
    GPIO.output(11,GPIO.HIGH)

    GPIO.setup(13,GPIO.OUT)
    GPIO.output(13,GPIO.LOW)

    GPIO.setup(15,GPIO.OUT)
    GPIO.output(15,GPIO.HIGH)

def forward():
    GPIO.setup(7,GPIO.OUT)
    GPIO.output(7,GPIO.HIGH)

    GPIO.setup(11,GPIO.OUT)
    GPIO.output(11,GPIO.LOW)

    GPIO.setup(13,GPIO.OUT)
    GPIO.output(13,GPIO.HIGH)

    GPIO.setup(15,GPIO.OUT)
    GPIO.output(15,GPIO.LOW)


def right():
    GPIO.setup(7,GPIO.OUT)
    GPIO.output(7,GPIO.LOW)

    GPIO.setup(11,GPIO.OUT)
    GPIO.output(11,GPIO.LOW)

    GPIO.setup(13,GPIO.OUT)
    GPIO.output(13,GPIO.HIGH)

    GPIO.setup(15,GPIO.OUT)
    GPIO.output(15,GPIO.HIGH)

def left():
    GPIO.setup(7,GPIO.OUT)
    GPIO.output(7,GPIO.HIGH)

    GPIO.setup(11,GPIO.OUT)
    GPIO.output(11,GPIO.HIGH)

    GPIO.setup(13,GPIO.OUT)
    GPIO.output(13,GPIO.LOW)

    GPIO.setup(15,GPIO.OUT)
    GPIO.output(15,GPIO.LOW)

def stop():
    GPIO.setup(7,GPIO.OUT)
    GPIO.output(7,GPIO.LOW)

    GPIO.setup(11,GPIO.OUT)
    GPIO.output(11,GPIO.LOW)

    GPIO.setup(13,GPIO.OUT)
    GPIO.output(13,GPIO.LOW)

    GPIO.setup(15,GPIO.OUT)
    GPIO.output(15,GPIO.LOW)
	
def getAngle(x,y,z):
        angle1=0
        if(y>0):
          angle1=90-math.atan(x/y)*(180/math.pi)
        elif(y<0):
          angle1=270-math.atan(x/y)*(180/math.pi)
        elif(y==0 and x<0):
          angle1=180
        elif(y==0 and x>0):
          angle1=0
        return angle1

def moveRobot(reference):
    i=0
    g_rate=0
    angle=0
    angle1=0
    prev_g_rate=0
    flag=0
    #reference=30
    while(1):
        (x,y,z) = hmc5883l.getAxes()
        angle1 = getAngle(x,y,z)
        print(reference," ",angle1)
        if((angle1 - reference) >= -5 and (angle1 - reference) <= 5):
            break
        if((angle1 - reference) < 0):
            if((angle1 - reference)>(-200)):
                right()
                time.sleep(0.01)
                stop()
            else:
                left()
                time.sleep(0.01)
                stop()
        else:
            if((angle1 - reference)>200):
                right()
                time.sleep(0.01)
                stop()
            else:
                left()
                time.sleep(0.01)
                stop()
	    

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	HOST = "192.168.42.1"
	PORT = 6789
	s.bind((HOST,PORT))

	while(True):
		data, addr = s.recvfrom(1024)
		moveRobot(int(data.decode('ascii')))

except KeyboardInterrupt:
	GPIO.cleanup()
except :
       e  = sys.exc_info()[0]
       print("Some error :( %s" %e)
finally:
       GPIO.cleanup()



	       
       



	
