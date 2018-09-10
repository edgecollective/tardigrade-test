import tsys01,ms5837

from machine import I2C
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
