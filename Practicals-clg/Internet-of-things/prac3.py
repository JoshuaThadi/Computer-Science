#Practical 5: DC Motor Controller

import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define Motor control pins
IN1 = 23  # Motor direction control
IN2 = 24  # Motor direction control
ENA = 25  # Enable pin

# Setup GPIO pins
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

# Enable motor
GPIO.output(ENA, GPIO.HIGH)

# Define motor control functions
def motor_forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

def motor_backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

def motor_stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

# Run Motor
try:
    print("Motor Forward")
    motor_forward()
    time.sleep(2)

    print("Motor Backward")
    motor_backward()
    time.sleep(2)

    print("Stopping Motor")
    motor_stop()

except KeyboardInterrupt:
    print("\nProcess interrupted!")

finally:
    GPIO.cleanup()  # Cleanup GPIO to prevent pin locking
    print("GPIO")