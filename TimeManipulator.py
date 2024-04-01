# Time manipulator

# changes the time given in total seconds
# and returns the respective values
# of the year(s), month(s), week(s),...upto second(s)

# input MUST be convertible to an integer


def getTime(secs):
	ts = int(secs)
		
	ys = 31536086
	mts = 2628007
	ws = 604800
	ds = 86400
	hs = 3600
	ms = 60
	ss = 1
	
	fts = ""
	
	if ts >= ys:
		yv = int(ts / ys)
		if yv == 1:
			fts = f"{yv} year,"
		elif yv > 1:
			fts = f"{yv} years,"
		ts = int(ts % ys)
		print (f"{yv} years got.. remaining {ts} seconds")
		
	if ts >= mts:
		mtv = int(ts / mts)
		if mtv == 1:
			fts = f"{fts}{mtv} month,"
		elif mtv > 1:
			fts = f"{fts}{mtv} months,"
		ts = int(ts % mts)
		print (f"{mtv} months got, rem {ts} secs")
		
		
	if ts >= ws:
		wv = int(ts / ws)
		if wv == 1:
			fts = f"{fts}{wv} week,"
		elif wv > 1:
			fts = f"{fts}{wv} weeks,"
		ts = int(ts % ws)
		print (f"{wv} weeks got.. rem {ts} secs")
		
	if ts >= ds:
		dv = int(ts / ds)
		if dv == 1:
			fts = f"{fts}{dv} day,"
		elif dv > 1:
			fts = f"{fts}{dv} days,"
		ts = int(ts % ds)
		print(f"{dv} days got.. {ts} secs rem..")
		
	if ts >= hs:
		hv = int(ts / hs)
		if hv == 1:
			fts = f"{fts}{hv} hour,"
		elif hv > 1:
			fts = f"{fts}{hv} hours,"
		ts = int(ts % hs)
		print(f"{hv} hours got, {ts} secs rwm..")
		
	if ts >= ms:
		mv = int(ts / ms)
		if mv == 1:
			fts = f"{fts}{mv} minute,"
		elif mv > 1:
			fts = f"{fts}{mv} minutes,"
		ts = int(ts % ms)
		print(f"{mv} minutes got, {ts} secs rem..")
		
	if ts >= ss:
		sv = int(ts / ss)
		if sv == 1:
			if fts == "":
				fts = f"{sv} second only."
			else:
				fts = f"{fts} and {sv} second."
		elif sv > 1:
			if fts == "":
				fts = f"{sv} seconds only."
			else:
				fts = f"{fts} and {sv} seconds."
		print(f"{sv} seconds got.")

	
	
	return (fts)