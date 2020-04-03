carOwner = {
    "АА1256АВ": ["Mercedes", "Ivanov"],
    "АА1255КВ": ["LADA2101", "Shishnyakow"],
    "АВ1786МВ": ["Renoult", "Dhiprenko"],
    "КА8826АВ": ["FIAT", "Samarenko"],
    "ВК1586ВМ": ["FIAT", "Khuan"],
    "СС8326ВВ": ["Mitsubishi", "Durnev"],
    "УК1526АВ": ["BELAZ", "Sobolev"],
    "МН7456ОВ": ["Tavria", "Mykolich"],
    "АМ2656АВ": ["KIA", "Sanja"],
    "АВ1653ВВ": ["Infinity", "Domosed"],
}

def searchInDictionary(searchNumber):
    for x in carOwner:
        if x == searchNumber:
            tempList = carOwner[x]
            return tempList[1]

def statOfUniqueness():
    uniqueness = {}
    for x in carOwner:
        tempList = carOwner[x]
        if tempList[0] in uniqueness:
            uniqueness[tempList[0]] += 1
        else:
            uniqueness[tempList[0]] = 1
    for x, y in uniqueness.items():
        print(x, y)

check = False

while not check:
    tempCommand = input('Введіть команду ("search" для пошуку, "stat" для статистики, "q" для виходу): ')
    if tempCommand == 'search':
        print(searchInDictionary(input('Веведіть номер авто: ')))
    elif tempCommand == 'stat':
        statOfUniqueness()
    elif tempCommand == 'q':
        break
    else:
        print('Невірна команда!')