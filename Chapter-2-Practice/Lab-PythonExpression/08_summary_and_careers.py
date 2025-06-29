bill = float(input("the total bill for today is :"))
tips = int(input("the percent of tips for this bill will be :"))
mPerson  = int(input("today we have : "))
print('--------------------------')
total= ((bill*(tips/100)+bill)/4)
print(f"the total for today will be :{total} bath")

