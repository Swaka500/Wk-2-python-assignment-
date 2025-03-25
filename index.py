# An empty list
my_list = []

# Appended elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 15 inserted at the second position
my_list.insert(1, 15)

# List extended with another
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# List sorted in ascending order
my_list.sort()

# Find and print the index of value 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)
