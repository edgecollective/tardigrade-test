import tsys01,ms5837
import sdcard, os
from machine import I2C,SPI
from machine import Pin

SCL=22
SDA=23

i2c = I2C(-1, Pin(SCL), Pin(SDA))

p=ms5837.MS5837(model='MODEL_30BA',i2c=i2c)
t=tsys01.TSYS01(i2c)

p.init()

temp_acc=t.getTemp()
temp,pressure,depth=p.get_measurement()

print(temp_acc)
print(temp,pressure,depth)

sck=Pin(5)
mosi=Pin(18)
miso=Pin(19)
cs = Pin(14, Pin.OUT)
spi2=SPI(2,baudrate=5000000,sck=sck,mosi=mosi,miso=miso)

sd = sdcard.SDCard(spi2, cs)
os.mount(sd,'/sd')
output=os.listdir('/sd')
print(output)

f=open('/sd/data.txt','a')
data_str="%.3f %3.f\n" % (temp_acc,temp)
f.write(data_str)
f.close()

spi2.deinit()


