a = []
n = int(input())
a = list(map(int,input().split()))
#product = []


#def MaxPairWiseProduct (arr,n):
#	res = 0
#	for i in range(0,n):
#		for j in range(1,n):
#			if(arr[i]!=arr[j]):
#				res = arr[i]*arr[j]
#				product.append(res)
#	return max(product)

#print (MaxPairWiseProduct(a,n))				

#comparing and multiplying each element of arr
#gave "time limit exceeded error"

#Now, I'm gonna try sorting all the elements in 
#ascending order and then returning the product
#of the greatest two. 

a.sort()
ans = a[-1]*a[-2]
print (ans)