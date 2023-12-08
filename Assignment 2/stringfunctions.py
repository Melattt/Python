#Number 1
def concat(s,n):
    x=s*n
    return x

#Number 2
def count(s,x):
    i=0
    for c in s:
        if c == x:
            i += 1
    return i


#Number 3
def reverse(s):
    rev=""
    for c in s:
        rev = c + rev
    return rev


#Number 4
def first_last(s):
    for c in s:
        f=s[0]
        l=s[-1]
    return f , l


#Number5
def has_two_X(s):
    x=0
    for c in s:
        if c=="X":
            x +=1

    if x==2:
        return True
    elif x < 2 or x > 2:
        return False


#Number 6
#i and j have different range so if the index of i ad j are equal means that there are duplicates.
def has_duplicates(s):
    
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i]==s[j] and i !=j:
                return True
    return False

