#Find the smallest k such that 1+2+3+...+k<=n
num=int(input("Enter a positive integer: "))
n=0
k=-1

if num < 1:
    print("The integer should be positive!")

while n + k <= num:
    k = k + 2
    n = n + k
print("Smallest k is: ", k)