#!/usr/bin/env python
# reducer.py
import sys;
import re;
import os

# maps ips to their counts
IPlist = {}
totalCount = 0


#read files 
dirOutput = "output/"
from os import path
files = [f for f in os.listdir(dirOutput)]

#go through each reducer output file
for f in files:
	if not f.endswith('~'):
			
		filenow = open(dirOutput+f)	
		
		for line in filenow:	
			#take ip and count	
			ip, count = re.split("[ \t]+", line.strip())
			
			totalCount = totalCount + int(count)
			
			IPlist[ip] = int(count)
			
	
#Display report
#print total of entries in the server log

print '%s\t%d' % ("--------------------------------------NUMBER OF CONNECTIONS TO THE SERVER:", totalCount)


#Number of entries for each IP
print("--------------------------------------NUMBER OF ENTRIES FOR EACH IP:")
for ip in IPlist.keys():
    print '%s\t%s'% ( ip, IPlist[ip])

#List of distinct IPs
print("--------------------------------------LIST OF DISTINCT IPs:")
for ip in IPlist.keys():
    print '%s\t'% ( ip)


