day = int(input("Enter day of the week (1–7): "))  

if 1 <= day <= 5:
    print("Weekday")
elif day == 6 or day == 7:
    print("Weekend")
else:
    print("Invalid day")
