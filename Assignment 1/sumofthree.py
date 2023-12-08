#Read input
n=int(input("three digit number:"))
print("\n n is: ",n)

n1=n//100
print("first digit is:", n1)

n2=n//10
n2=n2%10
print("second digit is: ", n2)

n3=n%10
print("third digit is: ", n3)

total=n1 + n2 + n3
print("Sum = : ",total)