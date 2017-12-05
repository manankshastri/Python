i = 1
number = 0
count = 0
while(count < 20):
    if(i%5 == 0 and i%7 == 0 and i%11 == 0):
        number = i
        print("Count: {} - Number: {}".format(count+1,number))
        i+=1
        count+=1
    else:
        i+=1