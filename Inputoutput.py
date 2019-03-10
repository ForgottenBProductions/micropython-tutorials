from microbit import *

#while True:
    #if pin0.is_touched():
        #display.show(Image.SURPRISED)
    #else:
       # display.show(Image.ASLEEP)

while True:
    pin0.write_digital(1)
    sleep(20)
    pin0.write_digital(0)
    sleep(480)

    #Was unable to test if this worked as I don't have the proper equipment to run sound off of the microbit