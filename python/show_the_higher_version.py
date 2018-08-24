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
from pkg_resources import parse_version

#read URL content
out = urllib.urlopen(url).read()

# json module loads raw data and convert it to json structure
j = json.loads(out)

#filter result for all version
result = j["versions"]

# use loop to extract all versions
# use find to exclude beta and rc versions
# compare all versions with max_ver 
for cur_ver in result: 
	if (cur_ver.find(ex1) == -1 and cur_ver.find(ex2) == -1): #print "This is not RC or Beta ver", cur_ver #max_ver = max_ver
		if parse_version(max_ver) < parse_version(cur_ver): 
				print "Current version", cur_ver, "/ Max version", max_ver  
                                max_ver = cur_ver
		else: print "This version", cur_ver, "is lower than", max_ver

print 'The higher version is: ', max_ver

