#/usr/bin/python

import time

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
print "Strike temp.(\xb0C) = "+str(Tw)
raw_input("Press Enter to exit...")
    
    
    
    

