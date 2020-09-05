a = []
num_list = []
n = int(input())
a = list(map(int,input().split()))

for i in range(0,n):
	num_list.append(a[i])


def MaxPairWiseProduct (arr,n):
	res = 0
	c = []
	for i in range(n):
		for j in range(1,n):
			if arr[i] != arr[j]:
				res = arr[i]*arr[j]
				c.append(res)

	prod = max(c)
	return prod 

max_prod = MaxPairWiseProduct(num_list,n)				
print (max_prod)