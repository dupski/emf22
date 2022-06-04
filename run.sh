#!/bin/bash

N="$(printf \\r)"

echo "Type CTRL+A then D to quit."
screen -dmS emfbadge /dev/tty.usbmodem1234561 115200
screen -S emfbadge -p 0 -X stuff "from emfschedule import test_func$N"
sleep 0.5
screen -r emfbadge
pkill SCREEN
#"^Mimport emfschedule^Memfschedule.main()^M"exit()
