print("welcome to the trip calculator")

totalbill=float(input("What was the total bill?"))
percentage =float(input("What percentage tip would you like to give ?10,12 or 15"))
num=int(input("how many people split the bill? "))
if percentage==12:
    tip=0.12*totalbill
elif percentage==10:
    tip=0.1*totalbill
else:
    tip=0.15*totalbill
totallpay=totalbill+tip
pay = round(totallpay/num, 2)
print("each person should pay $"+str(pay))
