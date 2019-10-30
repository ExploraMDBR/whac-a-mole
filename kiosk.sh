#!/bin/bash
xset s noblank
xset s off
xset -dpms

#Use this if need to hide the mouse:
#Require installing unclutter
#unclutter -idle 0.5 -root &

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences

/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk https://www.adafruit.com &
