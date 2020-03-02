sum1 = 0
sum2 = 0

# If the first number is 0 print "0" and end program

while True:
    entry = input()
    if entry == "0" and sum1 == 0:
        print("0")
        break

    # If the first number isn't 0, add it to sum1 and sum2
    sum1 += int(entry)
    sum2 += int(entry) ** 2  # Calculate the sum of each value's square

    if sum1 == 0:  # When sum1 reaches 0, print sum2
        print(sum2)
        break
