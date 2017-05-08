#Start demo 
def start (name=""):
    name = describe_game(name)
#12. Define a function that returns a string variable / 13. Call the function and print result to the shell
def describe_game(name):
    if name != "": 
        print ("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = raw_input("\What's your name?").capitalize()
                if name != "":
                    print ("\nHello, {}!".format(name))
                    stop = False
        get_answers(name)
        return name
        
    
def get_answers(name):
    stop = True
    while stop:
        choose = raw_input("\nWould you like my answers to the assignment? y/n: ").lower()
        if choose == "y":
            stop = False
            demo_code()
        elif choose == "n":
            print("\n\nToo bad, here they are...\n\n")
            stop = False
            demo_code()
        else:
            print("\nPlease enter 'y' for 'YES' or 'n' for 'NO'...")

# Demo of code
def demo_code():
    # 1. Assign an integer to a variable
    int_variable = 12


    # 2. Assign a string to a variable
    string_variable = "Becky Blue"


    # 3. Assign a float to a variable
    float_variable = 12.6

    print("================================================================================")
    # 4. Use the print f'n and .format() notation to print out assigned variable
    print("\nThe assigned variables are...\nx: {},\nName: \"{}\", \ny: {}\n".format(int_variable,string_variable,float_variable))


    # 5. Use each operator (+,-,*,/,+=,=,%)
    x = 12
    y = 12.6
    print("x += 1 = {}".format(x+1))
    print("x + y = {}".format(x+y))
    print("x - y = {}".format(x-y))
    print("x(y) = {}".format(x*y))
    print("(x)/(y) = {}".format(float(x)/float(y)))
    print("The remainder of (x)/(y) = {}".format(float(x)%float(y)))
    y = x
    print("y = x, making the new value of y:{}".format(y))

    # 6. Use of logical operators: and, or, not
        # AND
    if (x == 12) and (x + 2 >= 2):
        print("\n'and' is true!")
    else:
        print("\n'and' is false!")

       # OR
    if x > 6 or y < 1000:
        print("\n'or' is true!\n")
    else:
        print("\n'or' is false!\n")

        # NOT
    if x+y != 80:
        print("'not' returns true!")
    else:
        print("'not' returns false!")



    #7. Use of conditional statements: if, elif, else
    if y == 12.6:
        print("\nIf statement returns 4\n")
    elif y == 12:
        print("\nElif statement returns 5\n")
    else:
        print("\nElse statement returns x = 3\n")
    

    #8. Use of a while loop
    i = 15
    while True:
        print(i)
        i = i -1
        if i <= 0:
            break

    print("\n")


    #9. Use of a for loop
    for x in range(12,24):
        print(x)

    print("\n")

    #10. Create a list and iterate through that list using a for loop to print each item out on a new line
    demo_list = ["O", "I", "C", "U", "8", "1", "2"]

    for item in demo_list:
        print item

    print("\n")


    #11. Create a tuple and iterate through it using a for loop to print each item out on a new line
    demo_tuple = ("Becky", "Blue", "34", "Vancouver", "WA")

    for tuple in demo_tuple:
        print tuple

    print("\n")


    



if __name__ == "__main__":
    start()

            
 

