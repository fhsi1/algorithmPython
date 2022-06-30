n = int(input())
number = 0

for _ in range(n):
    petya, vasya, tonya = map(int, input().split())
    if petya + vasya + tonya >= 2:
        number += 1

print(number)