def is_positive_and_odd(n):
    
    if n % 2 != 0 and n > 0:
        return True
    else:
        return False
        
s=0
while s <= 5:      
    n = is_positive_and_odd(int(input("Enter a positive and odd integer: ")))
    #print(n)
    s += 1
    
    if n == True:
       break
