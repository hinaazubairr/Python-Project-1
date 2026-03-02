# Program name: Program7-Lists.py

# if you want to list all your friends in Python, you might think to create a variable for each friend and assign their name to the variable.
# But this will be difficult as you have to remeber all the variable name for each individual friends and apply changes one by one.
# Python enables you to group related items together into a list, which provides you will a better experience to manipulate the collection of items.

# A list is a collection of items that are ordered and can be changed. This means that each item in the list has
# a specific position, and if you want to change the items in the list, you can do so.
# You can have duplicate items in a list.
my_list = [ 'list item 1', 'list item 2']

# Make a list which contains hobbies
hobbies = ['swimming', 'dancing', 'singing']
print(hobbies)

# List length = To determine how many items are in the list.
print(len(hobbies))

# If you want to check whether an item exists in a list.
# using the in keyword. A boolean value returns with either True or False.
print('swimming' in hobbies)
print('running' in hobbies)

# Get index of an item.
# we can use index() method.
print(hobbies.index('dancing'))

# access items in a list
print(hobbies[1])
print(hobbies[-2])

# change item list value
# my_list[index]='new value'
hobbies[1]='running'
print(hobbies)


# add item to a list
# my_list.append('list item 3')
hobbies.append('gaming')
print(hobbies)


#insert item to a list
# you can insert an item into a list at a specific index using insert()
# my_list.insert(1, 'list item 3')
hobbies.insert(5,'eating')
print(hobbies)
# OR
hobbies.insert(hobbies.index('singing'),'eating')
print(hobbies)

#Remove item from a list
# You can remove a specific item from a list using remove()
# my_list.remove('list item1')
hobbies.remove('running')
print(hobbies)

#Remove item at a specified index
# You can remove an item from a list at a specified index using pop()
# If you do not provide an index, Python removes the last item in the list
# my_list.pop()
hobbies.pop(1)
print(hobbies)

# Empty a list
# To empty the entire list so that no items are in the list, use Clear()
# my_list.clear()
hobbies.clear()
print(hobbies)


# Concatenate
# When you combine or concatenate lists, a new list is created thats separate from the initial individual lists.
# my_list = ['list item 1', 'list item 2']
# my_other_list = ['list item A']
# my_new_list = my_list+my_other_list
# use + to concatenate lists and store the list in a new variable.
months = ['Jan', 'Feb', 'March', 'April']
seasons = ['autumn', 'winter', 'spring', 'summer']
months_and_seasons = months+seasons
print(months_and_seasons)


#Extend
# You dont have to create a new list every time you wan to join two lists together.
# You can also add a list to the end of a list using extend()
# my_list = ['list item', 'list item']
# my_other_list = ['list item']
# my_list.extend(my_other_list)
months = ['Jan', 'Feb', 'March', 'April']
seasons = ['autumn', 'winter', 'spring', 'summer']
months.extend(seasons)
print(months)
print(seasons)


# slicing
# Earlier, you accessed the items in a list using the index of an item.
# You can also use the index of an item or items to slice a list.
# Slicing a list will return items within a specified range.
# Create a new list 'rainbow' and store a list of rainbow colors inside the list.
rainbow = ['red','orange','yellow','green','blue','indigo','violet']
# use len() to get the length of the list. The length of the list is needed to help you determine how many items are in the list.
print(len(rainbow))
# To return specific items within a range, pass the list and the index of the item(s) into IDLE.
# the following example returns the 2nd, 3rd and 4th items in rainbow.
print(rainbow[1:4])
# remember that in python, a range will start at the 1st index you specify and end before the last index you specify.
# you can also use slicing to return all list items before or after an index.
print(rainbow[3:])  # all items starting at index 3 are printed.
print(rainbow[:5])  # all items before the item at index 5 are printed.

# negative indexes can be used as well when slicing lists. Python starts at the last item in the list and
# works backward to return the specified items.
print(rainbow[-5:-2])

