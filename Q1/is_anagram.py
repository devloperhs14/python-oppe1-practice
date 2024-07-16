'''
Given a list of words, check if all the words are anagrams. Assume words are lowercase.

Two words are anagrams of each other if each word can be obtained by rearranging the letters in the
other word.
'''

# assumes list is given
# store 1st value in sorted manner
ref = sorted(L[0])

# create counter and run loop over list
all_anagrams = True
    # check for the store and reference being same
for words in L:
    if sorted(words) != ref:
        all_anagrams = False
        break;

# output results
if all_anagrams:
    print("True")
else:
    print("False") 

# home work - function










#driver code
