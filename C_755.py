import itertools

n = input()
length = int(len(n))
n = int(n)

array = ['3','5','7']
tempPattern0 = []
tempPattern1 = []
allPattern = 0
if length == 3:
    for pair in itertools.permutations(array, 3):
        if (num := int(''.join(pair))) < n:
            tempPattern1.append(num)
else:
    for pair in itertools.permutations(array, 3):
        tempPattern1.append(int(''.join(pair)))
    allPattern = len(tempPattern1)
    for i in range(length -3): 
        for perttern in tempPattern1:
            perttern = str(perttern)
            for count in range(i + 3):
                tempPattern0.append(int(perttern[:count] + '3' + perttern[count:]))
                tempPattern0.append(int(perttern[:count] + '5' + perttern[count:]))
                tempPattern0.append(int(perttern[:count] + '7' + perttern[count:]))
                tempPattern1 = list(set(tempPattern1 + tempPattern0))
        if i == (length -4):
            tempPattern1 = ([num for num in tempPattern1 if num < n])

print(len(tempPattern1))