#!/usr/bin/env python
# reducer.py

import sys;
import re;


# maps ips to their counts
IPcount = {}
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    ip, count = line.split('\t', 1)
    # convert count (currently a string) to int
    #print(ip,count)
    try:
        count = int(count)
    except ValueError:
        continue
 
    try:
        IPcount[ip] = IPcount[ip]+count
    except:
        IPcount[ip] = count
 
 
#Number of entries for each IP
for ip in IPcount.keys():
    print '%s\t%s'% ( ip, IPcount[ip])


    
     


