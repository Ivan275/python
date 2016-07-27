n=raw_input("Enter an integer:")
b=len(n)
count = 0
for i in range(0,b):
     if n[i] == '7':
            count = count+1
if count>=1:
    print n + " is lucky!"
else:
    print n + " is not lucky!"
