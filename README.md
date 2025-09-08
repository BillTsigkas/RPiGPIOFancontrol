A simple Python script with some basic electronics for controlling (start/stop) your Raspberry Pi Zero 2 W cooling fan without the need for spinning 24/7 at full speed.
In my case, I have placed the RPi inside my modem-router, so the need for proper cooling is important. I'm using a 30mm 5VDC fan running at 4V, this is the most quite (for my ears) and effective voltage for proper cooling (summers are really hot in Greece).

<img src="https://github.com/user-attachments/assets/a74d9070-f7ae-4077-a03b-647dcb066edf" width="600" height="600" />



This is a simplest version if the above are to much solderning and electronics.
It's not necessary but if you'll see ripple you may need to add a capacitor between +5V RPi pin and GND.<br>
<b>Check the limitations of your transistor in datasheet, for both cases with or without using a voltage regulator.</b><br>
<b>Also bear in mind the current limitations of RPi +5V pin. Avoid to use a very powerful and power-hungry fan.</b>

<img src="https://github.com/user-attachments/assets/45322af2-d82c-49bf-a290-6fb0d9c5ae36" width="300" height="600" />

## Prerequirements

<b>Ubuntu 22.04 (I haven't tested it with Ubuntu 24.04)</b><br>
<b>Python3</b><br>
<b>RPi.GPIO Library</b>

Let's check first if you can read RPi temperature properly:
```ini
vcgencmd measure_temp
```
You will get an answer like this:
```ini
temp=52.6'C
```

Now let's begin the installanion:

```ini
sudo apt update && sudo apt upgrade
sudo apt install python3
sudo apt install python3-rpi.gpio
```

## Download the script and make it executable

```ini
sudo chmod +x fancontrol.py
```

Run the script to test if it's working:
```ini
./fancontrol.py
```

## Let’s make a Systemd Service so every time we reboot our system it will start automatically

```ini
sudo nano /etc/systemd/system/fancontrol.service
```

Copy and Paste inside the code below make the appropriate changes to the paths and save it:

```ini
[Unit]
Description=Fan Control Service
After=multi-user.target

[Service]
ExecStart=/usr/bin/python3 /home/your_username/RPiGPIOFancontrol-main/fancontrol.py #path to your script
WorkingDirectory=/home/your_username/RPiGPIOFancontrol-main #path to RPiGPIOFancontrol-main directory
StandardOutput=journal
StandardError=journal
Restart=always
User=your_username

[Install]
WantedBy=multi-user.target
```

After these execute the commands below:

```ini
sudo systemctl daemon-reload
sudo systemctl enable fancontrol.service
sudo systemclt start fancontrol.service
```
Check if the Service we just created working properly:

```ini
sudo systemctl status fancontrol.service
```
### ***If you want to change the temprature threshold limits you can open the script with your favorite text editor and change the temprature values to whatever serves your needs.***

## Here it's my RPi Zero 2 W inside a ZTE H288A modem-router:

<img width="600" height="600" alt="Screenshot from 2025-08-27 17-53-39" src="https://github.com/user-attachments/assets/d8aec4b2-c259-44c5-ac9c-ee1d51d28f61" />
<img width="400" height="600" alt="Screenshot from 2025-08-27 17-54-54" src="https://github.com/user-attachments/assets/f88c8fb8-1437-4dd2-aac2-5149f4c4d4a1" />
<img width="500" height="500" alt="Screenshot from 2025-08-27 17-56-54" src="https://github.com/user-attachments/assets/674acf6a-7fb9-4e34-ba01-2cd6f2ccc304" />
<img width="600" height="300" alt="Screenshot from 2025-08-27 17-57-40" src="https://github.com/user-attachments/assets/e3b5be5f-381e-4972-8896-14c8d264ca2f" />
<img width="500" height="500" alt="Screenshot from 2025-08-27 17-56-15" src="https://github.com/user-attachments/assets/eae51b10-626f-4015-ba2c-afdbffac3aa4" />

PS. We can make some code changes and use a software PWM frequency of 1kHz so we can make a duty cycle and control our fan speed but this is another story and 1kHz is really low for this kind of job.
