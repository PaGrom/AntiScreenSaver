#!/usr/bin/env python

from pymouse import PyMouse
import time

while 1:
	mouse = PyMouse()
	mouse.move(mouse.position()[0], mouse.position()[1]+1)
	time.sleep(60)