#Problem:By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#Goal: Sum of even entries in sequence

# Fibonacci sequence is the addidtion of 2 previous entries, & starting with 1 and 2.
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,...


fib = [1,2]
out = 0

while fib[len(fib)-1] < 4000000:
    fib.append(fib[len(fib)-1]+fib[len(fib)-2])

print(fib)

for i in fib:
    if i % 2==0: out += i
    else:continue

print(out)

# i figured later but my answer is technically wrong! i had to remove the last entry and i was just lucky that it wasnt an even number.