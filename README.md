A simple Python script with some basic electronics for controlling (start/stop) your Raspberry Pi Zero 2 W cooling fan without the need for spinning 24/7 at full speed.
In my case the RPi is inside on my modem-router case. I'm running the fan at +4.1VDC, this is the most quite and effective voltage for proper cooling and of course for my ears. 🙂

<img src="https://github.com/user-attachments/assets/a74d9070-f7ae-4077-a03b-647dcb066edf" width="600" height="600" />



This is a simplest version if the above are to much solderning and electronics.
You may need to add a capacitor between +5VDC RPi pin and GND. It depends on the fan you are going to use. <b>Also bear in mind the current limitations of RPi.</b>

<img src="https://github.com/user-attachments/assets/45322af2-d82c-49bf-a290-6fb0d9c5ae36" width="300" height="600" />


<b><fonsize>Prerequisites:</fontsize></b>

Ubuntu 22.04 (Didn’t test it with Ubuntu 24.04 on Rpi)
```bash
sudo apt update
sudo apt install lm-sensors
```
After the installation check if the lm-sensors can read the CPU temperature:
```bash
sensors
or 
watch sensors
```

If everything works proceed to the next step:

<mark>Install python rpi.gpio library</mark>
```bash
sudo apt install python3-rpi.gpio
```
Download the script and make it executable:
```bash
sudo chmod +x fancontrol.py
```
Run the script and test if it is working:
```bash
sudo python3 fancontrol.py
```
Let’s make a Systemd Service so every time we reboot our system it will start automatically:
```bash
sudo nano /etc/systemd/system/fancontrol.service
```
Copy and Paste the code below make the appropriate changes to the paths and save it:
```bash
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

After that execute the below commands:
```bash
sudo systemctl daemon-reload
sudo systemctl enable fancontrol.service
sudo systemclt start fancontrol.service</code>
```
Check if the Service we just created working properly:
```bash
sudo systemctl status fancontrol.py
```

And here it's my RPi Zero 2 W inside a ZTE H288A modem-router:

<img width="600" height="600" alt="Screenshot from 2025-08-27 17-53-39" src="https://github.com/user-attachments/assets/d8aec4b2-c259-44c5-ac9c-ee1d51d28f61" />
<img width="400" height="600" alt="Screenshot from 2025-08-27 17-54-54" src="https://github.com/user-attachments/assets/f88c8fb8-1437-4dd2-aac2-5149f4c4d4a1" />
<img width="500" height="500" alt="Screenshot from 2025-08-27 17-56-54" src="https://github.com/user-attachments/assets/674acf6a-7fb9-4e34-ba01-2cd6f2ccc304" />
<img width="600" height="300" alt="Screenshot from 2025-08-27 17-57-40" src="https://github.com/user-attachments/assets/e3b5be5f-381e-4972-8896-14c8d264ca2f" />
<img width="500" height="500" alt="Screenshot from 2025-08-27 17-56-15" src="https://github.com/user-attachments/assets/eae51b10-626f-4015-ba2c-afdbffac3aa4" />
