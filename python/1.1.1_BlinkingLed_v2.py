#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import random

LedPin = 17

def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)

    # Set LedPin's mode to output, initial level to High (3.3v)
    GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)

# Define a main function for main process
def main():
    while True:
        # Random delay between 0.5 and 3.0 seconds in 0.5-second increments
        delay = random.choice([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])

        print(f'LED ON for {delay} seconds')
        GPIO.output(LedPin, GPIO.LOW)
        time.sleep(delay)

        print(f'LED OFF for {delay} seconds')
        GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(delay)

# Define a destroy function for clean up everything after the script finished
def destroy():
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()

# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()