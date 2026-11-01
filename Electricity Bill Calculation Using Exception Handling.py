try:
    units = float(input("Enter units: "))

    if units < 0:
        raise ValueError("Negative units not allowed")

except ValueError as e:
    print("Invalid input:", e)

else:
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 500 + (units - 100) * 7
    else:
        bill = 1200 + (units - 200) * 10

    print("Total Bill: Rs.", bill)

finally:
    print("Thank you!")