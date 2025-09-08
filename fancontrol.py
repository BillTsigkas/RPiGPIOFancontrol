#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO
import subprocess

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT) # You can choose another GPIO pin if you like, I chose Pin 26 for practical reasons in my setup.

# Reading CPU temperature using vcgencmd
def read_cpu_temp():
    out = subprocess.check_output(["vcgencmd", "measure_temp"], text=True)
    temp_str = out.split('=')[1].strip()  
    return float(temp_str.rstrip("'C"))  

try:
    while True:
        cpu_temp = read_cpu_temp()
        print(f"CPU Temperature: {cpu_temp} °C")

        if cpu_temp >= 57:              # Fan starts at >=57 Celsius ***You can change this value***
            GPIO.output(26, GPIO.HIGH)  # Set GPIO 26 high
        elif cpu_temp <= 51:            # Fan stops at <=51 Celsius ***You can also change this value***
            GPIO.output(26, GPIO.LOW)   # Set GPIO 26 low

        time.sleep(20)  # Polling interval, temprature check every 20 seconds

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
