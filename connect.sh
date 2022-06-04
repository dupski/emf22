#!/bin/bash

echo "Type CTRL+A then D to quit."
sleep 1
screen -S emfbadge /dev/tty.usbmodem1234561 115200
pkill SCREEN
