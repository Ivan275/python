a=str(raw_input('Enter a string:'))
b=' '
i=0
c=0
while i<len(a) and c<3:
        if a[i]==b:
            print 'there is a space in position '+str(i)
            c=c+1
        i=i+1
          
