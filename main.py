import pyb

import lcd160cr
lcd = lcd160cr.LCD160CR('X')
accel = pyb.Accel()

from random import randint

SENSITIVITY = 3

bg = lcd.rgb(255, 255, 255)

dot_x = lcd.w / 2
dot_y = lcd.h / 2
dot_color = lcd.rgb(0, 0, 0)

food_x = randint(0, lcd.w)
food_y = randint(0, lcd.h)
food_color = lcd.rgb(255, 0 ,127)
draw_food = True

while True:
    lcd.erase()
    lcd.set_pen(dot_color, bg)   
    lcd.dot(int(dot_x), int(dot_y))
    x = accel.x()
    y = accel.y()

    if abs(x) > SENSITIVITY:
        dot_x += x

    if abs(y) > SENSITIVITY:
        dot_y -= y

    if draw_food:
        lcd.set_pen(food_color, bg)
        lcd.dot(food_x, food_y)

    if (dot_x == food_x and dot_y == food_y):
        lcd.write("very good")
        break

    pyb.delay(200)
