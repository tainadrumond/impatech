x = 21
myList = [10, 11, x, 13, "Ola", "casa", "carro", "pé"]
for i in myList[1:]:
    print(i)
    
print()

x = True or False
for i in myList[1:-3]:
    print(i)
    
print()

x = not True or False
for i in myList[::-3]:
    print(i)

print()
    
oList = [1, 2, 3]
myList = [[11,22,33,44], oList, ["ola", "tchau"]]
oList.append(4)
for i in myList:
    print(i)
    
