import datetime
def userinput():
    getDate=False
    while not getDate:
        try:
            date1=raw_input("enter your birthday date(MM-DD):")
            MM1=int(date1[0:2])
            DD1=int(date1[3:5])
            date1=datetime.date(2011,MM1,DD1)
            return date1
            getDate=True
            if MM1==2 and DD1==29:
                print "Feb,is 28 days. please enter right input"
        except:
            print "Please enter a valid month and day."
user1=str(userinput())

import datetime
def userinput():
    getDate=False
    while not getDate:
        try:
             date2=raw_input("Please enter a friend's birthday(MM-DD):")
             MM2=int(date2[0:2])
             DD2=int(date2[3:5])
             date2=datetime.date(2011,MM2,DD2)
             getDate=True
             if MM2==2 and DD2==29:
                print "Feb,is 28 days. please enter right input"
             return date2
        except:
            print "Please enter a valid month and day."

user2=str(userinput())
month1=user1[5:7]
day1=user1[8:10]
month2=user2[5:7]
day2=user2[8:10]
date1=datetime.date(2011,int(month1),int(day1))
date2=datetime.date(2011,int(month2),int(day2))
a=str(date1.strftime("%A"))
b=str(date2.strftime("%A"))
if month2>month1 and (a=="Saturday" or a=="Friday"):
    print 'your birthday come first! Great! The party is on ' +date1.strftime("%A")+ ',a weekend night.'
elif month2<month1 and (b=="Saturday" or b=="Friday"):
    print 'your friends come first! Great! The party is on ' +date2.strftime("%A")+ ',a weekend night.'
elif month2==month1 and day1<day2 and (a=="Saturday" or a=="Friday"):
    print ' your birthday come first! Great! The party is on ' +date1.strftime("%A")+ ',a weekend night.'
elif month2==month1 and day1>day2 and (b=="Saturday" or b=="Friday"):
    print 'your friends come first! Great! The party is on ' +date2.strftime("%A")+ ',a weekend night.'
elif month2==month1 and day1==day2 and (a=="Saturday" or a=="Friday"):
    print 'you can celebrate it together! Great! The party is on ' +date1.strftime("%A")+ ',a weekend night.'
else:
    if month2>month1 or (month2==month1 and day1<day2): 
        print 'your birthday come first! Too bad!  The party is ' +date1.strftime("%A")+ ',a school night.'
    elif month2<month1 or (month2==month1 and day1>day2):
        print 'your friends come first! Too bad!  The party is ' +date2.strftime("%A")+ ',a school night.'
    elif month2==month1 and day1==day2:
        print 'you can celebrate it together! Too bad!  The party is ' +date1.strftime("%A")+ ',a school night.'
