import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import time, sys
import os.path
import csv

start_time1 = time.time()
####setup ADC and assign input pin
ADC.setup()
#analog input pins are
# "AIN0", "P9_39", F1
# "AIN2", "P9_37", F2
# "AIN6", "P9_35", F3
# "AIN1", "P9_40", P1
# "AIN3", "P9_38", P2
# "AIN5", "P9_36", P3



newfile = time.strftime('%Y-%b-%d,%H:%M:%S', time.localtime())

print newfile


PIPin = "P9_24"

#def setup():
    #GPIO.add_event_detect(SensorPin, GPIO.FALLING)
GPIO.setup(PIPin, GPIO.IN)

GPIO.add_event_detect(PIPin, GPIO.FALLING)


count1 = 0

def countPulse1():
   global count1
   count1 = count1+1

try:

    while True:
            if GPIO.event_detected(PIPin):
                countPulse1()

                elapsed_time = time.time()
                deltaT = float(elapsed_time) - float(start_time1) #calculates the number of$
                PermFloR = (count1*0.053)/(deltaT/60) #units are mL/min
                print 'Time(sec)=\t\t%s' % (deltaT) # Time in seconds
                print 'F1(mL/min)=\t\t%s' % (PermFloR) # Flow rate in mL/min
                print
                print count1
                print deltaT/60
                print
                time.sleep(0.05)
            else:
                time.sleep(0.01)

except KeyboardInterrupt:
    GPIO.cleanup()
        #elapsed_time = time.time()
        #deltaT = float(elapsed_time) - float(start_time1)
