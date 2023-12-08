
number= int(input("Enter an odd positive integer: "))
print("\nThe triangle for number",number)

if number < 1 and number % 2 == 0:
    print("Error")
     
print("Right angled triangle:")

for i in range(number,0,-1):
    print("  "*(number-i)+" *"*(i))

print("Isosceles triangle:")

row=0
while row < number-3:
    
    line=0
    while line < number-row:
        print(" ",end=" ")
        line += 1

    col=0
    while col < 2*(row)+1:
        print("*",end=" ")
        col +=1

    row +=1
    print()   