#Create list of numbers
number_list = [1,2,3,4,5]
empty_number_list = []
#Loop each number in number_list
for x in number_list:
    '''#Print each number to the power of 2
    print x**2'''
    #Append each number to the power of 2
    #to the empty_number_list
    empty_number_list.append(x**2)
print empty_number_list
