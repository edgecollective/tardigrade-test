from machine import UART
import time
import ssd1306
from machine import I2C
from machine import Pin
import bme280


i2c = I2C(-1, Pin(14), Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.show()


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

while True:
    b=bme.values
    amb_temp=b[0]
    amb_press=b[1]
    amb_humid=b[2]

    a=uart.readline()
    print(a)
    try:
        packet_text = str(a, 'ascii')
        print('Received: {0}'.format(packet_text))
        row_vals=packet_text.strip().split(",")
        print(row_vals)
        print(amb_temp,amb_press)
        
        oled.fill(0)
        oled.text(str(index),0,0)
        oled.text(row_vals[0]+","+row_vals[1],0,20)
        oled.text(row_vals[2],0,30)
        oled.text(amb_temp+","+amb_press,0,40)
        oled.show()
        #index=index+1
    except Exception as e:
        print(str(e))
    time.sleep(1)
