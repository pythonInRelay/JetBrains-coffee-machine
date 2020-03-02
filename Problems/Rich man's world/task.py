years = 0
x = abs(int(input()))

while x <= 700000:
    x += x * 0.071
    years += 1

print(years)
