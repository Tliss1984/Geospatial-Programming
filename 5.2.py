
import math




def check_fermat(a, b, c, n):
	if n > 2 and a**n + b**n == c**n:
		print ("Holy smokes, Fermat was wrong!")
	else:
		print ("No, that doesn’t work.")


a=int(input("Find out if Fermet's Last Therom is True! Input 4 values(a,b,c,n>2) starting with a:"))
b=int(input('b:'))
c=int(input('c:'))
n=int(input('n:'))




check_fermat(a,b,c,n)

    
