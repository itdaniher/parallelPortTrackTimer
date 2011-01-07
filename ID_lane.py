#! /usr/bin/python
import time
import parallel
from math import log
p = parallel.Parallel()
p.PPDATADIR(0)
while True:
	val = p.PPRDATA()
	if val != 255:
		 print "lane "+"%.0f" % log(255-val,2)
	time.sleep(.2)
