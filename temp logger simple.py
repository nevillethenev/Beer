#/usr/bin/python
import serial 
import time
import matplotlib.pyplot as plt
import numpy as np

try:
    ser = serial.Serial('COM3',9600)  # open serial port
    print 'Waiting for response...'
except: 
    print('ERR: Unable to connect to arduino')
    time.sleep(3)
    try:
        ser = serial.Serial('COM3',9600)
    except:
        raw_input('ERR: Unable to connect to arduino....check connections and press Enter to continue')
        try:
            ser = serial.Serial('COM3',9600)
        except:
            raw_input('ERR: Unable to connect to arduino...Press Enter to exit...')
    
#read from serial and exit when user wants   
while True:
        try:
            temperaturefloat = round(float((ser.read(7))),1)   #read
        except: ##handle all serial read errors
            try:
                ser = serial.Serial('COM3',9600)  # open serial port
            except:
                ser.close()
                ser = serial.Serial('COM3',9600)  # open serial port
                temperaturefloat = 0
                time.sleep(1)
            
        nowtimefloat = round(time.clock(),1)
            
        nowtimestring = str(nowtimefloat)
        temperaturesting = str(temperaturefloat)
            
        goblin = open('templog.txt','a') #open txt file
        datastring = temperaturesting + '\t' + nowtimestring + '\n'

        print(datastring) #print temp to console 
        goblin.write(datastring)

raw_input('Press Enter to exit...')


    
    

