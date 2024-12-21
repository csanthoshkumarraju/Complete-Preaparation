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
