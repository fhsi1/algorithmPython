t = int(input())
words = [input() for i in range(t)]

result = []
for word in words:
    if len(word) > 10:
        word = word[0] + str(len(word) - 2) + word[-1]
    result.append(word)

for word in result:
    print(word)