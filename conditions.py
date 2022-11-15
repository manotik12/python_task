# using if statements to evaluate conditions
age_limit = int(input("enter age limit: "))

driver_age = int(input("Enter your age: "))
if (driver_age >= age_limit):
    print("eligible to have driving license")

else:
    print("not legible to have drivers license")
    print(f"please check back in {age_limit - driver_age} years")
