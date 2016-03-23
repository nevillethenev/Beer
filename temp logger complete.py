#/usr/bin/python
import serial 
import time
import matplotlib.pyplot as plt
import numpy as np
import os

"""""""""""""""""""""""""""""""""""
"""""""NEVS BEER SCRIPT""""""""""""
"""""""""""""""""""""""""""""""""""

###need to add exception handler for serial disconnection


##  SETUP SERIAL PORT

try:
    ser = serial.Serial('COM3',9600)  # open serial port
    print('Serial connection established!')
    
except: 
    print('ERR: Unable to connect to arduino...retrying')
    time.sleep(3)
    try:
        ser = serial.Serial('COM3',9600)
    except:
        raw_input('ERR: Unable to connect to arduino....check connections and press Enter to continue')
        try:
            ser = serial.Serial('COM3',9600)
        except:
            raw_input('ERR: Unable to connect to arduino...Press Enter to exit..')

##  STRIKE WATER CALCULATOR
    
##strike water calculator
##volume of water is heated inside an insulated mash tun
##grain is added to mash tun
## Tw = (Tm((Sw*mw)+(Sg*mg))-(Sg*mg*Tg))/(Sw*mw)
## Tw = strike water temp.
## Tm = mash temp.

Sw = 1; ##Specific heat water
Sg = 0.4; ##Specific heat grain

beername = raw_input("Please enter the name of the beer:")
Tm = input("Mash Temp.(\xb0C)")
Vw = input("Water Volume(L)")
mw = Vw; ##mass water(kg) =  volume water(L)
mg = input("Grain mass(kg)")
Tg = input("Grain temp.(\xb0C)")
print("Calculating...")
time.sleep(1)
Tw = (Tm*((Sw*mw)+(Sg*mg))-(Sg*mg*Tg))/(Sw*mw)
Tw = round(Tw,1)
##print "Strike temp.(\xb0C) = "+str(Tw)


##  MASH INSTRUCTIONS

print 'Set strike temperature to ' + str(Tw) + '\xb0C' 
raw_input('Press Enter to continue...')
temperaturefloat = 0

##measure temperature
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
            time.sleep(0.1)
        
    print str(temperaturefloat) + '\xb0C'
    time.sleep(0.1)
      
##    if temperaturefloat >  Tm:    #### check temperature 5 times
##        dragon = np.ones(5)        
##        for i in range(0,4):
##            try:
##                temperaturefloat = round(float(ser.read(7)),1)
##            except:  ##handle all serial read errors
##                temperaturefloat = 0
##        
##            if temperaturefloat < 0:  
##                temperaturefloat = 0
##            
##            print str(temperaturefloat) + '\xb0C'
##            dragon[i] = temperaturefloat
##            print str(dragon)
##            time.sleep(0.1)    
##        if sum(dragon)/5 > Tm:
##            print 'SUCCESS'
##            break
    if temperaturefloat >  Tm: 
        print 'Stike temperature reached! Please stir the water and prepare grain for submersion...'
        mashtime1 = 60*input('Enter total mash time (min):')
        raw_input('Submerge grain and press enter to coninue...')
        print 'Mash in progress, please wait ' + str(mashtime1/60) + ' minutes...'
        break
##  TEMPERATURE LOGGING

ser.close() ## restart Com port
ser = serial.Serial('COM3',9600)

print 'Temp(\xb0C)\tTime(s)'
nowtimefloat = 0
temperaturefloat = 0
#read from serial and exit when user wants   
while nowtimefloat < mashtime1:
    try:
        temperaturefloat = round(float((ser.read(7))),1)   #read
    except: ##handle all serial read errors
        try:
            ser = serial.Serial('COM3',9600)  # open serial port
        except:
            ser.close()
            ser = serial.Serial('COM3',9600)  # open serial port
            temperaturefloat = 0
            time.sleep(0.1)
            
    nowtimefloat = round(time.clock(),1)
    
    nowtimestring = str(nowtimefloat)
    temperaturesting = str(temperaturefloat)
    
    goblin = open('templog.txt','a') #open txt file
    datastring = temperaturesting + '\t' + nowtimestring + '\n'

    print(datastring) #print temp to console 
    goblin.write(datastring)       
##    goblin.flush()
##    ser.close()     # close port
else:
    print "Mash complete!"
    raw_input('Press Enter to save the data..')
    goblin.close()
    os.rename('templog.txt',beername + 'templog.txt')
    print 'Data saved!'
    
raw_input('Press Enter to exit...')
    
##  DATA ANALYSIS

##plt.axis([0,3600,55,75])
###temperature lines
##plt.hlines(70,0,3600,colors='r')
##plt.hlines(60,0,3600,colors='r')
##
##dragon = np.loadtxt('templog.txt', delimiter="\t")
##x = dragon[:,1]
##y = dragon[:,0]
##
##plt.scatter(x,y)
####plt.draw()
##plt.show()
##plt.waitforbuttonpress()
####plt.pause(0.1)
##
##raw_input('Press Enter to exit...')
##
    
    

