# a quick example to see if I can use the pyephem library correctly

# pip install pyephem
import ephem

# where I am looking from (using my back yard)
home = ephem.Observer()
home.lat = "34.7275455"
home.lon = "-86.7169633"
home.elev = 685

# an alternate viewpoint from Huntsville square (trying to match https://www.timeanddate.com/moon/usa/huntsville)
courthouse = ephem.Observer()
courthouse.lat = "34.7306532"
courthouse.long = "-86.58822"
courthouse.elev = 650

# what I want to look at
moon1 = ephem.Moon(home)
moon2 = ephem.Moon(courthouse)

# where I should look
print "Where is the Moon (from home)?"
print "Date: " + str(home.date)
print "Azimuth: " + str(moon1.az)
print "Altitude: " + str(moon1.alt)

# where I should look
print "Where is the Moon (from courthouse)?"
print "Date: " + str(courthouse.date)
print "Azimuth: " + str(moon2.az)
print "Altitude: " + str(moon2.alt)
