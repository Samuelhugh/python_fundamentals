my_new_favorite_language = 'Python'


# Declaring a variable and Initializing a Number
num1 = 42
# Declaring a variable and Initializing a Decimal/Float
num2 = 2.3
# Declaring a variable and Initializing a Boolean
boolean = True
# Declaring a variable and Initializing a String
string = 'Hello World'
# Declaring a variable and Initializing a List
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# Declaring a variable and Initializing a Dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# Declaring a variable and Initializing a Tuple. Also Tuples are ordered and NOT changeable
fruit = ('blueberry', 'strawberry', 'banana')
# Print the specified message to the screen or other standard output device and using the type() function
print(type(fruit))
# Print the specified message to the screen or other standard output device the List (pizza_toppings) of index 1
print(pizza_toppings[1])
# Adding a single item to the existing List. .append() does not return a new List of items but will modify the Original List by Adding the item to the end of the List
pizza_toppings.append('Mushrooms')
# Print the specified message to the screen or other standard output device the Dictionary for the Key-Value Pair for name
print(person['name'])
# Setting the person Dictionaries Key-Value pair for name to george. Also know as Changing the Values for an Dictionary
person['name'] = 'George'
# Adding to person Dictionary a Key-Value pair: Setting eye_color to blue
person['eye_color'] = 'blue'
# Print the specified message to the screen or other standard output device the Tuple of index 2
print(fruit[2])

# If statement/conditional/check asking a Boolean question if num1 is greater than 45
if num1 > 45:
# Print the specified message to the screen or other standard output device if the IF check is true
    print("It's greater")
# Else statement/conditional saying to do this IF the other if statements/conditional/checks are false
else:
# Print the specified message to the screen or other standard output device for the else statement
    print("It's lower")

# A separate IF check asking a Boolean question if the Length of the variable string is less than 5
if len(string) < 5:
# Print the specified message to the screen or other standard output device if the IF check is true
    print("It's a short word!")
# A else if check asking a Boolean question if the length of the variable string is greater than 15
elif len(string) > 15:
# Print the specified message to the screen or other standard output device if the else if check is true
    print("It's a long word!")
# A Else statement IF the other IF checks return false
else:
# Print the specified message to the screen or other standard output device
    print("Just right!")

# A FOR LOOP using the range() built-in function. This says that I to set the variable "x" to the current loop that I am currently on and want to count one by one(because when the STEP is not defined in a range() the default incrementing is 1) starting from 0 (because when a START is not defined in the range() built-in function the default is 0) and I want to continue until I am one less than the STOP(5) value. The STOP value is the only value that is required with the range() built-in function
for x in range(5):
# Printing the specified message to the screen or other standard output device
    print(x)
# A for loop commonly referred to as a range Loop when using the built-in range() function, This is telling me that I want to set the variable "x" to the START(2) for the loop that I am currently on and I want to count one by one(because the STEP is not defined so the incrementing is defaulted to 1) up until I reach the STOP(5)
for x in range(2,5):
# Print the specified message to the screen or other standard output device
    print(x)
# A Range Loop (A "for loop" using the "range()" function), This ONE is saying "for", 'for the variable x I want to set it to START(2) for the current loop that I am currently on', "("in" Keyword used to check if a value is present in a sequence(list, range, string, etc), Also "in" is used to iterate through a sequence in a range loop)", I want to count up until I hit one less than the STOP(10) value and I also want to increment each time by the STEP(3) value for "range(start,stop,step)".
for x in range(2,10,3):
# Print the specified message to the screen or other standard output device
    print(x)

# Declaring a variable and Initializing a Number For the While loop
x = 0
# Same "While Loop" that I used in Javascript. It is asking a Boolean question IF x is less than 5.
while(x < 5):
# Print the specified message to the screen or other standard output device
    print(x) 
# A piece of Code that is inside the "while loop" saying to set "x" to itself and then add one (x = x + 1)
    x += 1

# This is going to "pop" the last value from a Array, Object, and lists.
pizza_toppings.pop()
# This piece of Code is specifying to ".pop" the index at 1.
pizza_toppings.pop(1)

# Print the specified message to the screen or other standard output device
print(person)
# This is going to ".pop" the "eye_color" for the person "Object"
person.pop('eye_color')
# Print the specified message to the screen or other standard output device
print(person)

# This is a for Loop is saying, "for" variable toppings "in" the List 'pizza_toppings' Iterate through the List 'pizza_toppings' one index at a time. Remember that in python for their for loops when the start is not defined it is defaulted to zero. And when the incrementing is not defined then it is defaulted to 1.
for topping in pizza_toppings:
# A IF check asking a Boolean question saying "if topping is equal(==) to the string 'pepperoni' then do what is in my code block"
    if topping == 'Pepperoni':
# This is A continue statement, saying if the IF check is true then "continue" then STOP the CURRENT iteration. and START the NEXT iteration
        continue
# THIS is Just A print function Saying to print the specified message to the screen or other standard output device
    print('After 1st if statement')
# A separate IF check but Asking a Boolean question. Saying if the variable "topping" is equal(==) to the string 'Olives' then do what is in my code block
    if topping == 'Olives':
# This is A break statement in the IF checks' code block, and what this means is to stop the loop
        break

# This is a function definition/function with a function name "print_hello_ten_times()" with no parameter/variable attached to it. The ":" colons signify the start of the code block
def print_hello_ten_times():
# A for loop using the range() built-in function. This loop is saying I want to set "num" to the current loop that I am currently on and to then count one by one up until I reach one less than the STOP(10), starting from 0(because if no START is defined the default is 0), and if no STEP is defined then the default incrementing is 1
    for pointer_var in range(10):
# This is a print message saying to print the specified message to the screen or other standard output device
        print('Hello')
# This is the function call for the function definition/function "Print_hello_ten_times()"
print_hello_ten_times()

# This is a function definition/function with a function name "print_hello_x_times(x)" WITH a parameter/variable this time named "x"
def print_hello_x_times(x):
# This is a for loop using the range() built-in function. Also referred to as a "range loop". This loop is saying to I want to set "the variable num" to the current loop that I am currently on, and then I want to count one by one up until I am one less then the STOP value is
    for var_pointer in range(x):
# A print function saying print the specified message to the screen or other standard output device
        print('Hello')
# A function call, calling the function "print_hello_x_times(4)" and passing in the argument "4" to the function definition/function parameter/variable.
print_hello_x_times(4)

# Another function definition/function with the function name "print_hello_x_or_ten_times(x = 10)" with A "Default parameter value of 10 (represented with x = 10)"
def print_hello_x_or_ten_times(x = 10):
# A for loop that is also commonly referred to as a range loop, because it is using the range() built-in function. This for loop is saying I want to set the variable "num" to the the loop I am currently on and I want to start my count with 0 because no START is defined, and I want to count all the way up until one less then STOP (whatever value thats going to be)
    for num in range(x):
# print function saying print the specified message to the screen or other standard output device
        print('Hello')
# This is a function call, calling the function definition/function "print_hello_x_or_ten_times()" BUT IS NOT PASSING ANY ARGUMENT to the Function definition/Function so that means that because the Function definition/Function already has a "Default Parameter" this means that when the Function "print_hello_x_or_ten_times()" is called that the Function will keep whatever the "Default Parameter" is
print_hello_x_or_ten_times()
# This is also a function call, calling the "print_hello_x_or_ten_times(4)" Function definition/Function AND PASSING THE ARGUMENT "4" to the Function def "print_hello_x_or_ten_times(x = 10)", So this means that when "4" gets passed into the Function def "print_hello_x_or_ten_times(x = 10)" that the "Default Value" will now be set to incoming Argument Setting "print_hello_x_or_ten_times" "Default Value" to "4" so the finished product should look like this "print_hello_x_or_ten_times(x = 4)"
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) # NameError - Not defined
# num3 = 72 # Good
# fruit[0] = 'cranberry' # Tuples are not Changeable so you can't add to it with this code. (TypeError)
# print(person['favorite_team']) # There are only four Key/Value pairs within the person Dictionary{}, and no pair relating to 'favorite_team' in the person Dictionary{}. (KeyError)
# print(pizza_toppings[7]) # The 'pizza_toppings' list [] only has four indexes in its' list[], So You cannot access a seventh index if there is not one. (IndexError)
#   print(boolean) # This is a IndentationError and this happens when the spaces or tabs are not placed properly
# fruit.append('raspberry') # This happens because You cannot add to a Tuple because they are NOT changeable. but there are some  workarounds for it. (AttributeError)
# fruit.pop(1) # This is because Tuples are NOT changeable. (AttributeError)