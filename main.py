
print("Welcome to the bill split generator")

a=float(input("input your bill amount "))
b=float(input("Enter the tip you want to give in percentage "))
c=int(input("No. of people to split "))

bill_perperson_withtip= (a*(1+b/100))/c

print("Bill per head incl tip is " + "{:.2f}".format(bill_perperson_withtip))
