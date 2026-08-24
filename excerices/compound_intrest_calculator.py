#python compound interest calculator
principal = 0
rate =0
time = 0


while principal <=0 :
    principal =float(input("enter principal amount: "))
    if principal <=0 :
        print("principal amount should be greater than 0")

while rate  <=0:
    rate =float(input("enter intrest rate: "))
    if rate <=0 :
        print("intrest rate can't be less than or equal to 0")

while time  <=0:
    time =int(input("enter the time in years: "))
    if time <=0 :
        print("time can't be less than or equal to 0")

total = principal * (1 + rate/100) ** time
print(f"total amount after {time} years is {total:.2f}")