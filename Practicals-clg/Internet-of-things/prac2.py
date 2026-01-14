#Practical 4: Pattern LED Blink

import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define LED pins
led_pins = [18, 23, 24, 25]

# Set LED pins as output
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        time.sleep(0.2)
        print("LED ON")
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(25, GPIO.HIGH)

        time.sleep(0.2)
        print("LED OFF")
        GPIO.output(18, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)

        time.sleep(0.2)
        print("LED ON")
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(25, GPIO.LOW)

        time.sleep(0.2)
        print("LED OFF")
        GPIO.output(18, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.HIGH)

except KeyboardInterrupt:
    print("Exiting... Cleaning up GPIO")
    GPIO.cleanup()
