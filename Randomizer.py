from microbit import *

import random

#names = ["Brandon", "Brian", "Valencia", "Cindy", "Jeff", "Mindy", "Randy"]

#display.scroll(random.choice(names))

#numbers = [1, 2, 3, 4, 5, 6, 7]

#display.scroll(random.choice(numbers))

#display.show(str(random.randint(1, 6)))

#answer = random.randrange(100) + random.random()
#display.scroll(str(answer))

random.seed(1877)
while True:
    if button_a.was_pressed():
        display.show(str(random.randint(1, 6)))