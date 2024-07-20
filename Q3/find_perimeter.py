'''
Find the perimeter of a bar graph given the heights at each bar.

Assume width of each bar is 1 unit and height is atleast 1 unit and the heights of each bar is given as integers.

Example
Input
5 3 4 1 3 2 5

Output : 36


Perimeter 5+1+2+1+1+1+3+1+2+1+1+1+3+1+5+7 = 36
'''

# list input
L = [5, 3, 4, 1, 3, 2, 5]

# len list
n = len(L)

# variabes
perimeter = 0

#1st bar input
perimeter += L[0]+1

# define loop
for i in range(1, n):
    diff = abs(L[i]- L[i-1])
    perimeter += diff + 1

#add last value and no of the bars
perimeter  += L[-1]+n

print(perimeter)
