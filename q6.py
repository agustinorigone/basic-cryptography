import sys
import time
from math import sqrt

start = time.time()

def inverseModuloCalculator(a, b, t1, t2):
  #breaking condition: when b is zero => t1 is the multiplicative inverse
  if b == 0:
    return t1
 
  #calculate the remainder
  r = a % b

  #calculate the quotient
  q = a // b

  #calculate t
  t = t1 - (t2 * q)
  
  #next recursive call we will be:
  #shift b for a
  #shift r for b
  #shift t2 for t1
  #shift t for t2
  return inverseModuloCalculator(b, r, t2, t)

def getPrimeFactorization(n):
	primeFactorization = []  
	#here we will neatly divide n by 2 as many times as we can
	#on each iteration we will save 2 as the factor
	while n % 2 == 0:
		#append 2 as the factor
		primeFactorization.append(2)
		n = n / 2

	#here we will be strating iterating in 3 (since 2 was covered in the previos loop)
	#we will iterate still the sqrt of n
	#we will be incrementing by 2 every iterating (since even number are already covered)
	for i in range(3, int(sqrt(n)) + 1, 2):
		if(n % i) == 0:
			#appending i as the factor
			primeFactorization.append(i)
			n = n / i
  	
	if(n > 2):
		primeFactorization.append(int(n))

	return primeFactorization

def encrypt (m, e, n):
	return pow(m,e,n)

def decrypt (c, d, n):
	return pow(c,d,n)

#check if n,e are provided as an argument
if len(sys.argv) < 4:
  print("ERROR: You must provide n,e,c as an argument")
  print("USAGE: python3 q6.py 937513 638471 533071")
else:
	#initilialize n
	n = int(sys.argv[1])

	#initilialize e
	e = int(sys.argv[2])

	#initilialize c
	c = int(sys.argv[3])

	#call getPrimeFactorization
	primeFactorization = getPrimeFactorization(n)

	#set p
	p = primeFactorization[0]

	#set q
	q = primeFactorization[1]

	#calculate phi
	phi = (p - 1) * (q - 1)

	#call inverseModuloCalculator recursive function
	d = inverseModuloCalculator(e if e > phi else phi, phi if phi < e else e, 0, 1)
	
	#call decrpyt function
	m = decrypt(c,d,n)

	#print original message m
	print("RESULT: The original message m is",m)

end = time.time()
print("TIME:",end - start, "seconds")