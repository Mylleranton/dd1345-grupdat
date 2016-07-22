# Uppgift 4

def ramanujan(n):
    n = int(n)

    a = 1
    solutions = []
    for a in range(1,int(n**(1./3.))):
   	b = int(round((n-a**3)**(1./3.)))
	if a >= b:
	    break
	    	
	if (a**3 + b**3) == n:
	    solutions += [(a,b)]
	    
    return solutions
    
def isRamanujan(solutionList):
    return len(solutionList) >= 2
    
m = int(input("m = "))
ramanujanList = []
resultList = []
index = 1
while len(ramanujanList) != m:
    index_solution = ramanujan(index)
    
    if isRamanujan(index_solution):
        ramanujanList += [index]
        resultList += [index_solution]
    index += 1
        
print "Ramanujan number -- solution set"
for i in range(0, len(resultList)):
    print ramanujanList[i], " -- ",  resultList[i]
	