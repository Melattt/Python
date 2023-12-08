import random
def random_list(n):
    lst=[]
    
    for i in range(n):
        r=random.randint(1,100)
        
        lst.append(r)
    return lst
    


#Number 2
def average(lst):
    s=sum(lst)
    Average=round(s/len(lst))
    return Average



#Number 3
def only_odd(lst):

    l=[]
    for c in lst:    
        if c % 2 == 1: 
            l.append(c)
    return l



#Number 4
def to_string(lst):
    
    l=""
    for i in lst:
        l +=str(i)
    f=",".join(l)
    return "[" + f + "]" 

#Number 5
def contains(lst,a,b):
    
    for i in range (len(lst)):
        if a == lst[i] and b == lst[i+1]:
            return True
       
    return False


#Number 6
def has_duplicates(lst):
    
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i]==lst[j] and i != j:
                return True
    return False
"""
or
for item in lst:
    if lst.count(item) > 1:
        return True
return False
"""