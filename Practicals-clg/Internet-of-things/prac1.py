#Practical 3: Simple LED Blink

import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the LED pin
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

# Blink LED
try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED ON
        time.sleep(1)  # Wait 1 second
        GPIO.output(LED_PIN, GPIO.LOW)   # Turn LED OFF
        time.sleep(1)  # Wait 1 second

except KeyboardInterrupt:
    GPIO.cleanup()  # Reset GPIO on exit
