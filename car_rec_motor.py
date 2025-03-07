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

    
def Drive(lft,rgt):
# Receive the percent power to drive each motor in a specific direction
    r.motor(M2B, lft)
    r.motor(M1A, rgt)

while True:
    s = radio.receive()                    # receive direction command
    if s is not None:
        if s == "F":
            drive_turn.forward_1()
        if s=="L":                         # Drive forward
            drive_turn.turn_left()
        else:
            drive_turn.turn_right()
    sleep(20)

