# Basic remote control from microbit V1
# Trace the code to determine how the basic system works
# What would would a better interface for a different context?

from microbit import *
import radio
import read_map
chnl = xx #change the channel to your team number
radio.config(channel=chnl)
radio.on()

map = maze("sectorMap4.txt")
path = BFS(map)
number_of_move = len(path)
cnt = 0
while cnt != number_of_move - 1:
    # tuple for path
    x1 = path[cnt][0]
    y1 = path[cnt][1]
    x2 = path[cnt + 1][0]
    y2 = path[cnt + 1][1]

    if x1 < x2 and y1 == y2:
        display.show(Image.ARROW_S)
        radio.send("S")
    elif x1 > x2 and y1 == y2:
        display.show(Image.ARROW_N)
        radio.send("N")
    elif y1 > y2 and x1 == x2:
        display.show(Image.ARROW_W)
        radio.send("W")
    elif y1 < y2 and x1 == x2:
        display.show(Image.ARROW_E)
        radio.send("E")
    else:
        continue
    sleep(20)
