
for x in range(101):

    if x % 15 == 0:
        print("FizzBuzz")
        continue

    if x % 3 == 0:
        print("Fizz")
        continue

    if x % 5 == 0:
        print("Buzz")
        continue

    print(x)
