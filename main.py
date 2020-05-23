import pyb
from random import randint
import lcd160cr
lcd = lcd160cr.LCD160CR('X')
accel = pyb.Accel()

SENSITIVITY = 2                         # minimal sensitivity for the accel
WIDTH = 4                               # food and moving rect width and height

bg = lcd.rgb(255, 255, 255)             # background color = white
rect_fill_color = lcd.rgb(255, 0, 127)  # moving rect fill color = pink
rect_line_color = lcd.rgb(255, 0, 0)    # moving rect line color

rect_x = lcd.w / 2                      # initial x value for rect
rect_y = lcd.h / 2                      # initial y value for rect

food_x = randint(0, lcd.w - WIDTH)          # initial x value for first food
food_y = randint(0, lcd.h - WIDTH)          # initial y value for first food
if food_x % 2 != 0:
    food_x += 1
if food_y % 2 != 0:
    food_y += 1

food_color = lcd.rgb(0, 0 ,0)           # food color = black (to be used for both line and fill colors)

draw_food = True                        # do we need to draw the food?

while True:
    lcd.set_pen(rect_line_color, bg)   
    lcd.erase()                                         # backgroud is set to white
    lcd.set_pen(rect_line_color, rect_fill_color)
    lcd.rect(int(rect_x), int(rect_y), WIDTH, WIDTH)    # rect is drawn with its colots and x,y values

    x = accel.x()                                       # accel objects
    y = accel.y()

    if abs(x) > SENSITIVITY:                            # identifing movement in x axis
        rect_x += x             

    if abs(y) > SENSITIVITY:                            # identifing movement in y axis
        rect_y -= y

    if draw_food:                                       # drawing the food
        lcd.set_pen(food_color, food_color)
        lcd.rect(int(food_x), int(food_y), WIDTH, WIDTH)

    if (rect_x == food_x and rect_y == food_y):
        lcd.write("very good")
        break

    pyb.delay(200)
