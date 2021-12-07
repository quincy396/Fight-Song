from adafruit_circuitplayground import cp
import time
import random
from digitalio import DigitalInOut, Direction, Pull
import board

A1 = DigitalInOut(board.A1)
A2 = DigitalInOut(board.A2)
A3 = DigitalInOut(board.A3)
A4 = DigitalInOut(board.A4)
A5 = DigitalInOut(board.A5)
A6 = DigitalInOut(board.A6)
A7 = DigitalInOut(board.A7)

my_pins = [A1,A2,A3,A4,A5,A6,A7]

for i in my_pins:
    i.direction = Direction.INPUT
    i.pull = Pull.UP


on = False
n = [1,1,1,1]

tones = [262, 0, 0, 0, 262, 0, 0, 0, 262, 0, 0, 0, 262, 0, 0, 0]
current = 0

miniCounter = 0
while True:
    if tones[current] != 0:
        cp.play_tone(tones[current], 0.3)
        current+=1
    else:
        if not A1.value:
            tones[current] = random.randint(200, 350)
        if not A3.value:
            tones[current] = random.randint(350,500)
        if not A4.value:
            tones[current] = random.randint(500,650)
        if not A5.value:
            tones[current] = random.randint(650, 800)
        else:
            miniCounter +=1
            if miniCounter>600:
                miniCounter=0
                current+=1
    if current>15:
        current=0