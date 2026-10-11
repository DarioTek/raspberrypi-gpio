#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import random

LED_PIN = 17

# ----------------------
# Setup
# ----------------------

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.HIGH)

# LED on/off helpers (active-low LED)
def led_on():
    GPIO.output(LED_PIN, GPIO.LOW)

def led_off():
    GPIO.output(LED_PIN, GPIO.HIGH)

# ----------------------
# Dance Moves
# ----------------------

def slow_blink():
    print("Slow Blink")
    for _ in range(10):
        led_on()
        time.sleep(1)
        led_off()
        time.sleep(1)

def heartbeat():
    print("Heartbeat")

    for _ in range(5):
        led_on()
        time.sleep(0.2)

        led_off()
        time.sleep(0.2)

        led_on()
        time.sleep(0.2)

        led_off()
        time.sleep(1.0)

def disco():
    print("Disco")

    for _ in range(5):
        for _ in range(10):
            led_on()
            time.sleep(0.05)

            led_off()
            time.sleep(0.05)

        time.sleep(0.5)

def dot():
    led_on()
    time.sleep(0.2)
    led_off()
    time.sleep(0.2)

def dash():
    led_on()
    time.sleep(0.6)
    led_off()
    time.sleep(0.2)

def sos():
    print("SOS")

    for _ in range(3):
        dot()
    for _ in range(3):
        dash()
    for _ in range(3):
        dot()

    time.sleep(1)

def random_dance():
    print("Random Dance")

    for _ in range(random.randint(10, 30)):
        led_on()
        time.sleep(random.uniform(0.05, 0.5))

        led_off()
        time.sleep(random.uniform(0.05, 0.5))

def firefly():
    print("Firefly")

    for _ in range(20):
        led_on()
        time.sleep(random.uniform(0.05, 0.2))

        led_off()
        time.sleep(random.uniform(1.0, 3.0))

def breathing():
    print("Breathing")

    pwm = GPIO.PWM(LED_PIN, 100)
    pwm.start(100)  # active-low LED

    try:
        for _ in range(3):

            # fade in
            for dc in range(100, -1, -2):
                pwm.ChangeDutyCycle(dc)
                time.sleep(0.03)

            # fade out
            for dc in range(0, 101, 2):
                pwm.ChangeDutyCycle(dc)
                time.sleep(0.03)

    finally:
        pwm.stop()
        led_off()

def fireworks():
    print("Fireworks!")

    for show in range(5):

        print(f"Launching firework #{show + 1}")

        # Launch effect
        for delay in [0.30, 0.25, 0.20, 0.15, 0.10]:
            led_on()
            time.sleep(delay)
            led_off()
            time.sleep(delay)

        # Pause at the top before explosion
        time.sleep(0.3)

        print("BOOM!")

        # Explosion effect
        for _ in range(random.randint(15, 30)):
            led_on()
            time.sleep(random.uniform(0.01, 0.05))
            led_off()
            time.sleep(random.uniform(0.01, 0.05))

        # Sparkle effect
        for _ in range(random.randint(10, 20)):
            led_on()
            time.sleep(random.uniform(0.03, 0.10))
            led_off()
            time.sleep(random.uniform(0.05, 0.25))

        # Wait before next firework
        time.sleep(random.uniform(1.0, 2.0))

    print("GRAND FINALE!")

    for _ in range(100):
        led_on()
        time.sleep(0.02)
        led_off()
        time.sleep(0.02)

    time.sleep(1)        

def dance_party():
    print("Dance Party!")

    moves = [
        heartbeat,
        disco,
        random_dance,
        firefly,
        breathing,
        fireworks
    ]

    for _ in range(5):
        move = random.choice(moves)
        move()

# ----------------------
# Menu
# ----------------------

def show_menu():
    print("\n========================")
    print(" LED DANCE FLOOR ")
    print("========================")
    print("1 - Slow Blink")
    print("2 - Heartbeat")
    print("3 - Disco")
    print("4 - SOS")
    print("5 - Random Dance")
    print("6 - Firefly")
    print("7 - Breathing")
    print("8 - Dance Party")
    print("9 - Fireworks")
    print("0 - Exit")
    print("========================")

def main():
    while True:
        show_menu()

        choice = input("Select a dance move: ").strip()

        if choice == "1":
            slow_blink()

        elif choice == "2":
            heartbeat()

        elif choice == "3":
            disco()

        elif choice == "4":
            sos()

        elif choice == "5":
            random_dance()

        elif choice == "6":
            firefly()

        elif choice == "7":
            breathing()

        elif choice == "8":
            dance_party()

        elif choice == "9":
            fireworks()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid selection.")

# ----------------------
# Cleanup
# ----------------------

def destroy():
    led_off()
    GPIO.cleanup()

if __name__ == '__main__':
    setup()

    try:
        main()

    except KeyboardInterrupt:
        print("\nStopping...")

    finally:
        destroy()