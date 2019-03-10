from microbit import *

#sleep(10000)
#display.scroll(str(button_a.get_presses()))

#while running_time() < 10000:
    #display.show(Image.ASLEEP)


#display.show(Image.SURPRISED)

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        break
    else:
        display.show(Image.SAD)

display.clear()