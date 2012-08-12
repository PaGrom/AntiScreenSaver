#!/bin/env python

from pymouse import PyMouse
import time

while 1:
	mouse.move(m.position()[0], m.position()[1]+1)
	time.wait(60)