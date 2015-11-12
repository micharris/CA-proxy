import re

#check for this line: "Percentage of the requests completed within given times"
#after matching it, read the 2nd line down (ms results line)
#check to see if any numbers in that line exceed 3000 (3 seconds is the SLA required maximum respons time)



def response_SLA():
	errorFlag = 0
	responseFlag = 0
	totalErrors = 0
	totalRequests = 0

	with open("stats2.log") as f:
		for line in f:
			if(re.search('Percentage of the requests.',line)):
				responseFlag = 1
			 
			if(responseFlag == 2 and re.search('-------------------.',line)):
				responseFlag = 3

			if(responseFlag == 1 and re.search('-------------------.',line)):
				responseFlag = 2

			if(responseFlag == 2):
				responseTimes = line.split()
				try:
					if(responseTimes[7].isdigit()):
						if(int(responseTimes[7]) > 3000): #3 seconds is the max average response time per Alon
							print "SLA response time exceeded for 90th percentile: "+responseTimes[0]+responseTimes[1]+" was "+responseTimes[7]+" ms"
				except IndexError:
					print ''

				
			if(re.search('Total',line)):
				totalRequests = line.split()
				totalRequests = int(totalRequests[1])

			if(re.search('Error',line)):
				errorFlag = 1

			if(errorFlag == 1):
				errNumber = line.split()
				if(errNumber[0].isdigit()):
					totalErrors += int(errNumber[0])

			if(re.search('\n',line)):
				errorFlag = 0

		try:
				if(totalRequests / totalErrors > .03): #no greater than 3% error rate
						print "SLA error count exceeded.  % of errors is: "+(totalRequests / totalErrors)*100
		except:
				print ''


response_SLA()
