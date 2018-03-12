import Adafruit_BBIO.GPIO as GPIO
import time, sys
import os.path
import csv

start_time1 = time.time()

newfile = time.strftime('%Y-%b-%d,%H:%M:%S', time.localtime())

print newfile

elapsed_time = time.time()
deltaT = float(elapsed_time) - float(start_time1)
deltaT2 = float(elapsed_time) - float(start_time1)
#deltaT2 = (float(time.time()) - float(elapsed_time))/60
#deltaT = deltaT2
def timecount():
    deltaT = float(elapsed_time) - float(start_time1)
    deltaT2 = float(elapsed_time) - float(start_time1)
    if deltaT2 >= 60:
        #elapsed_time = 0
        deltaT2 = deltaT2 - 60
        #deltaT2 = (float(elapsed_time) - float(deltaT))/60
    return (deltaT2)

deltaT2 = timecount()
    #else False:
        #deltaT2 = float(elapsed_time) - float(start_time1)

try:
    while True:
        elapsed_time = time.time()
        deltaT = float(elapsed_time) - float(start_time1)
        #deltaT2 = float(elapsed_time) - float(start_time1)
        deltaT2
        if deltaT >= 60:
            print deltaT2
            #elapsed_time = 0
            #deltaT3 = deltaT2 - 60
            #deltaT2 = (float(elapsed_time) - float(deltaT))/60
            #yield (deltaT2)

#        else:
#            deltaT2 = float(elapsed_time) - float(start_time1)
        print start_time1
        print elapsed_time
        print 'Time(sec)=\t\t%s' % (deltaT) # Time in seconds
        print 'Time2(sec)=\t\t%s' % (deltaT2)
        time.sleep(1)

#flow calibration[Test1: 100 drops, 5.28 mL; Test2:  100 drops, 5.3 mL;
#Test3: 100 drops, 5.32 mL]
#Average vol per drop: 5.3 ml/100 drops = .053 mL/drop


except KeyboardInterrupt:
    GPIO.cleanup()
        #elapsed_time = time.time()
        #deltaT = float(elapsed_time) - float(start_time1)
