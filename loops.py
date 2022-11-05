# Dynamic looping using for
n = 1
starting_value = int(input("enter the starting value: "))
for i in range(starting_value, 20+n):
    print(i)

# more dynamic looping using for.
step = 3
for i in range(1, 20+1, step):  # 3 is the intervals that we want
    print(i)
