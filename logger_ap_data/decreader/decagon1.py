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

filename='data3'


while True:
    a=uart.readline()
    if a!=None and '\r' in a:
        print(a)
        b=str(a).split(' ')
        if len(b)==3:
            print(b)
            if(len(b)>3):
                c=b[-3:]
            else:
                c=b
            #ec_str=str(c[0])[-3:]
            d=c[0].split('c')
            ec_str=d[1]
            print(ec_str)
            #print("last three=",str(b[0])[-3:])
            temp_str=str(c[2])[:3]
            ec=int(ec_str)/50.
            temp=(int(temp_str)-400.)/10.
            print(ec,temp)
            f=open(filename+'_ec.txt','a')
            f.write(str(ec)+'\n')
            f.close()
            f=open(filename+'_temp.txt','a')
            f.write(str(temp)+'\n')
            f.close()

