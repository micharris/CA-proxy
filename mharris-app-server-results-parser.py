import re

#check for this line: "Percentage of the requests completed within given times"
#after matching it, read the 2nd line down (ms results line)
#check to see if any numbers in that line exceed 3000 (3 seconds is the SLA required maximum respons time)



def response_SLA():
    errorFlag = 0
    totalErrors = 0
    totalRequests = 0

    with open("stats.log") as f:
        for line in f:
            if(re.search('Percentage of the requests.',line)):
                 next(f) # skip 1 line
                 next(f) # skip another line
                 responseTimes = next(f).split()
                
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
                            
    for i in responseTimes:
        if(i.isdigit()):
            if(int(i) > 3000): #3 seconds is the max average response time per Alon
                print "SLA response time exceeded."

    if(totalRequests / totalErrors > .03): #no greater than 3% error rate
        print "SLA error count exceeded.  % of errors is: "+(totalRequests / totalErrors)*100


response_SLA()
