room1 = int(input())
room2 = int(input())
room3 = int(input())

answer = (room1 + room2 + room3) // 2
print(answer)

if answer % 2 == 1:
    answer += 1
else:
    answer -= 1
print(answer)
