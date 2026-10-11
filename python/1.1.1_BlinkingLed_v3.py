#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

LedPin = 17

def setup():
    # Set GPIO mode to BCM numbering
    GPIO.setmode(GPIO.BCM)

    # Set LED pin as output
    GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)

def get_delay():
    while True:
        try:
            delay = int(input("Enter LED delay (1-9 seconds): "))

            if 1 <= delay <= 9:
                return delay
            else:
                print("Please enter a number between 1 and 9.")

        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    delay = get_delay()

    print(f"Using delay of {delay} seconds")

    while True:
        print("LED ON")
        GPIO.output(LedPin, GPIO.LOW)
        time.sleep(delay)

        print("LED OFF")
        GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(delay)

def destroy():
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()