"""
Python imports revisted

It is important to note that when a Python script is executed or imported
all code is run. Sometimes we want this if we want to run some overhead
or global data at import. But sometimes we would like portions of our script
not to run if its imported and instead run only that code if that script
is run as a stand alone.

For this scenario we use a line in the script as follows:
    if __name__ == "__main__":
        code_goes_here()

Python is smart enough to know if its the main script or if it's been imported.
This check can be used to build scripts that have different behaviour if used
as a standalone. You could for example build a module as part of analysis code
and your testing could go in a if __name__ == "__main__", but that testing
code will not run if imported into your main project.

You may also have a folder of scripts you want to treat as a package. By placing
a file called __init__.py into a folder, Python will try import all .py files
for you. Your __init__.py file can have code in it when building fancy packages,
but can also be blank. This file is just to tell python to treat the folder as 
a collection of scripts. This very useful for grouping your common scripts together.

"""

def main():
    #main code goes here
    pass

#A typical way to simulate a main function.
if __name__ == "__main__":
    main()

#from the examples folder, import the file blank.py
#you can import selectively, or everything.
import examples.blank

"""
Python lists revisted

We've seen before that Python lists can be used to build containers
that can hold a collection of any type.

Lists are indexed like arrays using the square bracket notation. They
are sliced using a colon to delimit the start and stop indices of a slice.
Lists can be indexed using negative numbers as well. Negative numbers move
backwards in the list, where as positive numbers move forwards though the list.

Lists have several important methods associated with them. The most important
ones are append, remove and extend.

The len() function returns the number of elements in a list.

Lists have + and * operators. + will concatenate lists, but will only work
with lists. No other sequences. * is a scaler operation which will repeat
a number of values in the list.

A powerful feature of Python is the list comprehension. This allows us to
create lists in a very natural way. They are very useful to generate a new list
from an existing sequence. The syntax for list comprehension is somewhat 
confusing at first but becomes the most fast and powerful way to generate data
lists once you master them. List comprehensions are generally much faster than 
for loops for data generation. See the examples below.

"""

list1 = ['a', 's', 'd', 'f', 'g']
list_slice_1 = list1[0] #list_slice_1 = 'a'
list_slice_2 = list1[1:3] #list_slice_2 = ['s','d']
list_slice_3 = list1[-1] #list_slice_3 = 'g'
list_slice_4 = list1[2:] # slices from index 2 to end

list2 = [] #making empty list
for i in range(8):
    list2.append(i) #appending new values on the fly

list2.remove(2) #finds 2 in the list and removes it
del(list2[3]) #deletes an item at a specific index

list1.extend(list2) #concatenates list2 to list1. Extend will
#concatenate any sequence, such as tuples for example.

list_len = len(list1) #returns number of elements.

list3 = list1 + list2 # + operator concatenates lists

list4 = ['hello'] * 3 # list5 = ['hello','hello','hello']

#list comprehension examples

#for each letter in list1, convert to uppercase and make a new list
#of uppercase values
list1 = ['a', 's', 'd', 'f', 'g']
upper_list = [letter.upper() for letter in list1]

#this syntax is shorthand for the following loop, but will also run much faster
#as Python list comprehensions are better optimized
upper_list = []
for letter in list1:
    upper_list.append(letter)

#for each value in celsius, convert to fahrenheit and build a new
#list of fahrenheit data points.
celsius = [39.2, 36.5, 37.3, 37.8]
fahrenheit = [ ((float(9)/5)*x + 32) for x in celsius]

real = [1,2,3,4,5]
imag = [-1,-2,-3,-4,-5]

#here we perform a list comprehension over two lists to convert lists representing
#real and imaginary numbers into a complex value. The zip function allows you to 
#iterate over multiple sequences by returning a tuple of items at matching indices.
cmplx = [ complex(r,i) for r,i in zip(real,imag)]

#There is powerful tools available for list comprehensions. As you become more
#familiar with them, try to build clever code for compact code. Complicated 
#list comphrensions are fine because your data generation is compact and its
#obvious what expressions are involved, but try use intelligent naming.

alpha = [1,2,3,7,8,9]
beta = [1,3,5,7,9]
x = [1,2,3,4,5,6,7,8,9]

#Much more complicated expression, but remains concise and readable
y = [x for x in x if (x not in alpha and x not in beta)] #y = [4,6]



"""
Python object identity

It is important to note how Python objects work. In Python, everything is an 
object. Numbers, strings, data structures, and even functions are objects.
When we create a new variable that variable is actually a reference to that
object. This is why we must be careful when testing equivalence. We need to
know whether we are testing references or values.

The biggest confusion with comparison often comes with strings and number
literals. When strings literals, aka. words you type that are surrounded by
quotes, or number literals are entered into the interpretter or scripts, 
Python has a speed benefit by creating only one instance of that literal
and making all duplicate objects point to these instances. However, if values
are generated on the fly at runtime, Python won't necessarily know that your
literals are the same thing. The examples demonstrate this.

Another thing to note is that Python always passes arguments to functions
by value. This means if you update the reference to what an argument points to
then it will only be local to the scope of that function.

"""


#Since these are literals defined before runtime they can point to the same spot
string1 = "This is a string"
string2 = "This is a string"

print("String1 String2 value comparison")
print(string1 == string2) #True
print("String String2 reference comparison")
print(string1 is string2) #True

string3 = ' '.join(['This','is','a','string'])

print("String1 String3 value comparison")
print(string1 == string3)
print("String1 String3 reference comparison")
print(string1 is string3)
