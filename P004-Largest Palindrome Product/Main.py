# Largest 3 digit palindrome product.

# Description: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91*99
# Find the largest palindrome made from the product of two 3-digit numbers.  

# Goal: find the largest palindrome made from product of 3 digit numbers

# Ideas:
#       - a function, that loops through 3-digit numbers in reverse and then checks if their products are a palindrome or not
#
# 


def palindromeCheck(a):
    lia=list(map(int,str(a)))
    for i in range(0,int(len(lia)/2)):
        if lia[i] != lia[len(lia)-i-1]:
            return False
        else: continue
    return True
        
li = []

for i in range(999,100,-1):
    for x in range(999,100,-1):
        if palindromeCheck(i*x):
            li.append(i*x)
            print(str(i) + " * " + str(x) + " = " + str(i*x))
            break

        
li.sort()
print(li)

    








