from microbit import *
#This functions tests the orientation of the microbit, stating whether or not it is
# orientated to the leeft or to the right.
while True:
    reading = accelerometer.get_x()
    if reading > 20:
        display.show("R")
    elif reading < -20:
        display.show("L")
    else:
        display.show("-")

        # I am not going to include the musical bit for this excersize as
        # as I wasn't able to get proper equipment for the microbit