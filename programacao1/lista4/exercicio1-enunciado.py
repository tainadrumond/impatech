x = 2
myList = [1, 2, 3, 4]
myDict = {
    'chave1': 1,
    'chave2': x,
    3: 'Value',
    (1, 2): 'Nossa que massa!!!',
    'L': myList
}
x = 3
myDict['L'][2] = 5

# a
print(myDict['chave1'])
print(myDict['chave2'])

#b
print(myDict[3] + ' is bad')

#c
print(myDict[(1, 2)][6:16])

#d
print(myList)

