count1=0
for i in range(101):
    count1 += i*i

count2=0
for i in range(101):
    count2 += i

count2 = count2 * count2

print(count2-count1)