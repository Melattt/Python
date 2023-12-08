#Read input
S=int(input("initial savings: "))
print(S)
P=int(input("interest rates in percentages: "))
print(P)
t=5

#Compute the value of savings after 5 years
A=S * (1+P/100)**t

#Present value
print("A is: ", round(A))