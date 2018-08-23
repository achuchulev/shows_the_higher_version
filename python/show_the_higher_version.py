#!/usr/bin/env python	

#define variables
link = ("https://releases.hashicorp.com/vault/index.json")

#load modules
import urllib
import json

#read URL content
out = urllib.urlopen(link).read()

#print out

#json module takes a json string and read it
j = json.loads(out)

#filter result for all version
result = j["versions"]

print result

#use loop to extract download url of each provider 
#print 'The higher version is: '

#for ver in result: print ver['version']
	
