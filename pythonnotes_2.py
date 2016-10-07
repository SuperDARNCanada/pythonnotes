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
