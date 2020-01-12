import json
from pprint import pprint
import os
"""
inf = open('/home/rohit/Desktop/MP/Scraping/Dmoz-topics.txt','r')

for line in inf:
	print "crawling " + line
	print 'scrapy crawl dmoz -o JSON/'+line.strip("\n")+'.json'
	os.system('scrapy crawl dmoz -o JSON/'+line.strip("\n")+'.json')
"""

def readFile(filename):
    with open(filename) as json_data:
        d = json.load(json_data)
        json_data.close()
        return d
        
links=readFile('/home/rohit/Desktop/MP/Scraping/tutorial/Arts.json')

count = 1
for l in links:
	
    try:    
        if len(l['link'][0])<3:
            continue
    except IndexError:
        continue
    with open('/home/rohit/Desktop/MP/Scraping/tutorial/tutorial/spiders/dmoz_spider.py', 'r') as file:
        data = file.readlines()

    filename=l['title']
    filename=filename[0].replace (" ", "_")
    
    opjsonFile='JSON/Trial/'+filename+'.json'
    if os.path.isfile(opjsonFile):
        continue
    
    new_link=(data[8][:28]+l['link'][0]+data[8][-2:]).encode('ascii')
    data[8]=new_link

    print data

    new_link=(data[8][:28]+l['link'][0]+data[8][-2:]).encode('ascii')
    data[8]=new_link
    with open('/home/rohit/Desktop/MP/Scraping/tutorial/tutorial/spiders/dmoz_spider.py', 'w') as file:
        file.writelines( data )
    
    print 'scrapy crawl dmoz -o JSON/Trial/'+filename+'.json'
    os.system('scrapy crawl dmoz -o JSON/Trial/'+filename+'.json') 