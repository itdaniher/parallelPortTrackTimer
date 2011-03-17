import parallel
import time

p = parallel.Parallel()

p.PPDATADIR(0)

numTracks = int(raw_input("How many Tracks? "))

raw_input("Hit enter to start countdown...")

print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("GO!\n")

lanes = []
times = []
exclude = []

startTime = time.time()

while len(set(lanes)) != numTracks:
	data = p.PPRDATA()
	for a in range(0, 8):
		if (data & 2**a) >> a != 1:
			if a not in exclude:
				lanes.append(a)
				times.append(time.time()-startTime)
				exclude.append(a)
print zip(lanes, times)
while True:
        if str(raw_input("type 'close' to exit: ")) == "close":
                quit()

