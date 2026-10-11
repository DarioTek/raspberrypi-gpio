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

def flash_dot(show_output=True):

    if show_output:
        print(".", end="", flush=True)

    led_on()
    time.sleep(UNIT)
    led_off()

    time.sleep(UNIT)

def flash_dash(show_output=True):

    if show_output:
        print("-", end="", flush=True)

    led_on()
    time.sleep(UNIT * 3)
    led_off()

    time.sleep(UNIT)

def flash_letter(letter, secret_mode=False):

    morse = MORSE_CODE.get(letter)

    if not morse:
        return

    if not secret_mode:
        print(f" [{letter}:{morse}] ", end="", flush=True)

    for symbol in morse:

        if symbol == ".":
            flash_dot(not secret_mode)

        elif symbol == "-":
            flash_dash(not secret_mode)

    # Additional pause between letters
    time.sleep(UNIT * 2)

def flash_message(message, secret_mode=False):

    for char in message.upper():

        if char == " ":

            if not secret_mode:
                print("   /   ", end="", flush=True)

            # Word spacing
            time.sleep(UNIT * 7)
            continue

        flash_letter(char, secret_mode)

    if not secret_mode:
        print("\nDone!")
    else:
        print("\nTransmission complete.")

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

        print("\nSelect Mode")
        print("1 - Normal Mode")
        print("2 - Secret Agent Mode")

        mode = input("Choice: ").strip()

        secret_mode = (mode == "2")

        if secret_mode:
            print("\n*** SECRET AGENT MODE ACTIVATED ***")
            print("Message and Morse code will NOT be displayed.")
        else:
            print("\nNormal Mode")

        message = input("\nEnter message: ")

        if message.lower() == "quit":
            break

        if secret_mode:

            print("\nTransmitting classified message...")
            flash_message(message, secret_mode=True)

        else:

            morse = message_to_morse(message)

            print("\nMorse Code:")
            print(morse)
            print("\nFlashing LED...\n")

            flash_message(message, secret_mode=False)


if __name__ == "__main__":

    setup()

    try:
        main()

    except KeyboardInterrupt:
        print("\nProgram stopped.")

    finally:
        destroy()