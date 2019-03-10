from microbit import *

#while True:
#     gesture = accelerometer.current_gesture()
#     if gesture == "face up":
#         display.show(Image.HAPPY)
#     else:
#         display.show(Image.ANGRY)


import random

answers = [

"Maybe",
"Perhaps",
"I couldn't tell you",
"Try asking again",
"Yes",
"No",
"Systems unclear try again",
"Very doubtful",
"Signs point to no",
"Signs point to yes",
"With time",
"Reply hazy try again",
"Can't say",
]

while True:
    display.show("8")
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        display.scroll(random.choice(answers))