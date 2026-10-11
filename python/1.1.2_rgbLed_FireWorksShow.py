#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import random

# Set pins' channels with dictionary
pins = {
    'Red': 17,
    'Green': 18,
    'Blue': 27
}

# --------------------------------------------------
# SETUP
# --------------------------------------------------

def setup():
    global p_R, p_G, p_B

    GPIO.setmode(GPIO.BCM)

    for pin in pins.values():
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)

    p_R = GPIO.PWM(pins['Red'], 2000)
    p_G = GPIO.PWM(pins['Green'], 2000)
    p_B = GPIO.PWM(pins['Blue'], 2000)

    p_R.start(0)
    p_G.start(0)
    p_B.start(0)

# --------------------------------------------------
# RGB HELPERS
# --------------------------------------------------

def MAP(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / \
           (in_max - in_min) + out_min

def setColor(color):

    R_val = (color & 0xFF0000) >> 16
    G_val = (color & 0x00FF00) >> 8
    B_val = (color & 0x0000FF)

    R_val = MAP(R_val, 0, 255, 0, 100)
    G_val = MAP(G_val, 0, 255, 0, 100)
    B_val = MAP(B_val, 0, 255, 0, 100)

    p_R.ChangeDutyCycle(R_val)
    p_G.ChangeDutyCycle(G_val)
    p_B.ChangeDutyCycle(B_val)

def off():
    setColor(0x000000)

def flash(color, on_time, off_time=0.02):

    setColor(color)
    time.sleep(on_time)

    off()
    time.sleep(off_time)

def random_color():

    r = random.randint(50, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)

    return (r << 16) | (g << 8) | b

def launch():

    for delay in [0.25, 0.20, 0.15, 0.10, 0.05]:

        flash(0xFFFFFF, delay, delay / 2)

# --------------------------------------------------
# FIREWORK STYLES
# --------------------------------------------------

def red_rocket():

    print("🎆 Red Rocket")

    launch()

    for _ in range(30):
        flash(0xFF0000, 0.03)

def rainbow_burst():

    print("🌈 Rainbow Burst")

    launch()

    for _ in range(40):
        flash(random_color(), 0.04)

def golden_sparkler():

    print("✨ Golden Sparkler")

    launch()

    for _ in range(60):
        flash(0xFFD700, random.uniform(0.01, 0.08))

def rapid_fire_finale():

    print("💣 Rapid-Fire Finale")

    for _ in range(150):
        flash(random_color(), 0.01, 0.01)

def galaxy_fireworks():

    print("🌌 Galaxy Fireworks")

    colors = [
        0x8A2BE2,
        0x9400D3,
        0x00FFFF,
        0x4B0082,
        0xFF00FF
    ]

    launch()

    for _ in range(50):
        flash(
            random.choice(colors),
            random.uniform(0.02, 0.08)
        )

def christmas_fireworks():

    print("🎄 Christmas Fireworks")

    launch()

    for _ in range(40):

        flash(0xFF0000, 0.04)
        flash(0x00FF00, 0.04)

def random_show():

    print("🎲 Random Fireworks Show")

    shows = [
        red_rocket,
        rainbow_burst,
        golden_sparkler,
        galaxy_fireworks,
        christmas_fireworks
    ]

    for _ in range(5):

        random.choice(shows)()

        time.sleep(1)

    rapid_fire_finale()

def countdown():

    print("\nLaunching in...")

    for i in range(3, 0, -1):

        print(i)

        setColor(0xFFFFFF)
        time.sleep(0.5)

        off()
        time.sleep(0.5)

    print("BOOM!")

def independence_day_show():

    print("🇺🇸 Independence Day Spectacular")

    countdown()

    red_rocket()
    time.sleep(1)

    rainbow_burst()
    time.sleep(1)

    galaxy_fireworks()
    time.sleep(1)

    golden_sparkler()
    time.sleep(1)

    rapid_fire_finale()

def ocean_fireworks():

    print("🌊 Ocean Fireworks")

    colors = [
        0x0000FF,
        0x00BFFF,
        0x00FFFF,
        0x1E90FF
    ]

    for _ in range(75):

        setColor(random.choice(colors))
        time.sleep(0.08)

        off()
        time.sleep(0.02)

def firestorm():

    print("🔥 Firestorm")

    colors = [
        0xFF0000,
        0xFF4500,
        0xFFA500,
        0xFFFF00
    ]

    launch()

    for _ in range(100):

        flash(
            random.choice(colors),
            random.uniform(0.01, 0.04),
            0.01
        )

def unicorn_explosion():

    print("🦄 Unicorn Explosion")

    colors = [
        0xFF69B4,
        0xFF00FF,
        0x9370DB,
        0x00FFFF,
        0xBA55D3
    ]

    launch()

    for _ in range(75):

        flash(
            random.choice(colors),
            random.uniform(0.02, 0.06)
        )

def color_fade_show():

    print("🌈 Color Fade Show")

    colors = [
        0xFF0000,
        0x00FF00,
        0x0000FF,
        0xFFFF00,
        0xFF00FF,
        0x00FFFF
    ]

    for color in colors:

        setColor(color)
        time.sleep(1)

    off()

def lightning_storm():

    print("⚡ Lightning Storm")

    for _ in range(50):

        flashes = random.randint(1, 4)

        for _ in range(flashes):

            flash(0xFFFFFF, 0.03, 0.03)

        time.sleep(random.uniform(0.2, 1.5))

def mega_grand_finale():

    print("🎆 MEGA GRAND FINALE")

    colors = [
        0xFF0000,
        0x00FF00,
        0x0000FF,
        0xFFFF00,
        0xFF00FF,
        0x00FFFF,
        0xFFFFFF
    ]

    for _ in range(500):

        setColor(random.choice(colors))
        time.sleep(0.01)

    off()

def new_years_show():

    print("🎉 HAPPY NEW YEAR SHOW")

    countdown()

    ocean_fireworks()
    galaxy_fireworks()
    unicorn_explosion()
    firestorm()
    rapid_fire_finale()
    mega_grand_finale()

# --------------------------------------------------
# MENU
# --------------------------------------------------

def show_menu():

    print("\n====================================")
    print(" RGB LED FIREWORKS CONTROLLER ")
    print("====================================")
    print("1  - Red Rocket")
    print("2  - Rainbow Burst")
    print("3  - Golden Sparkler")
    print("4  - Rapid-Fire Finale")
    print("5  - Galaxy Fireworks")
    print("6  - Christmas Fireworks")
    print("7  - Random Fireworks Show")
    print("8  - Independence Day Spectacular")
    print("9  - Ocean Fireworks")
    print("10 - Firestorm")
    print("11 - Unicorn Explosion")
    print("12 - Color Fade Show")
    print("13 - Lightning Storm")
    print("14 - Mega Grand Finale")
    print("15 - New Year's Show")
    print("16 - Exit")
    print("====================================")

# --------------------------------------------------
# MAIN LOOP
# --------------------------------------------------

def main():

    while True:

        show_menu()

        choice = input("Choose a fireworks style: ").strip()

        if choice == "1":
            red_rocket()

        elif choice == "2":
            rainbow_burst()

        elif choice == "3":
            golden_sparkler()

        elif choice == "4":
            rapid_fire_finale()

        elif choice == "5":
            galaxy_fireworks()

        elif choice == "6":
            christmas_fireworks()

        elif choice == "7":
            random_show()

        elif choice == "8":
            independence_day_show()

        elif choice == "9":
            ocean_fireworks()

        elif choice == "10":
            firestorm()

        elif choice == "11":
            unicorn_explosion()

        elif choice == "12":
            color_fade_show()

        elif choice == "13":
            lightning_storm()

        elif choice == "14":
            mega_grand_finale()

        elif choice == "15":
            new_years_show()

        elif choice == "16":
            print("Goodbye!")
            break

        else:
            print("Invalid selection")

# --------------------------------------------------
# CLEANUP
# --------------------------------------------------

def destroy():

    off()

    p_R.stop()
    p_G.stop()
    p_B.stop()

    GPIO.cleanup()

# --------------------------------------------------
# START PROGRAM
# --------------------------------------------------

if __name__ == '__main__':

    setup()

    try:
        main()

    except KeyboardInterrupt:
        print("\nStopping fireworks show...")

    finally:
        destroy()