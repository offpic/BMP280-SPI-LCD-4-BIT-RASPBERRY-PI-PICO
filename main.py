from machine import Pin, SPI
from utime import sleep
from bmp280_spi import BMP280SPI
from bmp280 import BMP280
from lcd1602 import LCD1602
import math

lcd = LCD1602(e=21, rs=20, d4=22, d5=26, d6=27, d7=28)

spi1_sck = Pin(10)  #SCL
spi1_tx = Pin(11)   #SDA   DIN
spi1_rx = Pin(12)   #SDO
spi1_csn = Pin(13, Pin.OUT, value=1)    #CSB
spi1 = SPI(1, sck=spi1_sck, mosi=spi1_tx, miso=spi1_rx)
bmp280_spi = BMP280SPI(spi1, spi1_csn)

while True:
    readout = bmp280_spi.measurements
    print(f"Temperature: {readout['t']:.2f} °C, pressure: {readout['p']:.2f} hPa.")
    lcd.clear()
    lcd.cursor_home()
    lcd.print_str(f"Temp: {readout['t']:.2f} C")
    lcd.cursor_home()
    lcd.cursor_shift(40)
    lcd.print_str(f"Pres: {readout['p']:.2f} hPa")
    sleep(1)