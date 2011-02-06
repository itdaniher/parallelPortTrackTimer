#! /usr/bin/python
import time
import parallelppdev
from math import log
import re
p = parallelppdev.Parallel()
p.PPDATADIR(0)
num_tracks = int(raw_input("How many Tracks? "))
info = []
exclude = []
null = raw_input("Hit enter to start countdown...")
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("GO!\n")

start=time.time()
while len(info) != num_tracks:
	val = p.PPRDATA()
	if val != 255:
		if val not in exclude:
			d = { "end":time.time(), "dec":val, "rank":len(info)+1 }
			info.append(d)
			exclude.append(val)

for d in info:
	d["lane"] = int(log(255-int(d["dec"]),2))
	d["time"] = d["end"] - start
	d["time"] = "%.5f" % d["time"]
	del d["end"]
	del d["dec"]
clean = re.sub("}, {","}\n{",str(info))
clean = re.sub("[\]\[]","",clean)
print clean + "\n"
while True:
	if str(raw_input("type 'close' to exit: ")) == "close":
		quit()
