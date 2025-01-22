### January 22, 2025
### Keenan Young COMSC 175
### ShowBreak.py

"""
unwanted text
Print statement %
"""

from math import factorial

while __name__:
   N = input('Enter a nonnegative integer: ')
   try:
      fatN = factorial(int(N))
      if int(N)>=0:
         break
   except ValueError as vee:
      print("ValueError %s."%vee)
      print('N must be non-negative integer.')
      continue
   
   
print('\n\n%1d! = %1d' % (int(N),fatN))

