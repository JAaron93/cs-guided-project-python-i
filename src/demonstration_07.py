"""
Challenge #7:

Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the first smallest, the second smallest element is the
second smallest, etc).

Examples:
- nth_smallest([7, 5, 3, 1], 1) ➞ 1
- nth_smallest([1, 3, 5, 7], 3) ➞ 5
- nth_smallest([1, 3, 5, 7], 5) ➞ None
- nth_smallest([7, 3, 5, 1], 2) ➞ 3
"""


def nth_smallest(lst, n):
    # Your code here
    # This conditional statement is here in order to handle lists and 'n' that would throw an 'index out of range' error
    if n > len(lst):
        return None

    lst.sort()   # No need for an explicit 'else:'
    # Give 'n - 1' to index the list in order to grab our answer. Using 'n - 2' or just 'n' won't index it correctly
    # The 'n - 1' uses similar logic to [-1] to grab the last value from a list. This one just grabs the number from
    # the second position of our argument which is the at the end of all our positional arguments, which is only two.
    # So this isn't as easily recognizable. If we had more than two arguments the logic of [n - 1] would be instantly
    # recognizable!
    return lst[n - 1]


print(nth_smallest([7, 3, 5, 1], 2))
print(nth_smallest([1, 3, 5, 7], 3))
print(nth_smallest([1, 3, 5, 7], 5))
print(nth_smallest([7, 3, 5, 1], 2))
