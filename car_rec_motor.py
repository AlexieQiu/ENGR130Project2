from microbit import *
import radio
from time import sleep_us
import robotbit_library as r
from machine import time_pulse_us
import drive_turn
# Define Ports for the bank of high current output
M1A = 0x1
M1B = 0x2
M2A = 0x3
M2B = 0x4

chnl = 4   #define channel to your team number

r.setup()

radio.config(channel=chnl)
radio.on()

TIME_OUT = 100000  # Increase time out to see farther, but
# this will reduce the sample rate
ECHO = pin1      # ping sensor uses a single pin for ECHO and Trigger
TRIGGER = pin1

def distance(tp, ep):
    # tp is the trigger pin and ep is the echo pin
    ep.read_digital()  # clear echo
    tp.write_digital(1)  # Send a 10 microSec pulse
    sleep_us(10)  # wait 10 microSec
    tp.write_digital(0)  # Send pulse low
    ep.read_digital()  # clear echo signal - This is needed for a
    # pingSensor
    ts = time_pulse_us(ep, 1, TIME_OUT)  # Wait for echo or time out
    if ts > 0:
        ts = ts * 17 // 100  # if system did not timeout, then send
        # back a scaled value
    return ts  # Return timeout error as a negative number (-1)
def send_signal(txt):
    a = button_a.is_pressed()
    if a:
        map, num = read_map.maze(txt)
        display.show(num)
        path = read_map.BFS(map)
        number_of_move = len(path)
        cnt = 0
        record = ""
        while cnt != number_of_move - 1:
            # tuple for path

            x1 = path[cnt][0]
            y1 = path[cnt][1]
            x2 = path[cnt + 1][0]
            y2 = path[cnt + 1][1]

            if x1 < x2 and y1 == y2:
                display.show(Image.ARROW_S)
                if record[len(record) - 1] == "W":
                    drive_turn.turn_left()
                elif record[len(record) - 1] == "E":
                    drive_turn.turn_right()
                drive_turn.forward_1()
                record += "S"
            elif x1 > x2 and y1 == y2:
                display.show(Image.ARROW_N)
                if record[len(record) - 1] == "W":
                    drive_turn.turn_right()
                else:
                    drive_turn.turn_left()
                drive_turn.forward_1()
                record += "N"
            elif y1 > y2 and x1 == x2:
                display.show(Image.ARROW_W)
                if record[len(record) - 1] == "N":
                    drive_turn.turn_left()
                else:
                    drive_turn.turn_right()
                drive_turn.forward_1()
                record += "W"
            elif y1 < y2 and x1 == x2:
                display.show(Image.ARROW_E)
                if record[len(record) - 1] == "N":
                    drive_turn.turn_right()
                else:
                   drive_turn.turn_left()
                drive_turn.forward_1()
                record += "E"
            else:
                continue
            sleep(20)



if __name__ == '__main__':
    # txt_file = input("Input your maze")
    txt_file = "sectorMap4.txt"
    chnl = 4  # change the channel to your team number
    radio.config(channel=chnl)
    # radio.on()
    TIME_OUT = 100000  # Increase time out to see farther, but
    # this will reduce the sample rate
    # ECHO = pin1  # ping sensor uses a single pin for ECHO and Trigger
    # TRIGGER = pin1
    send_signal(txt_file)



