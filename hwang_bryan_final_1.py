import requests
import feedparser
from bs4 import BeautifulSoup
from time import time, sleep
import pickle

#define class
class UFO:
	def __init__ (self, city, state, tally):
		self.city = city
		self.state = state
		self.tally = tally

	def increase(self):
		self.tally+=1	

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

ufo = requests.get('http://www.nuforc.org/webreports/ndxevent.html')
bs = BeautifulSoup(ufo.text, 'html.parser')
links = bs.find_all('a')
links.pop(0)
start = time()
loop = time()
count = 0
unique = 0
total = 0
listy = {}

for month in links:
	url = month.get('href')
	data = requests.get('http://www.nuforc.org/webreports/' + url)
	page = BeautifulSoup(data.text, 'html.parser')
	page = page.find_all('tr')
	for line in page:
		info = line.find_all('td')
		if len(info) == 7:
			if info[2].text in states:
				if info[1].text != "":
					if info[2].text != "":
						citystate = ("%s,%s" % (info[1].text, info[2].text))
						total += 1
						if citystate in listy:
							z = UFO(info[1].text, info[2].text, listy[citystate])
							z.increase()
							listy[citystate] = int(z.tally)
						else:
							listy[citystate] = 1
							unique += 1
	sleep(5)
	count += 1
	if time() - loop >= 300:
		z = ((time() - start) / 60)
		print("%f Loops in %f minutes at %f loops/min" % (count, z, count/z))
		loop = time()


output = ""
for x in listy:
	output = output + ("%s\t%d\n" % (x, listy[x]))
file = open("hwang_bryan_cities.txt","w")
file.write(output)
file.close()
elapsed = time() - start
print("%f minutes" % elapsed)
print("%d loops" % count)
print("%d unique locations" % unique)
print("%d total locations" % total)