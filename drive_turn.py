from microbit import *
import robotbit_library as r
from time import sleep_us
from machine import time_pulse_us

M1A = 0x1
M1B = 0x2
M2A = 0x3
M2B = 0x4

M1A = 0x1
M1B = 0x2
M2A = 0x3
M2B = 0x4

r.setup()

def forward_1():
    sleep(1000)
    r.motor(M2B, 83.5)
    r.motor(M1A, -90)
    sleep(730)
    r.motor(M2B, 0)
    r.motor(M1A, 0)

def turn_left():
    sleep(1000)
    r.motor(M2B, 38)
    r.motor(M1A, -40)
    sleep(120)
    r.motor(M2B, 0)
    r.motor(M1A, 0)
    sleep(1000)
    r.motor(M2B, -90)
    r.motor(M1A, -90)
    sleep(239)
    r.motor(M2B, 0)
    r.motor(M1A, 0)

def turn_right():
    sleep(1000)
    r.motor(M2B, 38)
    r.motor(M1A, -40)
    sleep(120)
    r.motor(M2B, 0)
    r.motor(M1A, 0)
    sleep(1000)
    r.motor(M2B, 90)
    r.motor(M1A, 90)
    sleep(239)
    r.motor(M2B, 0)
    r.motor(M1A, 0)
