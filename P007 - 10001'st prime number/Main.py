
prime = [2,3]
count = 3

def checkIfDividable(n):
    for i in prime:
        if n%i==0:
            return False
        else: continue
    
    return True


while len(prime) < 10001:
    count += 2
    if checkIfDividable(count):
        prime.append(count)
        

print(prime[len(prime)-1])
print(prime)