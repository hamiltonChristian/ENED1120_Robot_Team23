#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, Motor, SpeedPercent

## selects the motor in port A
m1 = Motor(OUTPUT_A)

## asks for input using SSH console
sp = float(input("Speed Percent = "))

## Runs motor 1 for 5 seconds as sp% of full speed
m1.on_for_seconds(SpeedPercent(sp),5)
