# Uppgift 4

n = int(input("n = "))

a = 1
solutions = 0
for a in range(1,int(n**(1./3.))):
	b = int(round((n-a**3)**(1./3.)))
	if a > b:
	    break
	    	
	if (a**3 + b**3) == n:
		solutions += 1
		print('Solution ' +  str(solutions))
		print("(" + str(a) + "," + str(b) + ")")

if solutions == 0:
    print "No solutions found. ", n, "cannot be written as a sum of cubes."	
