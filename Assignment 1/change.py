Price=float(input("price: ", ))
print("Price: ", round(Price))
Payment=int(input("payment: ", ))
print("Payment: ", Payment)
Change=Payment-round(Price)
print("Change: " , Change)

c=Change // 1000
print("1000kr bills: " ,int(c))
Change=Change % 1000
c=Change // 500                    
print("500kr bills: " ,int(c))
Change=Change %  500
c= Change // 200
print("200kr bills: " ,int(c))
Change=Change % 200
c=Change // 100
print("100kr bills: " ,int(c))
Change=Change % 100
c=Change // 50
print("50kr bills: " ,int(c))
Change=Change % 50
c=Change // 20
print("20kr bills: " ,int(c))
Change=Change % 20
c=Change // 10
print("10kr coins: " ,int(c))
Change=Change % 10
c=Change // 5
print("5kr coins: " ,int(c))
Change=Change % 5
c=Change // 2
print("2kr coins: " ,int(c))
c=Change % 2
print("1kr coins: " ,int(c))