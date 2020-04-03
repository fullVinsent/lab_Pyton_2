arrayOfNumbers = []
count = 0
answerArray = []

while count < 10:
    arrayOfNumbers.append(int(input()))
    count += 1

for x in arrayOfNumbers:
    if x % 11 == 0:
        answerArray.append(x)

answerArray.sort(reverse = True)

print(answerArray)