from machine import Pin, I2C , #SoftI2C
from libs.i2c_lcd import I2cLcd
from libs.bmp180 import BMP180
import time

# 定义 I2C 控制对象
i2c = I2C(sda=Pin(6), scl=Pin(7), freq=100000)

# 获取 I2C 从机地址
address = i2c.scan()[0]

# 定义 I2CLCD 对象
i2c_lcd = I2cLcd(i2c, address, 2, 16)

bus = i2c
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

#temp_f= (temp * (9/5) + 32)
while True:
    try:
        temp = bmp180.temperature
        p = bmp180.pressure
        altitude = bmp180.altitude
        i2c_lcd.clear()
        
        i2c_lcd.putstr('{:.2f}°C'.format(temp))#保留小鼠两位
        i2c_lcd.putstr('{:.0f}hPa'.format(p))#第二行的内容输出加\n
        i2c_lcd.putstr('{:.2f}M'.format(altitude))
        time.sleep(1)
        print('{:.2f}°C,{:.0f}hPa,{:.2f}M'.format(temp,p,altitude))
    except OSError as e:
        i2c_lcd.putstr('bmp err!')
        print('bmp error!')
        
time.sleep(1)