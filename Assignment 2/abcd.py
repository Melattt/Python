def get_number(a,b,c,d):
    
    for a in range(1,9):

        for b in range(0,9):

            for c in range(0,9):

                for d in range(1,9):

                    if d*1000+c*100+b*10+a*1==4*(a*1000+b*100+c*10+d*1):
                        return a,b,c,d

#Program starts
f=get_number(0,0,0,0)
print(f)