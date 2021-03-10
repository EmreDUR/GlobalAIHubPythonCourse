# Create two lists.
# One of them should consist of odd numbers and the other one should consist of even numbers.

oddList = list(range(1, 11, 2))
evenList = list(range(2, 12, 2))

# Merge these two lists.
# Multiply all values in the new list by 2.

newList = [i*2 for i in oddList] + [i*2 for i in evenList]

# Use a for loop to print the DATA TYPE of all values in the new list.

for i in newList:
    print(type(i))
