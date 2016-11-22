"""
Python command line arguments

There are several options for parsing command line arguments in Python. The
easiest way is to use the sys module which gives you direct access to argv,
similar to C. The difference between C and Python is that the program name
is not stored in the first index of argv.

There are other modules such as argparse and getopt which allow for more
robust command line argument parsing, and make it easier to do key:value
style argument parsing, ex. "--freq 12e6 --timescale 1e-3". These notes won't
cover these modules in detail as there are already good tutorials out there.
I would recommend using argparse or getopt if you plan to distribute your
code to anyone, or if you expect other people may use your code at any time.
It just makes for more clear arguments and these modules can also provide
help messages for users.

It is important to note that using the basic argv list provided by 
sys will throw errors if you forget to pass an argument, or if the 
argument is of the wrong type. argparse or getopt provide functionality
to type check inputs and handle incorrect arguments.

"""

import sys

#sys.argv is a list of command line arguments passed to the program
print(sys.argv)

#*try/except blocks covered later. They catch and handle errors.
try:
    freq = sys.argv[0]
    timescale = sys.argv[1]
except:
    pass


"""
Python file IO

The most basic file IO in Python is printing to stdout using the print command.
Printing works slightly different between Python 2 and Python 3. In Python 2,
print is a statement, and in Python 3 print is a function. The way I use print
to never have a problem is to just always use parenthesis when printing. Python
2 will treat this as printing a tuple, and Python 3 will perform it as a
function call. This is slightly annoying to have to consider, but the switch
to treating print as a function is Python 3 is somewhat beneficial as now
it can be used in places where statements are not allowed, ex. list comphrensions.

User input is done using raw_input or input. raw_input returns the user input 
as a string whereas input actually assumes the input is a valid Python expression
and will evaluate it and return the result.

Files can be manipulated too. The most common operations are to open and close
files, and to read and write from them. One important Python statement is the with 
statement. There are many cases in Python where your operations require a set
up and tear down. For example, files need to be opened and then closed. Databases
require a connect and a disconnect. Going into Python in a deeper level, there
are certain constructs in place when developers create Python classes that
allow them to define these set up and tear down methods. The with command
will automatically run this overhead for you. This is useful for files, because
we dont have to worry about accidently forgetting to close them when we are
done using them. This is demonstrated in the examples.

I find that working with files is usually pretty custom because people usually
have different ways they want to work with their file contect. There is lots 
of additional information on working with files online.

"""

#print statement
print("This is the python print command!")

#receiving using input
input_str = raw_input("Enter an input string: ")
data = input("Enter your Python data: ")

#open a file in read mode. A list of other modes can be found online
f = open("testfile.txt",'r')

#read file contents into a variable
file_data = f.read()

#closing a file
f.close()

#open file in write mode. If the file doesnt exist, its created.
f = open("writefile.txt",'w')

#write out some data to the file
f.write("I'm writing out some text!")

#close the file after using
f.close()

#by using the with statement, the file is automatically closed when
#we leave the scope
with open("testfile.txt") as f:
    file_data = f.read()

#f is closed here







