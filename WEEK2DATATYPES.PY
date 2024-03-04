# Create an empty list called my_list
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40
my_list.extend([10, 20, 30, 40])

#insert the value 15 at the second position in the list 
my_list.insert(1,15)

# extend my_list with another list:[50,60,70]
my_list.extend([50,60,70])

# remove the last element from my_list
my_list.pop()

# sort my_list in ascending order
my_list.sort()

# find and print the index of value 30 in my_list 
index30=my_list.index(30)
print(index30)

# print my list 
print(my_list)