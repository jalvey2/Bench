import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import time, sys
import os.path
import csv

start_time1 = time.time()
####setup ADC and assign input pin



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

data = [[newfile, "Drops", "mL/min"],
        ["Time(s)", "F1", "F1"]] #Sets all tuples in list form
i = open('UVM'+newfile+'.csv', 'ab') #Assigns variable to open file with auto-populated name
tempwriter = csv.writer(i)
for row in data:
    tempwriter.writerow(row) #opens file and writes new data to the list
try:

    while True:
            if GPIO.event_detected(PIPin):
                countPulse1()

                elapsed_time = time.time()
                deltaT = float(elapsed_time) - float(start_time1) #calculates the number of$
                PermFloR = (count1*0.053)/(deltaT/60) #units are mL/min

                data1 = [[deltaT, PermFloR]] #Sets all tuples in list form
                #i = open('UVM'+newfile+'.csv', 'ab') #Assigns variable to open file with auto-populated name
                #tempwriter = csv.writer(i)
                for row in data1:
                    tempwriter.writerow(row) #opens file and writes new data to the list
                    #i.close()

                print 'Time(sec)=\t\t%s' % (deltaT) # Time in seconds
                print 'F1(mL/min)=\t\t%s' % (PermFloR) # Flow rate in mL/min
                print
                print count1
                print deltaT/60
                print
            else:
                pass

except KeyboardInterrupt:
    i.close()
    GPIO.cleanup()
        #elapsed_time = time.time()
        #deltaT = float(elapsed_time) - float(start_time1)

