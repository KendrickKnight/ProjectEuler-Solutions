#Problem:By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#Goal: Sum of even entries in sequence

# Fibonacci sequence is the addidtion of 2 previous entries, & starting with 1 and 2.
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,...


Fib = [1,2]
Out = 0

while Fib[len(Fib)-1] < 4000000:
    Fib.append(Fib[len(Fib)-1]+Fib[len(Fib)-2])

print(Fib)

for i in Fib:
    if i % 2==0: Out += i
    else:continue

print(Out)

