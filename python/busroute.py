#http://www.transitchicago.com/developers/

import urllib

# set u equal to
u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
# set data equal to refrenced url above
data = u.read()
# set f equal to "an open file named 'rt22.xml' in 'write buffered' mode "
f = open('rt22.xml', 'wb')
# writes data to 'rt22.xml'
f.write(data)
# closes xml file
f.close()
