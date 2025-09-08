import time
import RPi.GPIO as GPIO
import subprocess

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

# Function to read CPU temperature
def read_cpu_temp():
    out = subprocess.check_output(["sensors"], text=True)
    for line in out.splitlines():
        if "temp1" in line:
            temp_str = line.split()[1]   # "+57.3°C"
            return float(temp_str.rstrip("°C+"))
    raise RuntimeError("temp1 not found")

try:
    while True:
        cpu_temp = read_cpu_temp()
        print(f"CPU Temperature: {cpu_temp} °C")

        if cpu_temp >= 57:
            GPIO.output(26, GPIO.HIGH)  # Set GPIO 26 high
        elif cpu_temp <= 51:
            GPIO.output(26, GPIO.LOW)   # Set GPIO 26 low

        time.sleep(20)  # Wait for 20 seconds

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()  # Clean up GPIO settings
