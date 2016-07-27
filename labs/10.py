num=int(raw_input("please input a number in the range(0,127):"))
if num<128:
   digit_7=0
else:
   digit_7=1
   num=num-128
if num<64:
   digit_6=0
else:
   digit_6=1
   num=num-64
if num<32:
   digit_5=0
else:
   digit_5=1
   num=num-32
if num<16:
   digit_4=0
else:
   digit_4=1
   num=num-16
if num<8:
   digit_3=0
else:
   digit_3=0
   num=num-8
if num<4:
   digit_2=0
else:
   digit_2=1
   num=num-4
if num<2:
   digit_1=0
else:
   digit_1=1
   num=num-2
if num<0:
   digit_0=0
else:
   digit_0=1
   num=num-0
print "num"+"(10)" + "=" + str(digit_7) + str(digit_6)+str(digit_5)+str(digit_4)+str(digit_3)+str(digit_2)+str(digit_1)+str(digit_0)+"(2)"

