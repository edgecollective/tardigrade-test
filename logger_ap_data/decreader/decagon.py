from machine import UART
import time
#import ssd1306
from machine import I2C
from machine import Pin
import re

#i2c = I2C(-1, Pin(14), Pin(2))
#oled = ssd1306.SSD1306_I2C(128, 64, i2c)
#oled.fill(0)
#oled.show()

#oled.fill(0)
#oled.text("Starting up ...",0,0)
#oled.show()

#rx=34
#tx=13

rx=21
tx=19

uart=UART(2,baudrate=1200,bits=8, parity=None, stop=1,rx=rx,tx=tx)

index = 1

filename='data3.txt'


while True:
    a=uart.readline()
    if a!=None and '\r' in a:
        print(a)
        b=str(a).split(' ')
        print(b)
        ec=int(str(b[0])[-3:])
        print("last three=",str(b[0])[-3:])
        f=[]
        try:
            for c in b:
                d=re.sub("\D","",c)
                e=int(d)
                f.append(e)
            #print(f)
            #print(f[2])
            temp=(f[2]-400)/10.
            #print(f[0])
            e=(f[0]/50.)
            if temp < 100 and temp > -10:
                print(e,temp)
            #f=open(filename,'w')
                f=open(filename,'a')
                f.write(str(e)+'\n')
                f.close()
        except:
            q=2
            #print("didn't work")
            
        #print(''.join(e for e in str(a) if e.isalnum()))
    #time.sleep(.002)
