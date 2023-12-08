text=input("Enter a large positive integer: ")

n0,n_odd,n_even=0,0,0

for c in text:
    if c == '0':
        n0 += 1
    elif c == '2' or c=='4' or c=='6' or c=='8':
        n_even += 1
    elif c == '1' or c=='3' or c=='5' or c=='7' or c=='9':
        n_odd += 1

print("\nZeros: ", n0)
print(" Even: ", n_even)
print("  Odd: ", n_odd)