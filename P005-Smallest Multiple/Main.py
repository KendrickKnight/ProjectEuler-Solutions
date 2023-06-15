# 2520 is the smallest number that can be divided by all numbers from 1 to 10.
# then whats smallest positive number dividable by all numbers from 1 to 20. 

import math

n = int(input())

def lcm(n):
    ans = 1
    for i in range(1,n+1):
        ans = int((ans*i)/math.gcd(ans,i))
    print(ans)

lcm(n)