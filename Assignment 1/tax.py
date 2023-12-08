income=float(input("enter monthly income:", ))

if income < 38000:
    tax=income*30/100
    print("tax:", tax)
elif income > 38000 and income < 50000:
    tax=38000*30/100+(income-38000)*35/100
    print("tax:", tax)
elif income >50000:
    tax=38000*30/100+12000*35/100+(income-50000)*40/100
    print("tax:", tax)