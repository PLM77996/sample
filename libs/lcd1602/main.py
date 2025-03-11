from machine import Pin, SoftI2C, I2C
from libs.i2c_lcd import I2cLcd

# 定义 SoftI2C 控制对象
i2c = I2C(sda=Pin(13), scl=Pin(14), freq=100000)

# 获取 I2C 从机地址
address = i2c.scan()[0]

# 定义 I2CLCD 对象
i2c_lcd = I2cLcd(i2c, address, 2, 16)

# 显示 Hello world
i2c_lcd.putstr('Hello, world!')

