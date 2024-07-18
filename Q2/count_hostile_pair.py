'''
Given a list of integers, find the number of hostile_pairs in the given list.

Two positive integers are called hostile if they have no common digits.
'''

# input list
L = [12,78,456]

# create counter
hostile_pairs = 0

# get len of list
n = len(L) 

# check for pairs
for i in range(n):
    for j in range (i+1, n):
        if not set(str(L[i])) & set(str(L[j])):
            hostile_pairs +=1
            
# print output
print(hostile_pairs)
            
