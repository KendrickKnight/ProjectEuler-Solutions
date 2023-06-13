# Problem: the prime factors of 13195 are 5,7,13,29 ==> LARGEST prime factor of 600851475143

# Goal: finding prime factors of a number --> taking the largest one
#   * technically i dont need to find and keep all of its prime factors. i just want to.

#Ideas:
#   1) Elimination process: when reached a prime number, remove all of its correlated succeeding numbers. exp: if even, take 2 and remove all other even numbers
#   2) Brute force: go through each number 1 by 1.
#   3) mix of the previous 2?


num = 600851475143
prime = []

# checking if a number can be divided by numbers in a list?
#   ok lets go brute force method and see where it takes me.

def checkIfDividable(n):
    for i in prime:
        if n%i==0:
            return False
        else: continue
    
    return True

# my Initial answer. it wastes a lot of time by going through all numbers. now at least it only goes through half of em

# for i in range(num):
#     print(i)
#     if i == 1 or i == 0:
#         continue
#     elif num%2==0: 
#         prime.append(2)
#     elif i%2==0:
#         continue
#     elif num%i==0 and checkIfDividable(i):
#         prime.append(i)
#         print(prime)

if num%2==0:
    prime.append(2)

for i in range(3,num,2):
    if num%i==0 and checkIfDividable(i):
        prime.append(i)
        print(prime)

# Tbh its WAY too brute force for my like. 
# if possible, i'd like to make the "process of elimination method" work.
# also finding and storing prime numbers for later use IS useful in its own right...











