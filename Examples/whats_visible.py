# another quick example to see if I can use more of the pyephem library correctly

# pip install pyephem
import ephem
from ephem.stars import stars as ephem_stars

# where I am looking from (using my back yard)
home = ephem.Observer()
home.lat = "34.7275455"
home.lon = "-86.7169633"
home.elev = 685

# assume anything below 10 degrees is not visible
# 10 degrees in radians is 0.174533
horizon = 0.174533

planets = []

# ephem knows the Moon and all the planets, even though it does not have a nice data structure for them
# although, epehem does not seem to have built-in knowledge of other dwarfs like Ceres, Eris, Haumea, Makemake,
# but this database has the latter four: https://minorplanetcenter.net/iau/Ephemerides/Distant/Soft03Distant.txt
planets.append(ephem.Mercury(home))
planets.append(ephem.Venus(home))
planets.append(ephem.Moon(home))
planets.append(ephem.Mars(home))
planets.append(ephem.Jupiter(home))
planets.append(ephem.Saturn(home))
planets.append(ephem.Uranus(home))
planets.append(ephem.Neptune(home))
planets.append(ephem.Pluto(home))

# find the visible ones by checking to see whether they are above the horizon
for planet in planets:
    if planet.alt > horizon:
        print str(planet.name) + " (" + str(planet.alt) + "), near " + str(ephem.constellation(planet)[1])

print

bright_stars = []

# ephem knows many "bright" stars
for star_name in ephem_stars:
    bright_stars.append(ephem.star(star_name, home))

# find the visible ones by checking to see whether they are above the horizon
for bright_star in bright_stars:
    if bright_star.alt > horizon:
        print str(bright_star.name) + " in " + str(ephem.constellation(bright_star)[1])
