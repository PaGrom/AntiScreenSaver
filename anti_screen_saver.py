#!/usr/bin/env python

from pymouse import PyMouse
import time

mouse = PyMouse()
while 1:
	mouse.move(mouse.position()[0], mouse.position()[1]+1)
	time.sleep(60)