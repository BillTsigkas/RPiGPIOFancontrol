import time
import os
import RPi.GPIO as GPIO

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

# Function to read CPU temperature
def read_cpu_temp():
    # Reading the output of the sensors command
    temp_output = os.popen("sensors | grep 'temp1'").read()
    # Extract the temperature value
    # Example output: "temp1:        +57.3°C"
    temp_str = temp_output.split()[1]  # Getting the temperature string
    temp = float(temp_str[:-2])  # Remove the last two characters ('°C') and convert to float
    return temp

try:
    while True:
        cpu_temp = read_cpu_temp()
        print(f"CPU Temperature: {cpu_temp} °C")

        if cpu_temp >= 57:  # You can change this temp value to whatever you want. Above this temp the fan will start.
            GPIO.output(26, GPIO.HIGH)  # Set GPIO 26 high
        elif cpu_temp <= 51:  # You can also change this value. Below this temp number the fan will stop.
            GPIO.output(26, GPIO.LOW)   # Set GPIO 26 low

        time.sleep(20)  # Poll interval in seconds. Checking every 20 seconds. You can change it as well.

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()  # Clean up GPIO settings
