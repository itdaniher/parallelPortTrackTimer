#Ian Daniher - 2011.03.17 - 2011.03.16

#use the python parallel lib
import parallel
#use the python time library
import time

#invoke pyparallel class
p = parallel.Parallel()

#set parallel port directoin to be input
p.PPDATADIR(0)

#figure out how many events to wait for
numTracks = int(raw_input("How many Tracks? "))

#init variables
lanes = []
times = []
exclude = []

#wait for user input
raw_input("Hit enter to start race...")

#record starttime
startTime = time.time()

#while the number of discrete lane-events is not equal to the number of tracks....
while len(set(lanes)) != numTracks:
#get one byte of data from the parallel port
	data = p.PPRDATA()
#iterate through the possible lanes
	for a in range(0, 8):
#use bitmath magic to see if that lane is zero(triggered) or one(untriggered)
		if (data & 2**a) >> a != 1:
#if the lane hasn't already had an event recorded for it
			if a not in exclude:
#append at lane to the "lanes" list
				lanes.append(a)
#append the difference between current and start times to the "times" list
				times.append(time.time()-startTime)
#tell the system to ignore future events on that lane
				exclude.append(a)
#form tuples from lanes and times, print them
print zip(lanes, times)
#wait for user to type "close," then quit
while True:
        if str(raw_input("type 'close' to exit: ")) == "close":
                quit()

