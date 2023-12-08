import os
import math

# Calculating the mean
def mean(lst):
    length=len(lst)                                  
    sum=0
    for i in lst:
        sum += i                                
    mean_=(sum/length)                                                                       
    return round(mean_,2)
   
# Calculating the standard deviation
def std(lst):
    sum=0
    sum1=0
    length=len(lst) 
    for i in lst:
        sum += i                                                              
    mean=sum/length

    for i in range(length):                            
        sum1 =sum1 + (lst[i]-mean)**2
    root = sum1*1/length
    f=math.sqrt(root)
    return round(f,2)


#Progarm starts

#Mean and standard deviation for the first txt file
path= "/Users/melat/OneDrive/Desktop/Python/1DV501/mh225ic_assign3/file_10000integers_A.txt"
# Open the file
file=open(path,"r")
text=file.read()
nums=[] 
# To split the lines in the text file                                      
l=text.split("\n")                          
for lines in l:
    sep=lines.replace(":",",")               
    sep=sep.split(",")                       
    
    for number in sep:
        # Remove all spaces
        number=number.strip()               
        
        # Append it to the list if it is a number
        if number != "":
            nums.append(int(number))              
file.close()                        
print("Mean of A is",mean(nums))
print("Standard deviation of A is",std(nums))


#Mean and standard deviation for the second txt file
path= "/Users/melat/OneDrive/Desktop/Python/1DV501/mh225ic_assign3/file_10000integers_B.txt"
# Open the file
file=open(path,"r")
text= file.read()
# To split the lines in the text file
nums=[]                                      
l=text.split("\n")                           
for lines in l:
    sep=lines.replace(":",",")               
    sep=sep.split(",")                     

    for number in sep:
        # Remove all spaces
        number=number.strip()                
        
        # Append it to the list if it is a number
        if number != "":
            nums.append(int(number))              
file.close              
print("Mean of B is",mean(nums))
print("Standard deviation of B is",std(nums))
