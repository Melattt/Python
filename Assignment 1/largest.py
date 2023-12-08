A=int(input("enter A: " , ))
B=int(input("enter B: " , ))
C=int(input("enter C: " , ))

if A > B and A > C:
    print("The largest number is: " , A)
elif B > A and B > C:
    print("The largest number is: " , B)
elif C > A and C > B:
    print("The largest number is: " , C)