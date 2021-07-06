"""
Challenge #10:

Create a function that applies a discount d to every number in the list.

Examples:
- get_discounts([2, 4, 6, 11], "50%") ➞ [1, 2, 3, 5.5]
- get_discounts([10, 20, 40, 80], "75%") ➞ [7.5, 15, 30, 60]
- get_discounts([100], "45%") ➞ [45]

Notes:
- The discount is the percentage of the original price (i.e the discount of
"75%" to 12 would be 9 as opposed to taking off 75% (making 3)).
- There won't be any awkward decimal numbers, only 0.5 to deal with.
"""
def get_discounts(nums, percentage):
    # Your code here
    # Have to create an empty list, other wise the for loop will iterate over every character. 
    # So we must append everything to this empty list so that the iteration is done on every entry in the list.
    output = []
    for n in nums:
        # Have to use int() functions as to insert percentage AND apply the .replace method to rid ourselves of that symbol
        output.append(n/int(100/int(percentage.replace('%', ''))))
    
    return output

print(get_discounts([2, 4, 6, 11], "50%"))
print(get_discounts([10, 20, 40, 80], "75%"))
print(get_discounts([100], "45%"))
