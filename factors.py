# Python Program to find the factors of a number

# This function computes the factor of the argument passed
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x ):
       if x % i == 0:
           print(i)

num = 12

print_factors(num)
