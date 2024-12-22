# single line comment

"""
Multi-line comments
First line
Second line
Third line
"""
#  ***************************************************

# print('Hello World!')  # Calling the print function and printing the text "Hello World" with single quotes ''
# print("Hello World!")  # Calling the print function and printing the text "Hello World" with double quotes ""

# The use of single (' ') and double (" ") quotes is to avoid using extra quotes within the string.
# print('Hi, "Python" ')  # Error: Missing closing quote
# print("Hi, 'Python' ")  # Error: Missing closing quote
# print('Hello, "Python" ')  # Correct: String with double quotes inside single quotes
# print("Hello, 'Python' ")  # Correct: String with single quotes inside double quotes
# print(1+2)  # adding 1 + 2 and printing the sum 3 **** // In - line comment // ****

#  ***************************************************
#                   Python variables
#  ***************************************************

# a = 1  # Assigning the value 1 to the variable 'a'
# print(a)  # Printing the value stored in 'a', which is 1
# print(id(a))# Printing the memory address of the variable 'a'.This address may change during the program's execution.

#  ***************************************************
#                   Python Data Types
#  ***************************************************

"""
A data type defines the type of data that can be stored and manipulated within a program.
Common data types include: 
- Number
- Integer (int)
- Boolean (bool)
- Float
- Complex
- Set
- Dictionary
- Sequence types: list, tuple, string

Example: We cannot store water in a bowl that has holes, 
just as we cannot store certain types of data in incompatible data types.
"""

# Demonstrating Python Data Types
# print(type(1))          # <class 'int'>: Integer data type
# print(type('a'))        # <class 'str'>: String data type
# print(type([]))         # <class 'list'>: List data type
# print(type(()))         # <class 'tuple'>: Tuple data type
# print(type({'a', 'b'}))  # <class 'set'>: Set data type
# print(type({'a': 1}))   # <class 'dict'>: Dictionary data type
# print(type(9.0))        # <class 'float'>: Float data type
# print(type(1 + 9j))     # <class 'complex'>: Complex number data type

# Additional data types that can be included:
# - bytes: Immutable sequence of bytes
# - bytearray: Mutable sequence of bytes
# - memory view: A view of the memory of another object

# Python Data Type Conversion (Implicit/Automatic)
# a = 1  # Integer data type
# b = 2.6  # Float data type
# print(a + b)  # The sum of 'a' and 'b' is in Float data type. Python automatically converts 'a' to Float.

# Python Data Type Casting (Explicit/Manual)
# c = 6  # Integer data type
# d = '10'  # String data type
"""
# print(c + d)  # This will raise an error: unsupported operand type(s) for +: 'int' and 'str'. 
# We cannot add an int and a str.
"""
# print(c + int(d))  # Manually converting 'd' from String to Integer before adding.

#  ***************************************************
#               Python - Literals
#  ***************************************************

"""
Python literals, or constants, are notations for representing fixed values in source code.

-- Types
Integer Literal
Float Literal
Complex Literal
String Literal
List Literal
Tuple Literal
Dictionary Literal

"""
# x = 10  # Example: We are creating a variable 'x' and storing the value 10. This value is a literal.
# y = x * 2  # Here we are calculating a new value based on 'x'. The result is not a literal; it's an expression.
# print(y)  # Output the value of 'y'.

#  ***************************************************
#               Python - Operators
#  ***************************************************

#  ***************************************************
#               Arithmetic Operators
#  ***************************************************

# a = 1  # Assigning the value 1 to the variable 'a'.
# b = 2  # Assigning the value 2 to the variable 'b'.
# c = a + b  # 'a' and 'b' are the operands. '=' is the assignment operator, and '+' is the addition operator.
# print(c)  # Output the sum of 'a' and 'b'.
#
# print(b - a)  # '-' is the subtraction operator; this prints the result of 'b' minus 'a'.
# print(b * a)  # '*' is the multiplication operator; this prints the product of 'b' and 'a'.
# print(b / a)  # '/' is the division operator; this prints the result of 'b' divided by 'a'.
# print(b // a)  # '//' is the floor division operator;
# # this prints the quotient of 'b' divided by 'a' without the remainder.
# print(a ** b)  # '**' is the exponentiation operator; this prints 'a' raised to the power of 'b'.
# print(b % a)  # '%' is the modulus operator; this prints the remainder of 'b' divided by 'a'.
# print(-a)  # Unary negation; this prints the negation of 'a'.

#  ***************************************************
#           Comparison (Relational) Operators
#  ***************************************************

# print(1 == 2)  # Checks if both values are equal.
# print(1 != 2)  # Checks if both values are not equal.
# print(1 < 2)   # Checks if the value on the left is less than the value on the right.
# print(1 > 2)   # Checks if the value on the left is greater than the value on the right.
# print(1 <= 2)  # Checks if the value on the left is less than or equal to the value on the right.
# print(3 >= 2)  # Checks if the value on the left is greater than or equal to the value on the right.

#  ***************************************************
#           Assignment Operators
#  ***************************************************

# a = 10  # Assigning the value 10 to the variable 'a'.
# a += 10  # Adding 10 to 'a'; equivalent to a = a + 10.
# a -= 10  # Subtracting 10 from 'a'; equivalent to a = a - 10.
# a *= 10  # Multiplying 'a' by 10; equivalent to a = a * 10.
# a /= 10  # Dividing 'a' by 10; equivalent to a = a / 10.
# a //= 10  # Floor dividing 'a' by 10; equivalent to a = a // 10.
# a %= 10  # Taking the modulus of 'a' with 10; equivalent to a = a % 10.
# a **= 10  # Raising 'a' to the power of 10; equivalent to a = a ** 10.
# print(a)  # Output the final value of 'a'.

#  ***************************************************
#               Logical Operators
#  ***************************************************

# print(1 == 1 and 2 == 2)  # 'and' -- True if both sides are true; otherwise, False.
# print(1 == 2 or 2 == 2)   # 'or' -- True if at least one side is true; otherwise, False.
# b = 10
# print(not b == 11)        # 'not' -- Prints the opposite of the result; True if b is not equal to 11.

#  ***************************************************
#               Bitwise Operators
#  ***************************************************

# a = 10  # Binary: 1010
# b = 4   # Binary: 0100
#
# print(a & b)  # Bitwise AND: 1010 & 0100 = 0000 (0 in decimal)
# print(a | b)  # Bitwise OR:  1010 | 0100 = 1110 (14 in decimal)
# print(a ^ b)  # Bitwise XOR: 1010 ^ 0100 = 1110 (14 in decimal)
# print(~a)     # Bitwise NOT: ~1010 = ...11110101 (inverts bits, -11 in decimal)
# print(a << 1) # Left Shift: 1010 << 1 = 10100 (20 in decimal)
# print(a >> 1) # Right Shift: 1010 >> 1 = 0101 (5 in decimal)

#  ***************************************************
#               Membership Operators
#  ***************************************************

# string = 'Hello world'
# print('H' in string)        # Checks if 'H' is present in the string; returns True.
# print('a' not in string)    # Checks if 'a' is not present in the string; returns True.

#  ***************************************************
#               Identity Operators
#  ***************************************************

# a = 1
# b = 1
# c = 2
#
# print(a is b)          # Checks if 'a' and 'b' refer to the same object; returns True.
# print(b is not c)      # Checks if 'b' and 'c' do not refer to the same object; returns True.

#  ***************************************************
#               Python Operator Precedence
#  ***************************************************

"""
You can calculate the values based on the operator precedence rules in Python, 
which are as follows (from highest to lowest precedence):

Parentheses ()
Exponentiation **
Multiplication *, Division /, Floor Division //, and Modulus %
Addition + and Subtraction -

"""

# a = 10
# b = 5
# c = 2
# d = 3
# result1 = a + b * c  # 10 + 5 * 2 = 10 + 10 = 20
# result2 = (a + b) * c  # (10 + 5) * 2 = 15 * 2 = 30
# result3 = a - b + c * d  # 10 - 5 + 2 * 3 = 10 - 5 + 6 = 5 + 6 = 11
# result4 = a / b - c + d  # 10 / 5 - 2 + 3 = 2 - 2 + 3 = 3
# result5 = (a + (b - c)) / d  # (10 + (5 - 2)) / 3 = (10+ (3)) / 3 = 13 / 3 = 4.333333
# result6 = (a * (b + c)) / d  # (10 * (5 + 2)) / 3 = (10 * (7)) / 3 = 70/3 = 23.33333
# result7 = (a - (b / c)) + d  # (10 - (5 / 2)) + 3 = (10 - (2.5)) + 3 = 7.5 + 3 = 10.5
# result8 = (a + (b * c)) - d  # (10 + (5 * 2)) - 3 = (10 + (10)) - 3 = 20 - 3 = 17
#
# python_operator_Precedence_output_list = [result1, result2, result3, result4, result5, result6, result7, result8]
# print(python_operator_Precedence_output_list)

#  ***************************************************
#               Python If Elif else
#  ***************************************************

# python control statement
"""
The `if`, `elif`, and `else` statements are fundamental control structures in 
programming that allow for conditional execution of code blocks.
- `if`: This statement evaluates a condition and executes the associated block of code if the condition is true.
- `elif`: Short for "else if," this statement allows for multiple conditions to be checked sequentially. 
If the preceding `if` condition is false, the `elif` condition is evaluated, 
and its block of code is executed if true.
- `else`: This statement provides a fallback option that executes if none of the preceding 
`if` or `elif` conditions are true.
Together, these statements enable decision-making in programs, allowing for dynamic responses based on varying 
inputs or conditions.
"""
# This program calculates the discount based on the amount spent and displays the total bill.

# amount = 400
# if amount > 10000:
#     discount_20_p = amount * 20 / 100
#     bill_amount_20_p = amount - discount_20_p
#     print(f"Congrats! You received a discount of $ {discount_20_p:.2f}. Total bill is {amount} - {discount_20_p} = {bill_amount_20_p:.2f}.")
# elif 5000 <= amount <= 10000:
#     discount_10_p = amount * 10 / 100
#     bill_amount_10_p = amount - discount_10_p
#     print(f"Congrats! You received a discount of $ {discount_10_p:.2f}. Total bill is {amount} - {discount_10_p} = {bill_amount_10_p:.2f}.")
# elif 1000 <= amount < 5000:
#     discount_5_p = amount * 5 / 100
#     bill_amount_5_p = amount - discount_5_p
#     print(f"Congrats! You received a discount of $ {discount_5_p:.2f}. Total bill is {amount} - {discount_5_p} = {bill_amount_5_p:.2f}.")
# else:
#     print(f"Sorry, no discount is available for amounts less than $1000. Your bill amount is {amount:.2f}.")
#
#  ***************************************************
#               Python Nested If
#  ***************************************************
"""
A nested `if` statement is an `if` statement placed inside another `if` statement, 
allowing for more complex conditional logic based on multiple criteria.
"""
# num = 8
# print("num =", num)
# if num % 2 == 0:
#     if num % 3 == 0:
#         print("Divisible by both 3 and 2.")
#     else:
#         print("Divisible by 2 but not by 3.")
# else:
#     if num % 3 == 0:
#         print("Divisible by 3 but not by 2.")
#     else:
#         print("Not divisible by either 2 or 3.")

#  ***************************************************
#               Python match case
#  ***************************************************

"""
A Python match-case statement takes an expression and compares its 
value to successive patterns given as one or more case blocks. 
Only the first pattern that matches gets executed. 
It is also possible to extract components (sequence elements or object attributes) 
from the value into variables.
"""

# def weekday(n):
#     match n:
#         case 0:
#             return "Sunday"
#         case 1:
#             return "Monday"
#         case 2:
#             return "Tuesday"
#         case 3:
#             return "Wednesday"
#         case 4:
#             return "Thursday"
#         case 5:
#             return "Friday"
#         case 6:
#             return "Saturday"
#         case _:
#             return "Not a valid day"
#
#
# print(weekday(0))
# print(weekday('day'))
# print(weekday(2))

#  ***************************************************
#               Python pass Statement
#  ***************************************************
"""
Python pass statement is used when a statement is required syntactically but you do not want 
any command or code to execute. It is a null which means nothing happens when it executes. 
This is also useful in places where piece of code will be added later, 
but a placeholder is required to ensure the program runs without errors.
"""

# for letter in 'Python':
#     if letter == 'h':
#         pass  # The pass statement does nothing
#         print('This is the pass block.')  # Moved this line outside the if block
#     print('Current letter:', letter)
# print("Goodbye!")

"""
Output
-------
Current letter: P
Current letter: y
Current letter: t
This is the pass block.
Current letter: h
Current letter: o
Current letter: n
Goodbye!
"""

#  ***************************************************
#               Python for loop with Break continue
#  ***************************************************
"""
A Python for loop is a control structure that allows you to iterate over a sequence 
(such as a list, tuple, string, or range) and execute a block of code for each item in 
that sequence.
"""

# Normal for loop
# for i in range(1, 11):
#     print(i)

# For loop with if: Print only even numbers
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)

# For loop with break: Exit the loop when i equals 5
# for i in range(1, 11):
#     print(i, end=' ')  # Output: 1 2 3 4 5
#     if i == 5:  # When this condition is met, the loop will end
#         break
# print()  # Print a newline for better output formatting

# For loop with continue: Skip the iteration when i equals 5
# for i in range(1, 11):
#     if i == 5:  # When this condition is met, skip this iteration
#         continue
#     print(i, end=' ')  # Output: 1 2 3 4 6 7 8 9 10
# print()  # Print a newline for better output formatting

#  ***************************************************
#               While loop with Break continue
#  ***************************************************

"""
A while loop is a control structure that repeatedly executes a block of code 
as long as a specified condition is true. It checks the condition before each 
iteration, and if the condition evaluates to false, the loop terminates. 
This allows for dynamic iteration based on changing conditions.
"""

# Normal while loop
# i = 1
# while i < 11:
#     print(i, end=" ")  # Output: 1 2 3 4 5 6 7 8 9 10
#     i += 1
# print()  # Print a newline for better output formatting

# Break while loop
# i = 1
# while i < 11:
#     print(i, end=" ")  # Output: 1 2 3 4
#     i += 1
#     if i == 5:  # When i equals 5, exit the loop
#         break
# print()  # Print a newline for better output formatting

# Continue while loop
# i = 1
# while i < 11:
#     i += 1
#     if i == 5:  # When i equals 5, skip this iteration
#         continue
#     print(i, end=" ")  # Output: 2 3 4 6 7 8 9 10 11
# print()  # Print a newline for better output formatting

"""
A for loop iterates over a sequence (like a list, tuple, or string) or a range, 
executing a block of code for each item. It is typically used when the number 
of iterations is known beforehand.

A while loop repeatedly executes a block of code as long as a specified condition 
is true. It is used when the number of iterations is not known in advance and 
depends on dynamic conditions.
"""

#  ***************************************************
#                   Functions
#  ***************************************************

"""
A function is a block of code that can be called or reused whenever needed.
"""

# def add(a, b):
#     """Add two numbers and return the result."""
#     return a + b  # Return the sum of a and b.
#
#
# # Calling the function in two ways.
# addition = add(1, 2)  # Store the result of add(1, 2) in the variable 'addition'.
# print(addition)
#
# print(add(3, 4))  # Directly print the result without storing it.
#
#
# # The 'mul' function does not use print, it simply performs the calculation.
# def mul(a, b):
#     """Multiply two numbers and return the result."""
#     return a * b  # Return the product of a and b.
#
#
# mul(3, 4)  # This function is called, but the result is not printed.
#
#
# def sub(a, b):
#     """Subtract b from a and print the result."""
#     print(a - b)  # Print the result of a - b.
#     # It's better to use 'return' instead of 'print' for reusability.
#
#
# sub(5, 4)  # Print the result of the subtraction.
#
#
# def div(a, b):
#     """Divide a by b and return the result, or print a message if b is zero."""
#     if b != 0:
#         return a / b  # Exit the code after the return statement.
#         # print('Division completed')  # Do not print because the code exited. This code is unreachable.
#     else:
#         print('Cannot divide by 0')  # Print a message if b is zero.
#
#
# print(div(2, 6))  # Print the result of the division.
#
#
# # Function with type annotations
# def anno(a: int, b: int) -> int:
#     """Add two integers and return the result."""
#     return a + b  # Return the sum of a and b.
#
#
# print(anno(2, 4))  # The arguments must be integers, as per the type annotation.
#
#
# # Keyword arguments
# def kwa(name: str, age: int) -> str:
#     """Return a formatted string with the name and age."""
#     return f"Name: {name} || Age: {age}"
#
#
# print(kwa(name="Abc", age=25))  # Use keyword arguments for clarity.
#
# # Global and local variables
# v1 = 2  # Global variable. Accessible throughout the code.
# v2 = 3  # Global variable.
#
#
# def global_local_variable():
#     """Demonstrate the use of global and local variables."""
#     v3 = 4  # Local variable. Accessible only within this function.
#     v4 = 5  # Local variable.
#
#     print(v1 + v2)  # Access and print the global variables.
#     print(v3 + v4)  # Access and print the local variables.
#
#
# global_local_variable()
# print(v1, v2)  # Access the global variables.
# print(v3, v4)  # Uncommenting this line would result in an error because v3 and v4 are local variables.

#  ***************************************************
#                   strings
#  ***************************************************

"""
In Python, a string is an immutable sequence of Unicode characters. 
Each character has a unique numeric value as per the UNICODE standard. 
But, the sequence as a whole, doesn't have any numeric value even if all the 
characters are digits. To differentiate the string from numbers and other identifiers, 
the sequence of characters is included within single, double or triple quotes in its 
literal representation. Hence, 1234 is a number (integer) but '1234' is a string.
"""

# string = 'Hello, World!'
# string1 = "Welcome to Python"
# print(string, string1)
#
# # Slicing strings: [start:end:step]
# # The 'step' skips characters or directly jumps to the next character.
#
# slicing_string = 'In Python, a string is an immutable sequence of Unicode characters.'
# print(len(slicing_string))  # 67
# # Indexing starts from 0. For 'abc':
# # 0 -> (a), 1 -> (b), 2 -> (c)
# print(slicing_string[0])  # I
# # print(slicing_string[68])  # IndexError: string index out of range
#
# enumerate_string = 'ab cd'
# # 'enumerate' is used for automatic index iteration and access.
# for index, character in enumerate(enumerate_string):
#     print(f"enumerate_string index {index} -> value/character {character}")

"""
----Output---
enumerate_string index 0 -> value/character a
enumerate_string index 1 -> value/character b
enumerate_string index 2 -> value/character     -- counts spaces as well
enumerate_string index 3 -> value/character c
enumerate_string index 4 -> value/character d
"""

# string3 = "Python - Strings"
# print(string3[0:])  # From index 0 to the end: "Python - Strings"
# print(string3[:-1])  # From the beginning to the second-to-last character.
# -1 is a negative index starting from the end.
#
# # The last character is not included in the slice, so it doesn't get printed.
# # *** In for loops or when slicing, the last character is not included or printed.
# print(string3[0::2])  # "Pto tig"
# print(string3[0::3])  # "Ph Sis"
# print(string3[0::4])  # "Po i"
# print(string3[-1:])  # "s"
# print(string3[::-1])  # Reverse the string: "sgnirtS - nohtyP"
#
# # Modifying a string
#
# s1 = "WORD"
# l1 = list(s1)  # Convert the string to a list of characters
# print(l1)
# l1.insert(3, "L")  # Insert 'L' at index 3
# print(l1)
# s1 = ''.join(l1)  # Join the list back into a string
# print(s1)
#
# # Concatenation
#
# sc1 = "abc"
# sc2 = 'def'
#
# print(sc1 + sc2)  # Concatenate sc1 and sc2
# print(sc1 + sc2 + 'ghi')  # Concatenate sc1, sc2, and 'ghi'


#  ***************************************************
#                   Lists
#  ***************************************************
# A list in Python is a collection of data enclosed in square brackets [].
# Characteristics:
# - It is ordered, mutable, and allows duplicates.
# - Elements can be of different data types (heterogeneous).
# heterogeneous_list = [1, 2, 3, 2.5, 'abc', 1 + 9j]
# print(heterogeneous_list)
# # - Lists can be nested, meaning a list can contain other lists.
# nested_list = [4, [3, [1, 2], [3, 4]]]
# print(nested_list)
# # Operations:
# example_list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(example_list)
# # - insert: Insert an element at a specific index.
# example_list.insert(3, 10)  # [1, 2, 3, 10, 4, 5, 6, 7, 8]
# print(example_list)
# b = example_list.insert(5, 100)  # [1, 2, 3, 10, 4, 100, 5, 6, 7, 8]
# print(example_list)
# # - append: Add an element to the end of the list.
# example_list.append(20)
# print(example_list)  # [1, 2, 3, 10, 4, 100, 5, 6, 7, 8, 20]
# # - update: Modify an element at a specific index.
# example_list[5] = 1000
# print(example_list)  # [1, 2, 3, 10, 4, 1000, 5, 6, 7, 8, 20]
# # - delete: Remove an element by value or index.
# del example_list[5]
# print(example_list)  # [1, 2, 3, 10, 4, 5, 6, 7, 8, 20]
# # - pop: Remove and return an element at a specific index.
# example_list.pop(1)  # pop at the index 1
# print(example_list)  # [1, 3, 10, 4, 5, 6, 7, 8, 20]
# example_list.pop()  # pop at the end
# print(example_list)  # [1, 3, 10, 4, 5, 6, 7, 8]
# # - sort: Sort the list in ascending or descending order.
# print(sorted(example_list))  # [1, 3, 4, 5, 6, 7, 8, 10]
# # - len: Get the length of the list.
# print(len(example_list))  # 8
# # - extend: Add multiple elements from another iterable.
# example_list1 = [50, 500, 500]
# example_list.extend(example_list1)
# print(example_list)  # [1, 3, 10, 4, 5, 6, 7, 8, 50, 500, 500]
# # - reverse: Reverse the order of elements in the list.
# print(example_list[::-1])  # [500, 500, 50, 8, 7, 6, 5, 4, 10, 3, 1]
# # - clear: Remove all elements from the list.
# example_list2 = example_list1
# print(example_list2)  # [50, 500, 500]
# example_list2.clear()
# print(example_list2)  # []
# # - slicing: Extract a sublist from a list (e.g., list[start:end]).
# print(example_list[0:3])  # [1, 3, 10]
# # - membership: Check if an element exists in the list using `in` (e.g., item in list).
# print(500 in example_list)  # True
# # - list comprehension: Create a new list based on an existing iterable (e.g., [x for x in list if condition]).
# list_comprehension = [i for i in range(1, 11)]
# print(list_comprehension)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_comprehension1 = [i for i in range(1, 21) if i % 2 == 0]
# print(list_comprehension1)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#
# # - copy: Create a shallow copy of the list.
# list_comprehension2 = list_comprehension1.copy()
# print(list_comprehension2)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# # - index: Find the index of the first occurrence of a value.
# print(list_comprehension2.index(12))  # 5
# # - count: Count the number of occurrences of a value in the list.
# print(list_comprehension2.count(1))  # 0

#  ***************************************************
#                   tuples
#  ***************************************************

# A tuple in Python is a collection of data enclosed in parentheses ().
# Characteristics:
# - It is ordered, immutable, and allows duplicates.
# - Elements can be of different data types (heterogeneous).
# heterogeneous_tuple = (1, 'a', 2.5, 6 + 7j)
# print(heterogeneous_tuple)  # (1, 'a', 2.5, (6+7j))
# # - Tuples can be nested, meaning a tuple can contain other tuples.
# nested_Tuples = (1, (2, (3, (4, 5))))
# print(nested_Tuples)  # (1, (2, (3, (4, 5))))
# # - Tuples are hashable, making them suitable as dictionary keys.
# # - Once created, a tuple cannot be modified (no item insertion, deletion, or update).
#
# # Operations:
# example_tuple = (1, 2, 3, 4, 5, 6)
# print(example_tuple)
# # - len: Get the length of the tuple.
# print(len(example_tuple))  # 6
# # - slicing: Extract a sub tuple from a tuple (e.g., tuple[start:end]).
# print(example_tuple[2:4])  # (3, 4)
# # - membership: Check if an element exists in the tuple using `in` (e.g., item in tuple).
# print(6 in example_tuple)  # True
# # - tuple comprehension: Create a new tuple based on an existing iterable
# # (though tuple comprehensions are more commonly used for generator expressions).
# tuple_comprehension = (i for i in range(1, 10))
# print(tuple_comprehension)  # <generator object <genexpr> at 0x100548040>
# print(type(tuple_comprehension))  # <class 'generator'>
# tuple_comprehension1 = tuple([i for i in range(1,15)])
# print(tuple_comprehension1)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
# print(type(tuple_comprehension1))  # <class 'tuple'>
# # - index: Find the index of the first occurrence of a value.
# print(example_tuple.index(6))  # 5
# # - count: Count the number of occurrences of a value in the tuple.
# print(example_tuple.count(5)) # 1
# # - concatenation: Combine two tuples using the `+` operator.
# tup1 = (1, 2, 3, 4)
# tup2 = (3, 4, 6)
# print(tup1 + tup2)  # (1, 2, 3, 4, 3, 4, 6) # we can not add the different data types
#
# # - repetition: Repeat a tuple multiple times using the `*` operator.
# repetition_tuple = ('Hi') * 4
# print(repetition_tuple)  # HiHiHiHi
#
# # - unpacking: Assign the elements of a tuple to multiple variables.
# unpacking = (1, 2, 3)
# a, b, c = unpacking
# print(a, b, c)  # 1 2 3
# # - nested tuples: Tuples can contain other tuples, forming multidimensional structures.

# Note:
# - Unlike lists, you cannot modify, add, or remove elements in a tuple once it's created.
# - Tuples are typically used for fixed collections of items that should not change.

#  ***************************************************
#                   sets
#  ***************************************************

# A set in Python is a collection of unique, unordered data enclosed in curly braces {}.
# Characteristics:
# - It is unordered, mutable, and does not allow duplicates.
# - Elements must be hashable (immutable types like numbers, strings, tuples).
# - Sets are used to store unique items and are often used for membership tests,
# removing duplicates, and mathematical set operations.
# - A set does not maintain any specific order, meaning the order of elements is not guaranteed.
# order_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(order_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(order_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# # Operations:
# # - add: Add an element to the set (if it doesn't already exist).
# order_set.add(11)
# print(order_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# order_set.add(10)
# print(order_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# # - remove: Remove an element from the set; raises a KeyError if the element doesn't exist.
# # order_set.remove(20)  #  KeyError: 20
# order_set.remove(10)
# print(order_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11}
# # - discard: Remove an element from the set, but does not raise an error if the element doesn't exist.
# order_set.discard(11)
# print(order_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
# order_set.discard(1100)
# print(order_set)  # {2, 3, 4, 5, 6, 7, 8, 9}
# # - pop: Remove and return an arbitrary element from the set (since sets are unordered).
# order_set.pop()
# print(order_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
# # - clear: Remove all elements from the set.
# order_set1 = order_set
# print(order_set1)  # {2, 3, 4, 5, 6, 7, 8, 9}
# order_set1.clear()
# print(order_set1)  # set()
# print(order_set)   # set()
# # - len: Get the number of elements in the set.
# order_set2 = {1, 2, 3, 4, 5, 6, 7, 8}
# print(len(order_set2))  # 8
# # - union: Return a new set with all elements from both sets (using `|` or `union()` method).
# order_set3 = {6, 7, 8, 9, 10, 11, 12}
# print(order_set2.union(order_set3))  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
# print(order_set2 | order_set3)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
#
# # - intersection: Return a new set with elements common to both sets (using `&` or `intersection()` method).
# print(order_set2.intersection(order_set3))  # {8, 6, 7}
# print(order_set2 & order_set3)  # {8, 6, 7}
# # - difference: Return a new set with elements in the first set but not in the second
# # (using `-` or `difference()` method).
# print(order_set2.difference(order_set3))  # {1, 2, 3, 4, 5}
# print(order_set2 - order_set3)  # {1, 2, 3, 4, 5}
# # - symmetric_difference: Return a new set with elements in either of the sets,
# # but not both (using `^` or `symmetric_difference()` method).
# print(order_set2.symmetric_difference(order_set3))  # {1, 2, 3, 4, 5, 9, 10, 11, 12}
# print(order_set2 ^ order_set3)  # {1, 2, 3, 4, 5, 9, 10, 11, 12}
# # - subset: Check if a set is a subset of another set (using `<=` or `issubset()` method).
# print(order_set2 <= order_set3)  # False
# print(order_set2.issubset(order_set3))  # False
# # - superset: Check if a set is a superset of another set (using `>=` or `issuperset()` method).
# print(order_set2 >= order_set3)  # False
# print(order_set2.issuperset(order_set3))  # False
#
# # - membership: Check if an element exists in the set using `in` (e.g., item in set).
# print(6 in order_set3)  # True
# # - set comprehension: Create a new set based on an existing iterable (e.g., {x for x in iterable if condition}).
# set_comprehension = {i for i in range(1, 11)}
# print(set_comprehension)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Note:
# - Sets automatically remove duplicates when you add elements.
# - Since sets are unordered, indexing, slicing, or other sequence-like behavior is not supported.
# - Sets can be used to perform mathematical set operations like union, intersection, and difference.

#  ***************************************************
#                   dictionary
#  ***************************************************


# A dictionary in Python is a collection of key-value pairs enclosed in curly braces {}.
# Characteristics:
# - It is unordered (insertion order is preserved starting from Python 3.7+).
# - It is mutable, meaning you can modify, add, or remove key-value pairs.
# - Keys must be immutable (e.g., strings, numbers, tuples), but values can be of any data type.
# - Keys are unique within a dictionary, but values can be duplicated.
# - Dictionaries are optimized for fast lookups by key.

# Example dictionary
# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
#
# # Operations:
# # - get: Retrieve the value for a specific key (e.g., dict.get(key)).
# print(my_dict.get("name"))  # Output: Alice
#
# # - setdefault: Return the value of a key if it exists, otherwise set it to a default value.
# print(my_dict.setdefault("age", 25))  # Output: 30 (age exists, so it returns the value 30)
# print(my_dict.setdefault("country", "USA"))  # Output: USA (country doesn't exist, so it adds it)
#
# # - keys: Return a view object of all the keys in the dictionary (e.g., dict.keys()).
# print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city', 'country'])
#
# # - values: Return a view object of all the values in the dictionary (e.g., dict.values()).
# print(my_dict.values())  # Output: dict_values(['Alice', 30, 'New York', 'USA'])
#
# # - items: Return a view object of all key-value pairs as tuples (e.g., dict.items()).
# print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 30),
# ('city', 'New York'), ('country', 'USA')])
#
# # - update: Update the dictionary with key-value pairs from another dictionary or
# # iterable (e.g., dict.update(other_dict)).
# my_dict.update({"gender": "Female", "age": 32})  # Update 'age' and add 'gender'
# print(my_dict)  # Output: {'name': 'Alice', 'age': 32, 'city': 'New York', 'country': 'USA', 'gender': 'Female'}
#
# # - pop: Remove and return a key-value pair by key (e.g., dict.pop(key)).
# age = my_dict.pop("age")  # Removes 'age' and returns its value
# print(age)  # Output: 32
# print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York', 'country': 'USA', 'gender': 'Female'}
#
# # - popitem: Remove and return an arbitrary key-value pair (e.g., dict.popitem()).
# item = my_dict.popitem()  # Removes and returns an arbitrary item
# print(item)  # Output: ('gender', 'Female') (Output may vary)
# print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York', 'country': 'USA'}
#
# # - del: Delete a key-value pair from the dictionary (e.g., del dict[key]).
# del my_dict["city"]
# print(my_dict)  # Output: {'name': 'Alice', 'country': 'USA'}
#
# # - clear: Remove all key-value pairs from the dictionary.
# my_dict.clear()
# print(my_dict)  # Output: {}
#
# # - len: Get the number of key-value pairs in the dictionary.
# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# print(len(my_dict))  # Output: 3
#
# # - membership: Check if a key exists in the dictionary using `in` (e.g., key in dict).
# print("name" in my_dict)  # Output: True
# print("address" in my_dict)  # Output: False
#
# # - comprehension: Create a new dictionary based on an existing iterable
# # (e.g., {k: v for k, v in iterable if condition}).
# squared_dict = {x: x ** 2 for x in range(5)}
# print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
#
# # - merge: Merge two dictionaries (using `|` in Python 3.9+ or `update()` method).
# dict1 = {"name": "Alice", "age": 30}
# dict2 = {"city": "New York", "gender": "Female"}
# merged_dict = dict1 | dict2  # Using the `|` operator (available in Python 3.9+)
# print(merged_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'gender': 'Female'}
#
# # - copy: Create a shallow copy of the dictionary (e.g., dict.copy()).
# copied_dict = my_dict.copy()
# print(copied_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Note:
# - Dictionaries are often used for associative arrays, where a key is mapped to a value.
# - Since dictionaries are mutable, you can modify their contents (add, remove, update).
# - Dictionaries do not allow duplicate keys; if you try to assign a value to an
# existing key, it will overwrite the old value.
# - Keys in dictionaries are unordered, but starting from Python 3.7+, dictionaries preserve the insertion order.

#  ***************************************************
#                   Array
#  ***************************************************

# An array in Python is a collection of elements of the same type, defined using the 'array' module.
# Characteristics:
# - It is ordered, mutable, and allows duplicates.
# - All elements in an array must be of the same data type (homogeneous).
# - Arrays are more space-efficient than lists, particularly for large amounts of numerical data.
# - Elements are accessed using zero-based indexing, similar to lists.
# - Arrays are defined using the 'array' module.

# import array
#
# # Example of creating an array
# arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' represents integer type, and the list is the data.
#
# # Operations:
# # - append: Add an element to the end of the array.
# arr.append(6)
# print(arr)  # Output: array('i', [1, 2, 3, 4, 5, 6])
#
# # - insert: Insert an element at a specific index in the array.
# arr.insert(2, 10)  # Insert 10 at index 2
# print(arr)  # Output: array('i', [1, 2, 10, 3, 4, 5, 6])
#
# # - remove: Remove the first occurrence of a specified value.
# arr.remove(10)  # Removes the first occurrence of 10
# print(arr)  # Output: array('i', [1, 2, 3, 4, 5, 6])
#
# # - pop: Remove and return the element at a specific index.
# popped_element = arr.pop(3)  # Removes and returns the element at index 3 (value 4)
# print(popped_element)  # Output: 4
# print(arr)  # Output: array('i', [1, 2, 3, 5, 6])
#
# # - index: Find the index of the first occurrence of a value.
# index_of_5 = arr.index(5)  # Returns the index of the value 5
# print(index_of_5)  # Output: 3
#
# # - count: Count the number of occurrences of a value.
# count_of_5 = arr.count(5)  # Count how many times 5 appears in the array
# print(count_of_5)  # Output: 1
#
# # - reverse: Reverse the order of elements in the array.
# arr.reverse()
# print(arr)  # Output: array('i', [6, 5, 3, 2, 1])
#
# # - slice: Extract a portion (sub-array) of the array using slicing.
# sub_array = arr[1:4]  # Get elements from index 1 to 3 (excluding index 4)
# print(sub_array)  # Output: array('i', [5, 3, 2])
#
# # - len: Get the number of elements in the array.
# print(len(arr))  # Output: 5
#
# # - membership: Check if a value exists in the array using 'in'.
# print(3 in arr)  # Output: True
# print(10 in arr)  # Output: False
#
# # - extend: Add elements from an iterable to the end of the array.
# arr.extend([7, 8, 9])
# print(arr)  # Output: array('i', [6, 5, 3, 2, 1, 7, 8, 9])
#
# # - tolist: Convert the array to a regular Python list.
# arr_list = arr.tolist()
# print(arr_list)  # Output: [6, 5, 3, 2, 1, 7, 8, 9]
#
# # - buffer_info: Returns the address and length of the array buffer.
# print(arr.buffer_info())  # Output: (address, length) - this is a system-specific value.


#  ***************************************************
#                   Python - OOP Concepts
#  ***************************************************

# Object: A real-world entity, created from a class. An instance of a class.
# Class: A blueprint for creating objects. It defines the properties and behaviors (methods) of objects.
# Encapsulation: The bundling of data (attributes) and methods (functions)
# that operate on the data into a single unit or class.
#              It also involves restricting access to some of an object's
#              components by making variables private and using getter/setter methods.
# Abstraction: Hiding the complex implementation details and showing only the necessary features of an object.
#              It helps in reducing complexity and allows focusing on high-level functionality.
# Inheritance: Acquiring properties and behaviors (methods) of a parent class and allowing for code reuse.
#              A subclass can extend or modify the behavior of a parent class.
# Polymorphism: The ability to use the same method name with different behaviors.
#               It allows methods to behave differently based on the object type calling them.
#               Example: The `len()` function, which works on different data types
#               (e.g., string, list, tuple) to return the length.

# from abc import ABC, abstractmethod  # Corrected 'abstractclassmethod' to 'abstractmethod'
#
#
# class Animal(ABC):  # Creating the Animal class, inheriting from ABC to make it an abstract class
#
#     def __init__(self, name):  # Class constructor, initializing the variables.
#         self.__name = name  # Private variable for encapsulation
#         # self.a = a  # Public variable (not used in this example)
#         # self._b = b  # Protected variable (not used in this example)
#
#     def get_name(self):  # Getter method to access the private name attribute
#         return self.__name
#
#     @abstractmethod  # Corrected the method decorator to 'abstractmethod'
#     def sound(self):  # Abstract method, to be implemented by subclasses
#         pass
#
#
# class Cat(Animal):  # Inheriting from Animal class
#     def sound(self):  # Polymorphism: Overriding the sound method in the Cat class
#         return "Meow Meow"
#
#
# # Creating an instance/object of the Cat class
# cat = Cat("Cheela")
# print(cat.sound())  # Output: Meow Meow

# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     @abstractmethod
#     def type(self):
#         pass
#
#
# class Bus(Vehicle):
#     def type(self):
#         return "Passenger"
#
#
# class Truck(Vehicle):
#     def type(self):
#         return "Transport"
#
#
# class Car(Vehicle):
#     def type(self):
#         return "Personal"
#
#
# bus = Bus("Volvo")
# truck = Truck("Tata")
# car = Car("Tesla")
#
# print(f"Vehicle Name :- {bus.get_name()} , type :- {bus.type()}")
# print(f"Vehicle Name :- {truck.get_name()} , type :- {truck.type()}")
# print(f"Vehicle Name :- {car.get_name()} , type :- {car.type()}")

# Method Overloading Concept in Python - Using default parameters
# In Python, we can simulate method overloading using default parameters.
# The method can be called with different numbers of arguments,
# and the default values will be used if the arguments are not provided.

# def add(a=0, b=0, c=0, d=0, e=0):
#     """
#     Adds up to five numbers with default values of 0 for each parameter.
#     This simulates method overloading by allowing a different number of arguments.
#     """
#     return a + b + c + d + e
#
#
# # Calling the 'add' function with varying numbers of arguments
# print(add(1, 2))        # Outputs: 3 (1 + 2 + 0 + 0 + 0)
# print(add(1, 2, 3))     # Outputs: 6 (1 + 2 + 3 + 0 + 0)
# print(add(1, 2, 3, 4))  # Outputs: 10 (1 + 2 + 3 + 4 + 0)
# print(add(1, 2, 3, 4, 5))  # Outputs: 15 (1 + 2 + 3 + 4 + 5)


#  ***************************************************
#                   Python Errors & Exceptions
#  ***************************************************

"""
Exception handling in Python refers to managing runtime errors that may occur
during the execution of a program. In Python, exceptions are raised when errors
or unexpected situations arise, such as division by zero, trying to access a
file that does not exist, or attempting to perform an operation on incompatible
data types.
"""

# Python - try-except Block

# Handling division by zero error using try-except
# try:
#     print(10 / 0)  # Attempt to divide by zero
# except ZeroDivisionError:  # Catch ZeroDivisionError if it occurs
#     print("Cannot divide by zero.")  # Inform the user about the error
#
# # Handling unsupported operand types during addition
# try:
#     print(1 + '3')  # Attempt to add an integer and a string
# except TypeError:  # Catch TypeError if it occurs
#     print("Unsupported operand type(s) for +: 'int' and 'str'")  # Inform the user about the error
#
# # Python - try-finally Block
# # The finally block always executes, regardless of whether an exception occurred or not
#
# try:
#     print(10 / 0)  # Attempt to divide by zero
# except ZeroDivisionError:  # Catch ZeroDivisionError if it occurs
#     print("Cannot divide by zero.")  # Inform the user about the error
# finally:
#     print("This code always runs.")  # This block will always execute
#
# # Python - Raising Exceptions
# # Demonstrating how to manually raise an exception
#
# list1 = [1, 2, 3, 4]
#
# try:
#     print(list1[9])  # Attempt to access an index that doesn't exist
#     raise IndexError('List index out of range')  # Manually raise an IndexError (this line will not be reached)
# except IndexError as IE:  # Catch IndexError if it occurs
#     print(IE)  # Inform the user about the error
#
# # Python - User-defined Exception
#
# # Custom exception to handle invalid withdrawal amounts
# class InvalidAmount(Exception):
#     """Exception raised for invalid withdrawal amounts."""
#     pass
#
# def withdraw_amount(withdraw, balance):
#     """
#     Withdraws a specified amount from the balance. If the withdrawal amount is greater than the balance,
#     an InvalidAmount exception is raised.
#     """
#     if withdraw <= balance:  # Check if withdrawal amount is less than or equal to the balance
#         remaining_balance = balance - withdraw  # Calculate remaining balance after withdrawal
#         return f"Amount {withdraw} debited. {balance} - {withdraw}. Remaining balance: {remaining_balance}"
#     else:
#         # Raise a custom exception if withdrawal amount exceeds the balance
#         raise InvalidAmount(f"You do not have enough funds to withdraw. Available: {balance}, Requested: {withdraw}")
#
# # Example usage of the withdraw_amount function with exception handling
# try:
#     print(withdraw_amount(100, 1000))  # Attempt to withdraw an amount
# except InvalidAmount as IA:  # Catch the custom InvalidAmount exception
#     print(IA)  # Print the error message from the exception

