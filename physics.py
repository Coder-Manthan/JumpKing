#!/usr/bin/env python
#
#
#
#

import math

def add_vectors(angle1, length1, angle2, length2):

	x = math.sin(angle1) * length1 + math.sin(angle2) * length2
	y = math.cos(angle1) * length1 + math.cos(angle2) * length2
	
	angle = math.pi/2 - math.atan2(y, x)
	length = math.hypot(x, y)

	return angle, length