#Find the largest k such that 0+2+4+6+...+k<25
num = int(input("Enter a positive integer: "))
n = 0
k = -2
if num < 1:
    print("The integer should be positive!")

while n + k < num:
    k = k + 2
    n = n + k

print("Largest k is: ", k)