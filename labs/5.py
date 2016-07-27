def getDate():
    checkinput=False
    while  not checkinput:
        date=raw_input("enter your birthday date(MM-DD):")
        try:
            month=int(date[0:2])
            day=int(date[3:5])
            date=datetime.date(2011,month,day)
            return date
            checkinput=True
        except:
            print "it's not correct month and day"
getDate()
