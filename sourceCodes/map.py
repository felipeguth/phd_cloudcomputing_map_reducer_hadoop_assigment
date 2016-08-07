#!/usr/bin/python

import sys;
import re;
from datetime import datetime

#Configure the parameters in order to filter by dates
filt  = 0 # 0 - filter desabled, 1 - enabled
date1 = "05/03/2004" #date FROM string dd/mm/yyyy, i.e.= "05/03/2004"
date2 = "05/03/2004" #date TO string dd/mm/yyyy, i.e.= "05/03/2004"

if (filt == 0): #No filter in date params
	
	#read file and produce key, value output
	for line in sys.stdin:
		try:
			(ip, a,b,dateS,d,mtd,linkS,hstr, p, p2) = re.split("[ \t]+", line.strip())			
			print '%s\t%s' % (ip, "1") 				
		except ValueError:
			continue
else: #filter
		
	dfrom = datetime.strptime(date1, "%d/%m/%Y")
	dto   = datetime.strptime(date2, "%d/%m/%Y")


	#read file and produce key, value output
	for line in sys.stdin:
		
		#Filter by date	
		try:
			(ip, a,b,dateS,d,mtd,linkS,hstr, p, p2) = re.split("[ \t]+", line.strip())			
			dateS = dateS[1:12]
			dateS = datetime.strptime(dateS, "%d/%b/%Y")
			if (dateS >= dfrom) and (dateS <= dto):
				print '%s\t%s' % (ip, "1") 				
		except ValueError:
			continue
