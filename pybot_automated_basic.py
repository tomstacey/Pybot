## PyBot v.01
import RPi.GPIO as GPIO
import time

##setup GPIO - this has to be done somewhere in the code
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.IN)
GPIO.setwarnings(False)

## check killswitch and print
killswitchstatus = GPIO.input(10)
print(killswitchstatus)

## functions - these functions actually make the hardware respond on a GPIO level

def forward():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    return

def reverse():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    return
    
def left():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
	return
	
	
def right():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    return
    
def stop():
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    return
	
##main loop

while  1:
		#Go Forward for 1 sec
		forward()
		time.sleep(1)
		
		#Turn Right 90 degrees
		left()
		time.sleep(1)
		
		#add more movement here
		break
        
GPIO.cleanup()        
    




