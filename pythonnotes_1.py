"""
What is Python?

Python is high level, interpretted, object oriented language that focuses on
clarity and readability. Be explicit over implicit. This makes it easy to
learn and understand the language. 

Python is designed for rapid development. It is not compiled, so you can quickly
edit and rerun your scripts when developing. Python requires fewer lines of code
to do more work for you than other languages. The built in tools often let you
build creative solutions in fewer lines. It handles all its own memory
management and uses a powerful exception based error handling system to make
sure the programmer doesnt have to worry about segfaults. Errors are usually
given with a detailed stack trace so that you dont need complicated debugging 
methods.

Python also has a growing number of packages out there to aid in development.
There are many science and math based routines that can integrated into
projects for faster development and performance.
"""

"""
Python general syntax

Statements are assumed to be terminated by new lines and starting a new line
creates a new statement. Multiline statements are possible by adding a \ to 
the end of line. The statement will be continued on the next line. Semicolons 
are not needed in python, but will compile. Semicolons are the only way to 
achieve multiple statements in one line, but it is rarely necessary. 

Curly braces are only used for dictionaries. Scope is determined through
indentation as will be further demonstrated. Indentation is strictly
enforced so it is recommended to convert tabs to spaces. Using tabs to indent
does work, but mixed tabs/spaces has bitten me in the past when finding
indentation errors.

Typically, programmers try to adhere to the PEP-8 style guide to format their
code. Stylistically, class names in object oriented programming start with capital
letters. Everything else is typically lowercase. under_scores in variable names
are prefered over camelCase.

Python will not allow you to use override reserved keywords. The list of these
are easily found online. For example:
https://docs.python.org/2.5/ref/keywords.html

Python has two forms of comments. Multiline comments can be within triple quotes.
Single line comments start with a #.

Multiline assignment is possible.

"""

x = 1 #this is a statement

y = 2 + \
    1 #multline statement

a = 'a';b = 'b' #multiple statements on one line

prefered_variable_name = "extended variable names using underscores are prefered"

""" This is a comment"""
#This is also a comment

a,b,c,d = 1,2,3,4 #multiline assignment



"""
Python types

Python is dynamically typed and bound which means that variable
type is assigned at runtime. This means you can create variables
on the fly and Python will figure out the type for you.

The five standard Python data types are:
    Number
    Boolean
    String
    List
    Tuple
    Dictionary


Standard python has four number types: int, long, float, and complex.

Booleans can be True or False.

Strings can use both single or double quotes. As well as comments, 
triple quotes strings can be used for multiline long strings.

Lists are Python's most general and useful storage type. Lists can be used
for very powerful operations. They can be added to, removed from, and sliced
very easily. Lists can store any data type or object and lists allow for 
mixed type storage.

Tuples are similar to lists, however they cannot be updated.
This permanence is known as being immutable. They are like read only lists.

Dictionaries are key:value pairs. Very useful for creating named pairs. 
Dictionary keys can be any immutable type such as strings, number, or
even tuples. Values can be any Python type or object.

Type can be checked against or determined with the type() function.

A value representing a null value, or null object is the None type. Use
None to represent nothing.

"""

int_var = 10 #int
long_var = 100000L #Capital 'l' creates long int

float_var = 10.0 #64 bit floats
float_var = float(10) #float conversion from int

complex_var = 1 + 2j #complex types exist too

bool_var = True

string_var = "This is a string" #string var
string_var = str(float_var) #create a string converted from float_var

list_type = [0,1,"abc",7.63,2.6+3.14j] #storing values in a list

dict_type = {"one" : 1,
             "two" : 2,
             "complex" : 1 + 2j,
             ('x','y') : (1,1)
            }

type_tbd = type(list_type)

none_type = None

"""
Python branch statements

If-then statements use a colon to signal the condition and indentation to resolve
scope.

Be careful when testing equivalence. Make sure you know if you are comparing value
or object reference. == or != tests value equality where as 'is' or 'is not' tests
object identity. More on this in further notes.

Logical not, and, and or use words instead of the C operators.

"""

string1 = "this is a string"
string2 = "this is a different string"

if string1 == string2:
    result = "string values are equal"
elif string1 is string2:
    result = "reference to strings are equal"
else:
    result = "strings are completely different"


a,b,c,d = 1,1,1,1
if not ((a and b) or (c and d)): #showing logical operators in if
    pass #pass is a nop


"""
Python loops

Python has both while and for loops.

There is no do-while loop as there is in C.

Python makes use of a clever concept called iterators. Iterators represent the
elements of data types being looped over. This means we can more conveniently
loop over things like tuples, lists, or dictionaries without having to keep 
track of indexing.

The 'in' keyword is very powerful. It lets us quickly and easily create iterators
for any iterable type. Some common iterables are:
    lists
    tuples
    strings
    ranges
    files

"""

#This is how to loop over a range of numbers. An iterator is created to represent
#each value in the range.
x = 0
for i in range(0,10):
    x += i


#In this case, 'e' will represent every element in the list as it loops over it.
#This is much more convenient than having to create a range and then index this
#list
example_list = [1,2,3,4,5]
for e in example_list:
    x += e

#Iterating over a string
for char in "String":
    x = char


#example while loop. Iterators are not used as much with this type of loop
x = 10
while x > 0:
    x -= 1

#Going back a step. Iterating can be combined with if statements to make your
#life easier

if 'g' in "string":
    result = True

#easier than

for char in "string":
    if char == 'g':
        result = True 

"""
Python functions. 

Python functions are declared with the 'def' keyword and dont require a type.
They follow the same indentation rules. 

Functions allow for both single line and multiline returns. Empty returns are 
also allowed and are the same as returning None.

Python files are parsed from top to bottom so you need to declare functions in
the order they are used. Python code is executed as it is read which means that
code can execute between declaration of functions. This is all done at run time.

Contrast this to C where all functions and declarations are known at compile time
and the beginning of run time.

Because variable types are not bound until they are used, Python will not check
that your function arguments are correct until they are used. Be aware of the 
types you use or explicitly check if you are in doubt.

"""

#simple nop function
def nop():
    pass

#this statement will be executed before function_1 is declared
True == True

#function_1 will require nop to be declared first
def function_1():
    nop()
    return #unneeded, but empty return acts like void


#This time we have arguments
def function_2(a,b):
    return a + b

#multiline return
def function_3(a,b,c):
    x = a - b
    y = b - c
    return x,y

#checking against arg types
def function_4(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        return "incorrect type!"
    nop()
    return

"""
Python imports

Python scripts can be imported into other scripts as modules. You can import
your own scripts from the current directory, or PYTHONPATH. The PYTHONPATH
environment variable can be set and Python will search for scripts there. 
There is also a system wide location that contains default modules. It is possible
to install packages along side the system wide defaults. 

For now, lets just worry about system wide modules and scripts within the current
directory. Imports can happen at any time, but typically happen at the top of the 
file. I will import here for the examples though.

Imported modules can be imported as a different name, and it is also possible to
only import certain items from a module. When individual items are imported from
a module, they don't need to have their scope resolved. Module members are accessed
with the dot operator to resolve scope. All members can be imported with a *.

Take care that if you import using the wildcard * that multiple modules don't
share the same names. You will invoke some undefined behaviour when it comes to
resolving names.

"""
#typical import
import math

a = math.sqrt(2)

from math import exp

b = exp(1)

#importing as a more convenient name
import multiprocessing as mp
pool = mp.Pool()

#a script in the current dir
import helloworld

#wildcard import to grab everything. Not recommended.
from sys import *





