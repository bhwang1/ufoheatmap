import textparser
import xml.etree.ElementTree
import requests
from time import time, sleep

start = time()
loop = time()
count = 0
converted = {}
file = open("hwang_bryan_cities.txt", "r")
for x in file:
	line = file.readline()
	new = line.split("\t")
	location = new[0]
	location.replace(" ","")
	try:
		page = requests.get('http://open.mapquestapi.com/geocoding/v1/address?key=x5yDN0jlWSLU43Ggm9Yj2YHAuQbAfCTb&location=' + location + "&outFormat=xml").text
		root = xml.etree.ElementTree.fromstring(page)
		lat = root[1][0][1][0][15][0].text
		lon = root[1][0][1][0][15][1].text
		coords = ("%f,%f" % (float(lat), float(lon)))
		converted[coords] = new[1]
		count += 1
	except:
		pass
	if time() - loop >= 300:
		z = ((time() - start) / 60)
		print("%f Loops in %f minutes at %f loops/min" % (count, z, count/z))
		loop = time()

output = ""
for x in converted:
	output = output + ("%s\t%d\n" % (x, int(converted[x])))

new_file = open("hwang_bryan_latlon.txt","w")
new_file.write(output)
file.close()
new_file.close()

elapsed = time() - start
print("%d loops in %f minutes" % (count, elapsed/60))