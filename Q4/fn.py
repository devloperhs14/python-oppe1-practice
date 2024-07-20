
# fn 1 - calcualate loss%
def loss_percent(bp, sp):
    """Calculate the loss percentage."""
    loss = bp - sp
    return (loss / bp) * 100

# fn 2 - swap 1st and last element
def swap_first_and_last_chars(s):
    """Swap the first and last characters of a string."""
    if len(s) < 2:
        return s
    return s[-1] + s[1:-1] + s[0]

# fn 3 - Add 1st three element to Last
def add_first_three_items_to_the_last(l):
    """Add the first three elements to the end of the list."""
    l.extend(l[:3])


# fn 4 - Alternate postion equality check
def are_alternate_positions_equal(t):
    """Check if elements at alternate positions in the tuple are equal."""
    for i in range(0, len(t), 2):
        if t[i] != t[i+1]:
            return False
    return True


# fn 5 - Check list values present as set
def has_all_values(l, s):
    """Check if all numbers from the list are present in the set."""
    for item in l:
        if item not in s:
            return False
    return True


# fn 6 -swap key value pair
def swap_key_and_value(d, k):
    """Swap the key and value for the given key in the dictionary."""
    value = d.pop(k)
    d[value] = k





























# Example usage - 1
print(loss_percent(10, 8))  # Output: 20.0
print(loss_percent(20, 15))  # Output: 25.0


# Example usage -2
print(swap_first_and_last_chars("hello"))  # Output: 'oellh'
print(swap_first_and_last_chars("world"))  # Output: 'dorlw'


# Example usage-3
lst = [1, 2, 3, 4, 5]
add_first_three_items_to_the_last(lst)
print(lst)  # Output: [1, 2, 3, 4, 5, 1, 2, 3]


# Example usage -4 
print(are_alternate_positions_equal((1, 1, 2, 2, 3, 3)))  # Output: True
print(are_alternate_positions_equal((1, 2, 3, 4, 5, 6)))  # Output: False


# Example usage - 5
print(has_all_values([1, 2, 3, 4], {1, 2, 3, 4}))  # Output: True
print(has_all_values([1, 2, 3, 1], {2, 3}))  # Output: False


# Example usage
d = {'a': 1, 'b': 2, 'c': 3}
swap_key_and_value(d, 'b')
print(d)  # Output: {'a': 1, 2: 'b', 'c': 3}

d = {1: 'a', 2: 'b', 3: 'c'}
swap_key_and_value(d, 2)
print(d)  # Output: {1: 'a', 'b': 2, 3: 'c'}
