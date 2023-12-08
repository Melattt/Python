import random

n1=random.randint(1,100)
n2=random.randint(1,100)
n3=random.randint(1,100)
n4=random.randint(1,100)
n5=random.randint(1,100)
print(n1,n2,n3,n4,n5)

sum=n1+n2+n3+n4+n5
print("The sum is:", sum)


#Works this way too
sum = 0
for i in range (5):
    n1=random.randint(1,100)
    sum +=n1
print(sum)
