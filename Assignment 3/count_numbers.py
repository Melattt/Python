import os
# Counting how many different numbers there are using a set
def count_different(lst):
    
    s=set()                 
    for i in lst: 
        s.add(int(i)) 
    return len(s)

# Counting the occurence of every number using dictionary
def count_occurrences(lst):

    d=dict()                                   
    for i in lst:
        d[i]=d.get(i,0)+1         
    return d


#Program starts

#Counting the number of different integers and their occurance in txt_A                                 
path="/Users/melat/OneDrive/Desktop/Python/1DV501/mh225ic_assign3/file_10000integers_A.txt"  
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
print("Number of different integers in txt_A:",count_different(nums))
print("Number of times each integer occurs in txt_A:", count_occurrences(nums))

#Counting the number of different integers and their occurance in txt_B                                
path="/Users/melat/OneDrive/Desktop/Python/1DV501/mh225ic_assign3/file_10000integers_B.txt"
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
print("Number of different integers in txt_B:",count_different(nums))
print("Number of times each integer occurs in txt_B:", count_occurrences(nums))
