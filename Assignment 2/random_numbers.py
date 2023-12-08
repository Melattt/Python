import random
n=int(input("Number of random numbers: "))
sum=0
min=100
max=0

print("Generated values: ")
for i in range(n):
   r=random.randint(1,100)
   print (r,end=" ")
    
   sum += r
   average = sum / n
    
   if r < min:
      min = r
   if r > max:
      max = r

print("\nAverage,min and max are",average,min,max)


    