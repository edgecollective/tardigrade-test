from machine import UART
import time
import ssd1306
from machine import I2C
from machine import Pin
from machine import SPI

filename='east1a.csv'

import bme280

import sdcard, os

i2c = I2C(-1, Pin(14), Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.show()

sck=Pin(16)
mosi=Pin(4)
miso=Pin(17)
cs = Pin(15, Pin.OUT)
spi2=SPI(2,baudrate=5000000,sck=sck,mosi=mosi,miso=miso)

sd = sdcard.SDCard(spi2, cs)
os.mount(sd,'/sd')


oled.fill(0)
oled.text("Starting up ...",0,0)
oled.show()

bme = bme280.BME280(i2c=i2c)

#rx=34
#tx=13

rx=21
tx=19

uart=UART(2,baudrate=1200,rx=rx,tx=tx)

index = 1

f=open('/sd/'+filename,'a')
data_str="counter, p_h20, t_h20, d_h20, p_amb, t_amb, h_amb"
f.write(data_str+"\n")
f.close()
    
counter=0
while True:
    b=bme.values
    print(b)
    t_amb=float(b[0])
    p_amb=float(b[1])
    h_amb=float(b[2])

    a=uart.readline()
    print(a)
    try:
        packet_text = str(a, 'ascii')
        print('Received: {0}'.format(packet_text))
        row_vals=packet_text.strip().split(",")

        t_h20=float(row_vals[0])
        p_h20=float(row_vals[1])
        d_h20=float(row_vals[2])
        
        f=open('/sd/'+filename,'a')
        data_str="%d,%s,%s,%s,%s,%s,%s" % (counter,p_h20, t_h20, d_h20, p_amb, t_amb, h_amb)
        #print("host:"+ip[0])
        print(data_str)
        f.write(data_str+"\n")
        f.flush()
        f.close()
            
        
        oled.fill(0)
        oled.text(str(counter),0,0)
        oled.text(row_vals[0]+","+row_vals[1],0,20)
        oled.text(row_vals[2],0,30)
        oled.text(str(t_amb)+","+str(p_amb),0,40)
        oled.show()
        counter=counter+1
        #index=index+1
    except Exception as e:
        print(str(e))
    time.sleep(1)
