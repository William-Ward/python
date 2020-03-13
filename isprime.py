#!/usr/bin/python
import os
import math

def isprime(n):                  # is prime function
    i = 2                        # initialize i to 2
    if(n < 2):                   # special case 2
        return 0                 # not prime
    while i < math.sqrt(n):      # 
        if(n%i == 0):            # if divides evenly
            return 0             # not prime
        i = i + 1                # increment i
    return 1                     # prime number

for i in range(1000000):             # check 100 numbers
    if(isprime(i)):              # call isprime
        print(i, 'is prime')     # if it's prime, print it

