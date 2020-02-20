a=0
while a<100:
    a=a+1
    if a%7==0: #7的倍数
    	continue
    if a%10==7: #个位是7
    	continue
    if a//10==7: #十位是7
        continue
    print(a)