#read input
n=[]

for i in range(100):

    numbers=int(input("Enter positive integers: "))
    
    n.append(numbers)
    if numbers < 0:
        break
     
rev=n[::-1]
rev.pop(0)
print("Number of positive integers: ",len(rev))
print("In reverse order: ",rev)   

 
