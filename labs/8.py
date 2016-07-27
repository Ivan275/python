import datetime
def userinput():
    getDate=False
    while not getDate:
        try:
            date=raw_input("enter your birthday date(MM-DD):")
            month=int(date[0:2])
            day=int(date[3:5])
            if month==2 and day==29:
                print "Feb,is 28 days. please enter right input"
            date=datetime.date(2011,month,day)
            return date
            getDate=True
        except:
            print " it's not correct"

print userinput()


