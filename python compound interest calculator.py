# python compound interest calculator : 
principal=0
rate=0
time=0
while True :
    principal=float(input("enter the principal amount : "))
    if  principal<=0 :
        print("principal can't be less or equal to zero ")
    else :
        break

while True :
    rate=float(input("enter the interest rate : "))
    if  rate<=0 :
        print("interest rate can't be less or equal to zero ")
    else :
        break

while True :
    time=float(input("enter the time in years : "))
    if  rate<=0 :
        print("time can't be less or equal to zero ")
    else :
        break

total = principal *pow((1+rate/100) ,time)
print(f"balance after {time} year/s dh{total: .2f}")
