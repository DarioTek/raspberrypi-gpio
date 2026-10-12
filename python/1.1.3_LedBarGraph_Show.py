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
        for pin in ledPins:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.LOW)
        for pin in reversed(ledPins):
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.LOW)

# Mode 3: Alternate LEDs light up
def mode3_alternate():
    for _ in range(5):
        for i in range(0, len(ledPins), 2):
            GPIO.output(ledPins[i], GPIO.HIGH)
        time.sleep(0.3)
        for i in range(0, len(ledPins), 2):
            GPIO.output(ledPins[i], GPIO.LOW)
        
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

# Mode 6: Fill & Drain (Stacker)
def mode6_fillAndDrain():
    for _ in range(5):
        # Fill up
        for i in range(len(ledPins)):
            for j in range(len(ledPins) - i):
                GPIO.output(ledPins[j], GPIO.HIGH)
                time.sleep(0.02)
                GPIO.output(ledPins[j], GPIO.LOW)
            GPIO.output(ledPins[len(ledPins) - 1 - i], GPIO.HIGH) # Lock in place
        # Drain down
        for i in range(len(ledPins)):
            GPIO.output(ledPins[i], GPIO.LOW)
            time.sleep(0.04)

# Mode 7: Bounce / Pendulum Decay
def mode7_bounceDecay():
    for _ in range(5):
        low, high = 0, len(ledPins) - 1
        while low <= high:
            for i in range(low, high + 1):
                GPIO.output(ledPins[i], GPIO.HIGH)
                time.sleep(0.04)
                GPIO.output(ledPins[i], GPIO.LOW)
            high -= 1
            if low > high:
                break
            for i in range(high, low - 1, -1):
                GPIO.output(ledPins[i], GPIO.HIGH)
                time.sleep(0.04)
                GPIO.output(ledPins[i], GPIO.LOW)
            low += 1
        time.sleep(0.2)

# Mode 8: Binary Counter (0 to 31 sequence)
def mode8_binaryCounter():
    for _ in range(5):
        for val in range(32):
            for i in range(len(ledPins)):
                if (val >> i) & 1:
                    GPIO.output(ledPins[i], GPIO.HIGH)
                else:
                    GPIO.output(ledPins[i], GPIO.LOW)
            time.sleep(0.08)
        for pin in ledPins:
            GPIO.output(pin, GPIO.LOW)

# Mode 9: Ripple / Wave (Expands & contracts from center)
def mode9_rippleWave():
    for _ in range(5):
        pairs = [(4, 5), (3, 6), (2, 7), (1, 8), (0, 9)]
        for c1, c2 in pairs:
            GPIO.output(ledPins[c1], GPIO.HIGH)
            GPIO.output(ledPins[c2], GPIO.HIGH)
            time.sleep(0.08)
            GPIO.output(ledPins[c1], GPIO.LOW)
            GPIO.output(ledPins[c2], GPIO.LOW)
        for c1, c2 in reversed(pairs):
            GPIO.output(ledPins[c1], GPIO.HIGH)
            GPIO.output(ledPins[c2], GPIO.HIGH)
            time.sleep(0.08)
            GPIO.output(ledPins[c1], GPIO.LOW)
            GPIO.output(ledPins[c2], GPIO.LOW)

# Mode 10: Running Segment (Block of 3 moving back and forth)
def mode10_runningSegment():
    block_size = 3
    for _ in range(5):
        for i in range(len(ledPins) - block_size + 1):
            for b in range(block_size):
                GPIO.output(ledPins[i + b], GPIO.HIGH)
            time.sleep(0.08)
            for b in range(block_size):
                GPIO.output(ledPins[i + b], GPIO.LOW)
        for i in range(len(ledPins) - block_size, -1, -1):
            for b in range(block_size):
                GPIO.output(ledPins[i + b], GPIO.HIGH)
            time.sleep(0.08)
            for b in range(block_size):
                GPIO.output(ledPins[i + b], GPIO.LOW)

# Mode 11: Random Strobe / Sparkle
def mode11_randomStrobe():
    for _ in range(5):
        for _ in range(25):
            active_pins = random.sample(ledPins, 2)
            for p in active_pins:
                GPIO.output(p, GPIO.HIGH)
            time.sleep(0.05)
            for p in active_pins:
                GPIO.output(p, GPIO.LOW)
        time.sleep(0.1)

# Mode 12: Inward Drain / Compression
def mode12_inwardDrain():
    for _ in range(5):
        for pin in ledPins:
            GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.2)
        for i in range(5):
            GPIO.output(ledPins[i], GPIO.LOW)
            GPIO.output(ledPins[9 - i], GPIO.LOW)
            time.sleep(0.08)
        time.sleep(0.1)
        for i in range(4, -1, -1):
            GPIO.output(ledPins[i], GPIO.HIGH)
            GPIO.output(ledPins[9 - i], GPIO.HIGH)
            time.sleep(0.08)
        time.sleep(0.2)
        for pin in ledPins:
            GPIO.output(pin, GPIO.LOW)

# Mode 13: Play all modes in a randomized order
def mode13_randomSequence():
    modes = [
        mode1_sequence, mode2_backAndForth, mode3_alternate,
        mode4_meetInMiddle, mode5_splitFromMiddle, mode6_fillAndDrain,
        mode7_bounceDecay, mode8_binaryCounter, mode9_rippleWave,
        mode10_runningSegment, mode11_randomStrobe, mode12_inwardDrain
    ]
    random.shuffle(modes)
    for mode in modes:
        mode()
        time.sleep(0.3)

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
    for i in ledPins:
        GPIO.setup(i, GPIO.OUT)     # Set all ledPins to output
        GPIO.output(i, GPIO.LOW)    # Set all ledPins to LOW to turn off LEDs

def loop():
    while True:
        print("\n========================================")
        print("          LED BAR GRAPH MENU            ")
        print("========================================")
        print(" 1. Mode 1: Original Sequence         (5x)")
        print(" 2. Mode 2: Back & Forth Scan         (5x)")
        print(" 3. Mode 3: Alternate LEDs            (5x)")
        print(" 4. Mode 4: Meet in the Middle        (5x)")
        print(" 5. Mode 5: Split from the Middle     (5x)")
        print(" 6. Mode 6: Fill & Drain (Stacker)    (5x)")
        print(" 7. Mode 7: Bounce / Pendulum Decay   (5x)")
        print(" 8. Mode 8: Binary Counter            (5x)")
        print(" 9. Mode 9: Ripple / Wave             (5x)")
        print("10. Mode 10: Running Segment          (5x)")
        print("11. Mode 11: Random Strobe / Sparkle  (5x)")
        print("12. Mode 12: Inward Drain             (5x)")
        print("13. Mode 13: Randomized Shuffle       (All)")
        print("14. Quit Program")
        
        choice = input("\nSelect a mode (1-14): ").strip()
        
        modes_map = {
            '1': (mode1_sequence, "Mode 1"),
            '2': (mode2_backAndForth, "Mode 2"),
            '3': (mode3_alternate, "Mode 3"),
            '4': (mode4_meetInMiddle, "Mode 4"),
            '5': (mode5_splitFromMiddle, "Mode 5"),
            '6': (mode6_fillAndDrain, "Mode 6"),
            '7': (mode7_bounceDecay, "Mode 7"),
            '8': (mode8_binaryCounter, "Mode 8"),
            '9': (mode9_rippleWave, "Mode 9"),
            '10': (mode10_runningSegment, "Mode 10"),
            '11': (mode11_randomStrobe, "Mode 11"),
            '12': (mode12_inwardDrain, "Mode 12"),
            '13': (mode13_randomSequence, "Mode 13 (Random Shuffle)")
        }
        
        if choice in modes_map:
            func, name = modes_map[choice]
            print(f"\n[Running {name}...]press Ctrl+C to stop early if needed.")
            func()
        elif choice == '14':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 14.")

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