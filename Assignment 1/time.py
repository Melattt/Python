#Read the input
s=int(input("seconds"))

#Compute
h=s//3600
print("h is:", h)
s = s % 3600
m=s//60
print("m is:", m)
s=s%60
print("s is:", s )