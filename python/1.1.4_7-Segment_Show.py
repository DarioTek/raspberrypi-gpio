#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

# Set up pins
SDI   = 17
RCLK  = 18
SRCLK = 27

# Define a segment code from 0 to F in Hexadecimal (Common cathode)
segCode = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f, 0x77, 0x7c, 0x39, 0x5e, 0x79, 0x71]

# Extended character map for common marquee characters on a 7-segment display
char_map = {
    '0': 0x3F, '1': 0x06, '2': 0x5B, '3': 0x4F,
    '4': 0x66, '5': 0x6D, '6': 0x7D, '7': 0x07,
    '8': 0x7F, '9': 0x6F, 'A': 0x77, 'B': 0x7C,
    'C': 0x39, 'D': 0x5E, 'E': 0x79, 'F': 0x71,
    'H': 0x76, 'I': 0x30, 'L': 0x38, 'N': 0x54,
    'O': 0x3F, 'P': 0x73, 'R': 0x50, 'S': 0x6D,
    'T': 0x78, 'U': 0x3E, 'Y': 0x6E, ' ': 0x00
}

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SDI, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(RCLK, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(SRCLK, GPIO.OUT, initial=GPIO.LOW)

# Shift the data to 74HC595
def hc595_shift(dat):
    for bit in range(0, 8): 
        GPIO.output(SDI, 0x80 & (dat << bit))
        GPIO.output(SRCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(RCLK, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(RCLK, GPIO.LOW)

def run_counter():
    print("\n[Running Hex Counter 0-F]")
    print("Tip: Press Ctrl+C at any time to return to the main menu.\n")
    try:
        while True:
            for code in segCode:
                hc595_shift(code)
                print(f"segCode: 0x{code:02X}")
                time.sleep(0.5)
    except KeyboardInterrupt:
        hc595_shift(0x00) # Clear display on exit
        print("\nReturning to main menu...\n")

def run_marquee():
    text = input("\nEnter the marquee text to display (e.g., HELP, OPEN): ").upper()
    print(f"\n[Displaying Marquee: '{text}']")
    print("Tip: Press Ctrl+C at any time to return to the main menu.\n")
    
    try:
        while True:
            for char in text:
                # Fallback to '0' (0x3F) if the character isn't in our map
                code = char_map.get(char, 0x3F)
                hc595_shift(code)
                print(f"Character: '{char}' (0x{code:02X})")
                time.sleep(0.8)
            time.sleep(1.0) # Pause before repeating the message
    except KeyboardInterrupt:
        hc595_shift(0x00) # Clear display on exit
        print("\nReturning to main menu...\n")

def main():
    while True:
        print("==============================")
        print("   7-SEGMENT DISPLAY MENU     ")
        print("==============================")
        print("1. Hex Counter (0 to F)")
        print("2. Custom Message Marquee")
        print("3. Quit")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            run_counter()
        elif choice == '2':
            run_marquee()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

def destroy():
    hc595_shift(0x00) # Clear display before cleanup
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()