import datetime

# 13.1 Write the current date into a today.txt
def writetoday():
    today = datetime.date.today()

    file_today = open('today.txt','w')
    file_today.write(str(today))
    file_today.close()
    
# 13.2    
def readtoday():
    # read today_string from today.txt
    file_today = open('today.txt','r')
    today_string = file_today.read()
    file_today.close()
    
    # printing today_string
    print(today_string)

#13.3
def parsetoday():
    # read today_string from today.txt
    file_today = open('today.txt','r')
    today_string = file_today.read()
    file_today.close()
    
    # parsing the today_string and print
    parsetoday = datetime.datetime.strptime(today_string, '%Y-%m-%d')
    print("Today is ", parsetoday)

#15.1

    

writetoday()
readtoday()
parsetoday()