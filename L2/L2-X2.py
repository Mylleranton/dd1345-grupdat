# -*- coding: utf-8 -*-
# Uppgift X1 Labb 2, Anton Möller
    
n = int(input("Hitta alla primtal upp till:"))

listofindices = []
for i in range(n+1):
    listofindices.append(True)

# A value of False indicate a non-prime
listofindices[0] = False
listofindices[1] = False

currentnumber = 2
while currentnumber <= n:
    if listofindices[currentnumber] == True:
        index = 0
        while (currentnumber**2 + index*currentnumber) <= n:    
            listofindices[currentnumber**2 + index*currentnumber] = False
            index += 1
                
    currentnumber += 1

for index,value in enumerate(listofindices):
   if value == True:
        print index