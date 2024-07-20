'''
Implement all the given functions according to the docstrings. 

There will be 6 function and 6 test cases corresponding to each of the functions
'''

# Find the loss percentage given the buying price and the selling price.
'''
loss = buying - selling
percent = (loss / buying)*100
'''
def loss_percent(bp, sp):
    loss = bp-sp
    percentage = (loss / bp)*100
    return percentage

# Swap the first and last characters of a string.
def swap_first_last(s):

    # check len
    if len(s)<2:
        return s
    return s[-1] + s[1:-1] + s[0]


# Add the first three elements to the end of the list in the same order. Modify the list inplace.
# [1,2,3,4,5] -> [1,2,3,4,5,1,2,3]

def swap_first_three_to_last(l):
    return l.extend(l[:3]) #inplace

# Check if the elements at alternate positions in the tuple are equal.
# Assume even number of elements in the tuple

def are_alternate_postion_equal(t):
    for i in range(0, len(t), 2):
        if t[i] != t[i+1]:
            return False
    return True


# Check if all numbers from a list are present in a set.
# [1,2,3] -> (1,2,3)

def has_all_values(l,s):
    for ele in l:
        if ele not in s:
            return False
    return True


# Swap the key and value for a given key in a dictionary. Modify the dictionary inplace do not return a new dictionary.
def key_value_pair_swap(d,k):
    value = d.pop(k) # key remove -> value stored in value
    d[value] = k
