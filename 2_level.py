arrayLenght = int(input("Введіть довжину масиву: "))
arrayHeight = int(input("Веддіть ширину масиву: "))

inputLine = input("Введіть числа массиву через пробіл: ")
arrayOfNumbers = inputLine.split(" ")

doubleArray = [[0] * arrayLenght for i in range(arrayHeight)]

x = 0

for i in range(len(doubleArray)):
    for j in range(len(doubleArray[i])):
        doubleArray[i][j] = arrayOfNumbers[x]
        x += 1

doubleArray.reverse()

for i in doubleArray:
    for j in i:
        print(j, end = ' ')
    print()