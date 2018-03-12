import Adafruit_BBIO.GPIO as GPIO
import time, sys
import os.path
import csv

start_time1 = time.time()

newfile = time.strftime('%Y-%b-%d,%H:%M:%S', time.localtime())

print newfile

PIPin = "P9_24"

#def setup():
    #GPIO.add_event_detect(SensorPin, GPIO.FALLING)
GPIO.setup(PIPin, GPIO.IN)

GPIO.add_event_detect(PIPin, GPIO.FALLING)

count1 = 0
count2 = 0

elapsed_time = time.time()
deltaT = float(elapsed_time) - float(start_time1)

def countPulse1():
    global count1
    count1 = count1+1
    elapsed_time = time.time()
    deltaT = float(elapsed_time) - float(start_time1) #calculates the number of seconds
    PermFloR = (count1*0.53)/(deltaT/60) #units are mL/min

def timecount():
    deltaT = float(elapsed_time) - float(start_time1)
    #deltaT = int(float(elapsed_time) - float(start_time1))
    if deltaT >= 60:
        new_start = time.time()
        global deltaT2
        deltaT2 = (float(elapsed_time) - float(new_start))/60
    else:
        pass

def countPulse2():
    global count2
    #count2 = count2+1
    if deltaT2 >= 1:
        global count2
        count2 = 0
    else:
        global count2
        count2 = count2+1
        PermFloR2 = (count2*0.53/deltaT2)

            #print deltaT
            #print flowrate + 'mL/min'
    print 'Time(sec)=\t\t%s' % (deltaT) # Time in seconds
    print 'Time(sec)=\t\t%s' % (deltaT2)
    print 'F1(mL/min)=\t\t%s' % (PermFloR) # Flow rate in mL/min
    print 'F1(mL/min)=\t\t%s' % (PermFloR2) # Flow rate in mL/min
    print
    time.sleep(0.05)
#flow calibration[Test1: 100 drops, 5.28 mL; Test2:  100 drops, 5.3 mL;
#Test3: 100 drops, 5.32 mL]
#Average vol per drop: 5.3 ml/100 drops = .053 mL/drop
try:
    while True:
        if GPIO.event_detected(PIPin):
            countPulse1()
            timecount()
            countPulse2()

        else:
            time.sleep(0.01)

except KeyboardInterrupt:
    GPIO.cleanup()
        #elapsed_time = time.time()
        #deltaT = float(elapsed_time) - float(start_time1)
