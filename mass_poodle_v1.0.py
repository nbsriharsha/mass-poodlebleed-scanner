#!/usr/bin/python 
#coded by N B Sri Harsha
#Greetz to ALL IHOS and 404 members :) 

import requests,json
from HTMLParser import HTMLParser

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
       if data=='The Server at '+z+' has SSL 3.0 enabled. Clients connecting with browsers that support SSL 3.0 and HTTPS fall back will not be secure.':
        print bcolors.OKGREEN+"The "+z+" is Vulnerable :"+bcolors.ENDC 
        print "\n"

query=raw_input("Enter Dork:")
 
for start in range(0,3):  #if you want more results change range to 50
  page=1 
  resultPerPage=8
  url="http://ajax.googleapis.com/ajax/services/search/web?v=1.0&hl=iw&rsz="+str(resultPerPage)+"&start="+str(start)+"&q="+query
  print "Starting Google Search"
  search_response= requests.get(url)
  search_results=search_response.text
  results = json.loads(search_results)
  data = results['responseData']
  global hits
  hits=data['results']
  print "Results Grabbed , Testing For poodlebleed"

  for h in range(0,8):
    print "Checking  "+hits[h]['visibleUrl']
    global z
    z=hits[h]['visibleUrl']
    url2="http://poodlebleed.com/server.php?domain="+hits[h]['visibleUrl']+"&port=443"
    poodlebleed=requests.get(url2)
    parser = MyHTMLParser()
    parser.feed(poodlebleed.text)
