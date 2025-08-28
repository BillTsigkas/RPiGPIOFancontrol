A simple Python script with some basic electronics for controlling (start/stop) your Raspberry Pi Zero 2 W cooling fan without the need for spinning 24/7 at full speed.
In my case the RPi handles a PiHole+PiVPN and my car's server alarm.

<img width="726" height="797" alt="Screenshot from 2025-08-27 17-16-20" src="https://github.com/user-attachments/assets/aa3be717-b1b4-4ac1-a913-30df4a9cef4c" />



This is a simplest version if the above are to much solderning and electronics. 🙂
It's better to add a decoupling capacitor between +5v RPi power pin and GND.

<img width="461" height="784" alt="Screenshot from 2025-08-27 17-20-58" src="https://github.com/user-attachments/assets/977d4394-85fe-4c90-904e-94c24eac37ad" />

<b><mark>Dependencies:</mark></b>

Ubuntu 22.04 (Didn’t test it with Ubuntu 24.04 on Rpi)

<code>sudo apt update</code>

<code>sudo apt install lm-sensors</code>

After the installation check if the lm-sensors can read the CPU temperature:

<code>sensors</code>
or 
<code>watch sensors</code>


If everything works proceed to the next step:

<mark>Install python rpi.gpio library</mark>

<code>sudo apt install python3-rpi.gpio</code>

Download the script and make it executable:

<code>sudo chmod +x fancontrol.py</code>

Run the script and test it if it works:

<code>sudo python3 fancontrol.py</code>

Let’s make a Systemd Service so every time we reboot it will start automatically:

<code>sudo nano /etc/systemd/system/fancontrol.service</code>

<mark>Copy and Paste the below:</mark>

<code>[Unit]
Description=Fan Control Service
After=multi-user.target</code>

<code>[Service]
ExecStart=/usr/bin/python3 /home/your_username/fancontrol.py #path to your script
WorkingDirectory=/home/Bill/fancontrol
StandardOutput=journal
StandardError=journal
Restart=always
User=your_username</code>

<code>[Install]
WantedBy=multi-user.target</code>


<code>sudo systemctl daemon-reload
sudo systemctl enable fancontrol.service
sudo systemclt start fancontrol.service</code>

Check if the Service we just created working properly:

<code>sudo systemctl status fancontrol.py</code>


And here it's my RPi Zero 2 W inside a ZTE H288A modem-router.
I always loved compact desing.

<img width="960" height="846" alt="Screenshot from 2025-08-27 17-53-39" src="https://github.com/user-attachments/assets/d8aec4b2-c259-44c5-ac9c-ee1d51d28f61" />
<img width="641" height="837" alt="Screenshot from 2025-08-27 17-54-54" src="https://github.com/user-attachments/assets/f88c8fb8-1437-4dd2-aac2-5149f4c4d4a1" />
<img width="552" height="496" alt="Screenshot from 2025-08-27 17-56-54" src="https://github.com/user-attachments/assets/674acf6a-7fb9-4e34-ba01-2cd6f2ccc304" />
<img width="1141" height="715" alt="Screenshot from 2025-08-27 17-57-40" src="https://github.com/user-attachments/assets/e3b5be5f-381e-4972-8896-14c8d264ca2f" />
<img width="557" height="598" alt="Screenshot from 2025-08-27 17-56-15" src="https://github.com/user-attachments/assets/eae51b10-626f-4015-ba2c-afdbffac3aa4" />
