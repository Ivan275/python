date=raw_input("Enter a date in YYYY-MM-DD:")
YYYY =date[0:4]
MM =date[5:7]
DD =date[8:10]
if len("date")<10:
    print "date does not have enough hyphens."
elif len("date")>10:
    print "date have too many hyphens."
else:
    print "your book is due" + YYYY+ "-"+ MM+ "-"+DD+"."
while MM=01 or 03 or 05 or 07 or 08 or 10 or 12:
                DD=31
        if DD<=10:
                DD=DD+21
        else:
                DD=DD%31 and MM=MM+1
while MM=04 or 06 or 09 or 11:
                DD=30
        if DD<=9:
                DD=DD+21
        else:
                DD=DD%30 and MM=MM+1
while MM=02:
                DD=28
        if DD<=7:
                DD=DD+21
        else:
                DD=DD%28 and MM=MM+1
while MM<=12:
        MM=MM%12 and YYYY=YYYY+1

print "your book is due" + YYYY+ "-"+ MM+ "-"+DD+"."
            
