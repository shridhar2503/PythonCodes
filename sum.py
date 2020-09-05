a = []
a = list(map(int,input('\nEnter the numbers : ').split()))
sum = 0
for i in range (len(a)):
	sum += a[i]

print (sum)