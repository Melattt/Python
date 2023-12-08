
count = 0
for i in range(100,200):

    if i % 4 ==0 and i % 5 !=0:
        print(i, end=' ')
        count +=1

    
    
    elif i % 4 !=0 and i % 5 ==0:
        print(i, end=' ')
        count +=1
    

    if count == 10:  
        print( ) 
        count = 0
        #count +=1   