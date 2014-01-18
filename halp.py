#!/usr/bin/python

import os

if os.geteuid() != 0:
    exit("I need root permissions!")
