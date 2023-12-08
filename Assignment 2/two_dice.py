import random

lst=[0,0,0,0,0,0,0,0,0,0,0]

count=0
while count < 10000:
    r=random.randint(1,6) + random.randint(1,6)
    
    lst[r-2] +=1
    count +=1 

for i in range(len(lst)):
    l=" {0:2}      {1:2} ". format(i+2,lst[i])
    print(l)
