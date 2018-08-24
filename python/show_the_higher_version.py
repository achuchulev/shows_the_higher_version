#!/usr/bin/env python	

#define variables
link = ("https://releases.hashicorp.com")
ext = ("/vault/index.json")
url = (link + ext)
max_ver = ("0.0.0")
ex1 = ("rc1")
ex2 = ("beta1")

print url

#load modules
import urllib
import json

#read URL content
out = urllib.urlopen(url).read()

#print out

#json module takes a json string and read it
j = json.loads(out)

#filter result for all version
result = j["versions"]

#print result

#use loop to extract all versions 
#print 'The higher version is: '

for cur_ver in result: 
	if (cur_ver.find(ex1) == -1 and cur_ver.find(ex2) == -1): #print "This is not RC or Beta ver", cur_ver #max_ver = max_ver
		if max_ver < cur_ver: 
				print "Current version", cur_ver, "/ Max version", max_ver  
                                max_ver = cur_ver
		else: print "This version", cur_ver, "is lower than", max_ver
#print max_ver
	
