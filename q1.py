import sys
import time

start = time.time()

def isPrime(p):
  #exclude 1
  if p == 1:
    return 0

  for i in range(2,p-1):
    #get the quotient
    quotient = p/i
    
    #check if the quotient is an integer value => p is not prime
    if(int(quotient) == quotient):
      return 0
  else:
    return 1
  

#check if p is provided as an argument
if len(sys.argv) < 2:
  print("ERROR: You must provide p as an argument")
  print("USAGE: python3 q1.py 9")
else:
  #initilialize p
  p = int(sys.argv[1])

  #run isPrime function
  result = isPrime(p)

  if result == 1:
    print("RESULT:", p, "is a prime number")
  else:
    print("RESULT:", p, "is not a prime number")

end = time.time()
print("TIME:",end - start, "seconds")