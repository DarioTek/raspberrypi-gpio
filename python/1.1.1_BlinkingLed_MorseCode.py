#!/usr/bin/env python3

##
# Morse Timing Rules
# Dot (.) = 1 unit (0.2 seconds)
# Dash (-) = 3 units (0.6 seconds)
# Gap between symbols = 1 unit
# Gap between letters = 3 units
# Gap between words = 7 units
##

import RPi.GPIO as GPIO
import time

LED_PIN = 17

# Morse code dictionary
MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

UNIT = 0.2  # seconds

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.HIGH)

def led_on():
    GPIO.output(LED_PIN, GPIO.LOW)

def led_off():
    GPIO.output(LED_PIN, GPIO.HIGH)

def flash_dot():
    print(".", end="", flush=True)

    led_on()
    time.sleep(UNIT)
    led_off()

    time.sleep(UNIT)

def flash_dash():
    print("-", end="", flush=True)

    led_on()
    time.sleep(UNIT * 3)
    led_off()

    time.sleep(UNIT)

def flash_letter(letter):

    morse = MORSE_CODE.get(letter)

    if not morse:
        return

    print(f" [{letter}:{morse}] ", end="", flush=True)

    for symbol in morse:

        if symbol == ".":
            flash_dot()

        elif symbol == "-":
            flash_dash()

    # Additional pause between letters
    time.sleep(UNIT * 2)

def flash_message(message):

    for char in message.upper():

        if char == " ":
            print("   /   ", end="", flush=True)

            # Word spacing
            time.sleep(UNIT * 7)
            continue

        flash_letter(char)

    print("\nDone!")

def message_to_morse(message):

    morse_words = []

    words = message.upper().split()

    for word in words:

        morse_letters = []

        for letter in word:

            if letter in MORSE_CODE:
                morse_letters.append(MORSE_CODE[letter])

        morse_words.append(" ".join(morse_letters))

    return " / ".join(morse_words)

def destroy():
    led_off()
    GPIO.cleanup()

def main():

    print("================================")
    print(" Morse Code LED Communicator")
    print("================================")
    print("Type 'quit' to exit")
    print()

    while True:

        message = input("Enter message: ")

        if message.lower() == "quit":
            break

        morse = message_to_morse(message)

        print("\nMorse Code:")
        print(morse)
        print("\nFlashing LED...\n")

        flash_message(message)

if __name__ == "__main__":

    setup()

    try:
        main()

    except KeyboardInterrupt:
        print("\nProgram stopped.")

    finally:
        destroy()