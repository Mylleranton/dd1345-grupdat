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
	