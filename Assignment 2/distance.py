import math

def distance(X1,Y1,X2,Y2):
    d = math.sqrt( (X1 - X2)**2 + (Y1 - Y2)**2)
    return d
    


#Program starts
X1=float(input("Enter X1: "))
Y1=float(input("Enter Y1: "))
X2=float(input("Enter X2: "))
Y2=float(input("Enter Y2: "))

dis = distance(X1,Y1,X2,Y2)
dis = round(dis,3)
print(dis)