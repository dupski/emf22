#!/bin/bash

py_copy () {
    ./pyboard.py --no-soft-reset -d /dev/tty.usbmodem1234561 -f cp $1 :/$1
}

py_copy devutils.py
py_copy apps/emfschedule/__init__.py
