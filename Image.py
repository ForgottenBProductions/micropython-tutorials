from microbit import *

display.show(Image.HEART)
sleep(4000)

boat = Image("05050:" #These are the co-ordinates on a 5x5 grid. the numbers represent the intensity of the light.
                    "05050:"
                    "05050:"
                    "99999:"
                    "09990")
display.show(boat)