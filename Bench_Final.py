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

psensor_pin1 = 'P9_38'
psensor_pin2 = 'P9_40'


newfile = time.strftime('%Y-%b-%d,%H:%M:%S', time.localtime())

print newfile

w1 = "/sys/bus/w1/devices/28-000007c65b5c/w1_slave" #Device 1 file
w2 = "/sys/bus/w1/devices/28-0417a2631fff/w1_slave" #Device 2 file

PIPin = "P9_24"

#def setup():
    #GPIO.add_event_detect(SensorPin, GPIO.FALLING)
GPIO.setup(PIPin, GPIO.IN)

GPIO.add_event_detect(PIPin, GPIO.FALLING)

count1 = 0

def countPulse1():
   global count1
   count1 = count1+1

#flow calibration[Test1: 100 drops, 5.28 mL; Test2:  100 drops, 5.3 mL;
#Test3: 100 drops, 5.32 mL]
#Average vol per drop: 5.3 ml/100 drops = .053 mL/drop

def readTemp1():
         raw = open(w1, "r").read()
         f = str((float(raw.split("t=")[-1])/1000)*(9.0/5.0) + 32.0)
         c = str(float(raw.split("t=")[-1])/1000)
         identifier1 = 'T1'
         result1 = 'T1 =\t%s\t\t%s' % (c, f)
         return (result1, identifier1, f, c)

result1, identifier1, f, c = readTemp1() #Assign returned tuple

def readTemp2():
         raw = open(w2, "r").read()
         f2 = str((float(raw.split("t=")[-1])/1000)*(9.0/5.0) + 32.0)
         c2 = str(float(raw.split("t=")[-1])/1000)
         identifier2 = 'T2'
         result2 = 'T2 =\t%s\t\t%s' % (c2, f2)
         return (result2, identifier2, f2, c2)

result2, identifier2, f2, c2 = readTemp2() #Assign returned tuple

data = [[newfile, "degrees C", "degrees C",
        "Drops", "mL/min",
        "raw signal", "Volts", "psi", "bar", "raw signal", "Volts", "psi",
        "bar"],
        ["Time(s)", "T1", "T2", "F1", "F1", "P1", "P1", "P1", "P1", "P2", "P2", "P2",
        "P2", "Jp", "TMP"]] #Sets all tuples in list form
i = open('UVM'+newfile+'.csv', 'ab') #Assigns variable to open file with auto-populated name
tempwriter = csv.writer(i)
for row in data:
    tempwriter.writerow(row) #opens file and writes new data to the list
i.close()

try:

    while True:
            if GPIO.event_detected(PIPin):
                countPulse1()

                elapsed_time = time.time()
                deltaT = float(elapsed_time) - float(start_time1) #calculates the number of$
                PermFloR = (count1*0.053)/(deltaT/60) #units are mL/min

                #raw = open(w1, "r").read()
                #raw = open(w2, "r").read()
                readTemp1()
                result1, identifier1, f, c = readTemp1()
                readTemp2()
                result2, identifier2, f2, c2 = readTemp2()

                reading1 = ADC.read(psensor_pin1)
                time.sleep(0.01)
                reading2 = ADC.read(psensor_pin2)
                time.sleep(0.01)


                #scale reading back to voltage
                volts1=reading1*1.800
                volts2=reading2*1.800



                #scale 1.8V reading to pressure based on 4-20mA signal read
                #from shunt resistor with a 1.8V max at 20 mA corresponding to
                #100 psi and a 4mA min corresponding to 0 psi
                pressure1 = volts1 * 70.54176072 - 25.00 #psi
                pressure2 = volts2 * 140.7657658 - 50.00 #psi

                #SiC_SA = 0.01628916
                #permeateflux = flow0 * 3.78541 * 60 / SiC_SA #gpm * L/gal * min/hr / m^2
                TMP = pressure1 - pressure2 #(pressure feed + pressure reject)/2 - pressure permeate


                print 'Time(sec)=\t\t%s' % (deltaT) # Time in seconds
                print '%s\n%s' % ((result1), (result2)) #This prints on the display screen
                print 'F1(mL/min)=\t\t%s' % (PermFloR) # Flow rate in mL/min
                print 'P1=\t%s\t%s\t%s' % (reading1, volts1, pressure1)
                print 'P2=\t%s\t%s\t%s' % (reading2, volts2, pressure2)
                print count1
                print deltaT/60
                #print 'Jp=\t%s' % (permeateflux)
                print 'TMP=\t%s' % (TMP)
                print

               #prints raw reading, output voltage, and flow
                data1 = [[deltaT, c, c2, count1, PermFloR,
                        reading1, volts1, pressure1,
                        pressure1*0.0689476, reading2, volts2, pressure2,
                        pressure2*0.0689476]]# permeateflux, TMP]] #Sets all tuples in list form
                i = open('UVM'+newfile+'.csv', 'ab') #Assigns variable to open file with auto-populated name
                tempwriter = csv.writer(i)
                for row in data1:
                    tempwriter.writerow(row) #opens file and writes new data to the list
                i.close()
                time.sleep(.05)
            else:
                elapsed_time = time.time()
                deltaT = float(elapsed_time) - float(start_time1) #calculates the number of$
                PermFloR = (count1*0.053)/(deltaT/60) #units are mL/min

                #raw = open(w1, "r").read()
                #raw = open(w2, "r").read()
                readTemp1()
                result1, identifier1, f, c = readTemp1()
                readTemp2()
                result2, identifier2, f2, c2 = readTemp2()

                reading1 = ADC.read(psensor_pin1)
                time.sleep(0.01)
                reading2 = ADC.read(psensor_pin2)
                time.sleep(0.01)


                #scale reading back to voltage
                volts1=reading1*1.800
                volts2=reading2*1.800



                #scale 1.8V reading to pressure based on 4-20mA signal read
                #from shunt resistor with a 1.8V max at 20 mA corresponding to
                #100 psi and a 4mA min corresponding to 0 psi
                pressure1 = volts1 * 70.54176072 - 25.00 #psi
                pressure2 = volts2 * 140.7657658 - 50.00 #psi

                #SiC_SA = 0.01628916
                #permeateflux = flow0 * 3.78541 * 60 / SiC_SA #gpm * L/gal * min/hr / m^2
                TMP = pressure1 - pressure2 #(pressure feed - pressure permeate)


                print 'Time(sec)=\t\t%s' % (deltaT) # Time in seconds
                print '%s\n%s' % ((result1), (result2)) #This prints on the display screen
                #print 'F1(mL/min)=\t\t%s' % (PermFloR) # Flow rate in mL/min
                print 'P1=\t%s\t%s\t%s' % (reading1, volts1, pressure1)
                print 'P2=\t%s\t%s\t%s' % (reading2, volts2, pressure2)
                print count1
                print deltaT/60
                #print 'Jp=\t%s' % (permeateflux)
                print 'TMP=\t%s' % (TMP)
                print

               #prints raw reading, output voltage, and flow
                data1 = [[deltaT, c, c2, count1, "",
                        reading1, volts1, pressure1,
                        pressure1*0.0689476, reading2, volts2, pressure2,
                        pressure2*0.0689476]]# permeateflux, TMP]] #Sets all tuples in list form
                i = open('UVM'+newfile+'.csv', 'ab') #Assigns variable to open file with auto-populated name
                tempwriter = csv.writer(i)
                for row in data1:
                    tempwriter.writerow(row) #opens file and writes new data to the list
                i.close()
                time.sleep(0.05)

except KeyboardInterrupt:
    GPIO.cleanup()
