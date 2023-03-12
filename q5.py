import sys
import time

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
  

#check if a,b are provided as an argument
if len(sys.argv) < 3:
  print("ERROR: You must provide a,b as an argument")
  print("USAGE: python3 q5.py 499017086208, 676126714752")
else:
  #initilialize a
  arg1 = int(sys.argv[1])

  #initilialize b
  arg2 = int(sys.argv[2])

  #we ensure a > b, as is an algorithm pre-requisite
  a = arg1 if arg1 > arg2  else arg2
  b = arg2 if arg1 > arg2  else arg1

  #call inverseModuloCalculator recursive function
  result = inverseModuloCalculator(a, b, 0, 1)

  #print result
  print("RESULT: The modular multiplicative inverse is",result)

end = time.time()
print("TIME:",end - start, "seconds")