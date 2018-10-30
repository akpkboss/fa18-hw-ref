"""
matrix_multiply

Given two 2-D input arrays `arr0`, `arr1`, return the matrix product arr0 * arr1.
Return None if the matrix product does not exist.

As with math, assume that indices are in [row][column] format, so each inner list is a row.
"""

def matrix_multiply(arr0, arr1):
	if len(arr0[0]) != len(arr1):
		return None
    
	answer = []
	for i in range(0,len(arr0)):
		answer.append([])
		for j in range(0,len(arr1[0])):
			answer[i].append(0)
            
	for i in range(0,len(arr0)):
		for j in range(0,len(arr1[0])):
			for k in range(0,len(arr1)):
				answer[i][j] += arr0[i][k] * arr1[k][j]
	return answer
"""
nth_largest_element

Given an input list `arr`, and index `n`, return the nth largest element.
Avoid using built-in sorting methods.
"""
def heapify(arr, n, i): 
    largest = i  
    l = 2 * i + 1  
    r = 2 * i + 2 
    if l < n and arr[i] < arr[l]: 
        largest = l 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest) 
  
def heapSort(arr): 
    n = len(arr) 
    for i in range(n, -1, -1): 
        heapify(arr, n, i)  
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0) 

def nth_largest_element(arr, n):
	if n >= len(arr):
		return None
	heapSort(arr)
	return arr[len(arr)-n]
"""
reverse_block

Given an input list `arr`, and a block size `n` > 0, reverse the list in blocks of n.

Example:
	Arguments:
		[1,2,3, 4,5,6, 7], 3
	Return:
		[3,2,1, 6,5,4, 7]
	(spacing added for emphasis)

"""
def reverse_block(arr, n):
    answer = [] 
    iterate = 0
    while (iterate + n) < len(arr):
        answer.append(arr[iterate:iterate + n])
        iterate +=  n
    answer.append(arr[iterate:])
    for every in answer:
        every.reverse()
        
    finale = []
    
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            finale.append(answer[i][j])
    return finale

"""
subset_sum

Given an input list `arr`, and a number `target`, return whether or not any possible subset of the values in `arr` could sum to `target`.

Example 1:
	Arguments:
		[1,2,3,4,5,7], 13
		7 + 4 + 2 = 13
	Return:
		True

Example 2:
	Arguments:
		[1,2,-1,5,4,-196], 196
	Return:
		False
"""
def subset_sum(arr, target):
    if target is 0:
        return True
    elif len(arr) is 0:
        return False
    else:
        return subset_sum(arr[1:], (target - arr[0])) or subset_sum(arr[1:], target)

"""
spiral_matrix

Given an input 2-D array, return a list with the values obtained by following a clockwise spiral path, starting from [0][0], then proceeding to [0][n], [m][n], [m][0], then going inwards:

Example:
	Argument:
		[[a,b,c,d,e],
		 [f,g,h,i,j],
		 [k,l,m,n,o],
		 [p,q,r,s,t],
		 [u,v,w,x,y]]
	Return:
		[a,b,c,d,e, j,o,t,y, x,w,v,u, p,k,f, g,h,i, n,s, r,q, l, m]
"""
def spiral_matrix(arr):
    lis = []
    x = 0
    k = 0
    m = len(arr)
    n = len(arr[0])
    while x < m*n:
        for i in range(k, n-k):
            lis.append(arr[k][i])
            x += 1
        if x >= m*n:
            break
        
        for i in range(1 + k, m - k):
            lis.append(arr[i][n - 1 - k])
            x += 1
        if x >= m*n:
            break
        
        for i in range(1 + k, n-k):
            lis.append(arr[m-1-k][n-1-i])
            x += 1
        if x >= m*n:
            break
        
        for i in range(1 + k, m - 1 - k):
            lis.append(arr[m - 1 - i][k])
            x += 1
            
        k += 1
    return lis


