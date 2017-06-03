'''
DRILL:

Write your own version of the sorted() method in Python.
This method should take a list as an argument and return a list that is sorted in ascending order.
Call your method passing in the following lists as arguments and print out each sorted list to the shell.
This should be an algorithm that you write.
Do not use .sort() or the sorted() methods in your method.

[67, 45, 2, 13, 1, 998]

[89, 23, 33, 45, 10, 12, 45, 45, 45]

Your sorted lists should look like this when displayed:

[1, 2, 13, 45, 67, 998]

[10, 12, 23, 33, 45, 45, 45, 45, 89]
'''

my_list1 = [67, 45, 2, 13, 1, 998]
new_list1 = []

while my_list1:
    minimum = my_list1[0]
    for x in my_list1: 
        if x < minimum:
            minimum = x
    new_list1.append(minimum)
    my_list1.remove(minimum)    

print (new_list1)


my_list2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]
new_list2 = []

while my_list2:
    minimum = my_list2[0]
    for x in my_list2: 
        if x < minimum:
            minimum = x
    new_list2.append(minimum)
    my_list2.remove(minimum)    

print (new_list2)
