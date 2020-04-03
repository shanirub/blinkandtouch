import pyb

import lcd160cr
lcd = lcd160cr.LCD160CR('X')

from random import randint

SIDE_LENGTH = 70

while True:
    lcd.rect(randint(0, lcd.w - SIDE_LENGTH), randint(0, lcd.h - SIDE_LENGTH), SIDE_LENGTH, SIDE_LENGTH)
    pyb.delay(500)