import lcddriver
from time import *

lcd = lcddriver.lcd()

lcd.lcd_display_string("Bitajor.com", 1)
lcd.lcd_display_string("Raspberry Pi", 2)