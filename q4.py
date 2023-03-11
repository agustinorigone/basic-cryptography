import sys
import time
from math import sqrt

start = time.time()

# def hcf(a,b):
#   while a != b:
#     if a > b:
#     #b is smaller than a => we substract b (the smallest)
#       a = a - b
#     else:
#       #a is smaller than b => we substract a (the smallest)
#       b = b - a
#   return a

def hcf(a,b):
  #breaking condition: when b is zero then a is the hcf
  if b == 0:
    return a
 
  reminder = a % b
  #next recursive call we will be:
  #shifting a for b
  #shifting reminder for b 
  return hcf(b, reminder)
  

#check if p is provided as an argument
if len(sys.argv) < 3:
  print("ERROR: You must provide a,b as an argument")
  print("USAGE: python3 q1.py 499017086208, 676126714752")
else:
  #initilialize a
  a = sys.argv[1]

  #initilialize b
  b = sys.argv[2]

  #run hcf function
  #result = hcf(int(a),int(b))
  #print("RESULT:",result)

  #run hcf recursive function
  result2 = hcfRecursive(int(a),int(b))
  print("RESULT (recursive):",result2)

end = time.time()
print("TIME:",end - start, "seconds")