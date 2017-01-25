# http://www.transitchicago.com/developers/
# https://developers.google.com/maps/documentations/staticmaps/


import urllib
from xml.etree.ElementTree import parse

u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()

print data

doc = parse('rt22.xml')

for bus in doc.findall('bus'):
    d = bus.findtext('d')
    lat = float(bus.findtext('lat'))
