"""
def all_odd(lst):

    l=[]
    for c in lst:    
        if c % 2 != 0: 
            l.append(c)
    return l

m= [5,454,56,98,56,97,57,93,85]
f=all_odd(m)
print(f)


def add_dash(s):
    p = "-"
    return p.join(s)

s="abcd"
print(add_dash(s))
s="Jonas"
print(add_dash(s))


lst= []

for i in range(1,100):
    number = int(input(f'Number {i}: '))
    lst.append(number)
    i +=1
    if number in lst:
        break

n=[]



    numbers=int(input("Enter positive integers: "))
    
    n.append(numbers)
    if numbers < 0:
        break
 """    

lst= []

for i in range(1,100):
    number = int(input(f'Number {i}: '))
    if number in lst:
        break
    lst.append(number)
    
    
        
print("Identified duplicate element: ",number)     
rev=lst[::1]
#rev.pop(0)
separator=", "
rev = separator.join(rev)
print("All numbers: ",' '.join rev)

















