import pyb

import lcd160cr
lcd = lcd160cr.LCD160CR('X')

from random import randint

while True:
    lcd.rect(randint(0, lcd.w), randint(0, lcd.h), randint(10, 30), randint(10, 30))
    pyb.delay(200)