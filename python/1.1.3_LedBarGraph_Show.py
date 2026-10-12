#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import random

ledPins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]

def oddLedBarGraph():
    for i in range(5):
        j = i * 2
        GPIO.output(ledPins[j], GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(ledPins[j], GPIO.LOW)

def evenLedBarGraph():
    for i in range(5):
        j = i * 2 + 1
        GPIO.output(ledPins[j], GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(ledPins[j], GPIO.LOW)

def allLedBarGraph():
    for i in ledPins:
        GPIO.output(i, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(i, GPIO.LOW)

# Mode 1: Original sequence repeated 5 times
def mode1_sequence():
    for _ in range(5):
        oddLedBarGraph()
        time.sleep(0.3)
        evenLedBarGraph()
        time.sleep(0.3)
        allLedBarGraph()
        time.sleep(0.3)

# Mode 2: LED graph goes back and forth
def mode2_backAndForth():
    for _ in range(5):
        # Forward scan
        for pin in ledPins:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.LOW)
        # Backward scan
        for pin in reversed(ledPins):
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.LOW)

# Mode 3: Alternate LEDs light up
def mode3_alternate():
    for _ in range(5):
        # Even-indexed LEDs ON
        for i in range(0, len(ledPins), 2):
            GPIO.output(ledPins[i], GPIO.HIGH)
        time.sleep(0.3)
        for i in range(0, len(ledPins), 2):
            GPIO.output(ledPins[i], GPIO.LOW)
        
        # Odd-indexed LEDs ON
        for i in range(1, len(ledPins), 2):
            GPIO.output(ledPins[i], GPIO.HIGH)
        time.sleep(0.3)
        for i in range(1, len(ledPins), 2):
            GPIO.output(ledPins[i], GPIO.LOW)

# Mode 4: LEDs meet in the middle from the outside
def mode4_meetInMiddle():
    for _ in range(5):
        for i in range(5):
            left_pin = ledPins[i]
            right_pin = ledPins[9 - i]
            GPIO.output(left_pin, GPIO.HIGH)
            GPIO.output(right_pin, GPIO.HIGH)
            time.sleep(0.15)
            GPIO.output(left_pin, GPIO.LOW)
            GPIO.output(right_pin, GPIO.LOW)

# Mode 5: LEDs split from the middle outward
def mode5_splitFromMiddle():
    for _ in range(5):
        for i in range(4, -1, -1):
            left_pin = ledPins[i]
            right_pin = ledPins[9 - i]
            GPIO.output(left_pin, GPIO.HIGH)
            GPIO.output(right_pin, GPIO.HIGH)
            time.sleep(0.15)
            GPIO.output(left_pin, GPIO.LOW)
            GPIO.output(right_pin, GPIO.LOW)

# Mode 6: Play all modes in a random order
def mode6_randomSequence():
    modes = [
        mode1_sequence,
        mode2_backAndForth,
        mode3_alternate,
        mode4_meetInMiddle,
        mode5_splitFromMiddle
    ]
    random.shuffle(modes)
    for mode in modes:
        mode()
        time.sleep(0.5)  # Brief pause between different mode transitions

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
    for i in ledPins:
        GPIO.setup(i, GPIO.OUT)     # Set all ledPins' mode to output
        GPIO.output(i, GPIO.LOW)    # Set all ledPins to LOW to turn off LEDs

def loop():
    while True:
        print("\n==================================")
        print("       LED BAR GRAPH MENU         ")
        print("==================================")
        print("1. Mode 1: Original Sequence     (Runs 5 times)")
        print("2. Mode 2: Back & Forth Scan     (Runs 5 times)")
        print("3. Mode 3: Alternate LEDs        (Runs 5 times)")
        print("4. Mode 4: Meet in the Middle    (Runs 5 times)")
        print("5. Mode 5: Split from the Middle (Runs 5 times)")
        print("6. Mode 6: Randomized Sequence   (All modes, shuffled)")
        print("7. Quit Program")
        
        choice = input("\nSelect a mode (1-7): ").strip()
        
        if choice == '1':
            print("\n[Running Mode 1...]")
            mode1_sequence()
        elif choice == '2':
            print("\n[Running Mode 2...]")
            mode2_backAndForth()
        elif choice == '3':
            print("\n[Running Mode 3...]")
            mode3_alternate()
        elif choice == '4':
            print("\n[Running Mode 4...]")
            mode4_meetInMiddle()
        elif choice == '5':
            print("\n[Running Mode 5...]")
            mode5_splitFromMiddle()
        elif choice == '6':
            print("\n[Running Mode 6 (Random Shuffle)...]")
            mode6_randomSequence()
        elif choice == '7':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 7.")

def destroy():
    for pin in ledPins:
        GPIO.output(pin, GPIO.LOW)    # Turn off all LEDs
    GPIO.cleanup()                    # Release resources

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
    finally:
        destroy()