"""
Object oriented programming

OOP is a language model that lets you express your data as a set of objects instead
of a group of inputs and procedures. It is easier for people think in terms of
things that are tangible and make physical sense. OOP allows you to construct
your programs as a model of what we experience in the real world. Python was
fully designed and based around this principle.

The first step in OOP is identify how to model your data and concepts as objects
and how your objects relate to each other. In programming we define 'classes'
which hold the properties and methods of objects, and when these 'classes' are
instantiated at runtime, they are known as objects.

Classes are a useful construct for other reasons other than data modelling.
Because classes contain only the properties and methods associated with them,
the programmer doesnt have to be worried about mixing or accessing the wrong
data. This concept is known as encapsulation. A class also promotes reusuability.
Our models are often useful in more than one program, so we can easily add our
classes to different programs to use them. It's also often possible to create
subclasses which create more special cases from a general case. This is known
as object inheritance.

In python, everything is an object. This includes functions, and even basic types!
Python also has constructs for creating your own classes. Our classes will have
some special terms, but the most important and basic is the __init__ function.
The __init__ function is known as constructor. A constructor is a function that is
run when the object is created. This is great for defining any set up or overhead
that the object has and saves you from having to call a bunch of code everytime
an object is created. The second most import term is the 'self' term. 'Self'
allows for an object to directly reference its own properties and functions.
It means that even if you instantiate multiple of the same object at runtime,
each object will only operate on itself. You don't have to worry about about
objects mangling themselves this way.

"""

#Creating a new class to model a vehicle. The parameter to a class is
#not actually an argument in the classic sense, but is actually the object
#we are inheriting from. In this case we are inheriting from Python's
#most basic construct, object.
class Vehicle(object):
    """docstring for Vehicle class"""

    #The constructor can take arguments like any other function.
    #We add self as an argument so that Python knows to pass a reference
    #from an object instance to this function.
    def __init__(self, make, model, color):
        #super refers to the class being inherited. We are simply
        #calling the constructor of the base class.
        super(ClassName, self).__init__()

        #Lets create some properties of this function. Using the dot operator
        #on self creates new properties for this class and we can assign
        #anything we like to them. Any variables not created using this
        #method will be only local to this function.
        self.make = make
        self.model = model
        self.color = color

    #here is a method for this class. We set the color in the constructor,
    #but now we can change the color at a later time!
    def change_color(self,color):
        self.color = color


new_vehicle = Vehicle("Ford","Fiesta","green")

#It's completely possible to access object properties directly,
#although its seen as a bad programming practice. It's better
#to create accessor or mutator functions within your class to
#expose properties, such as our change_color function.
vehicle_make = new_vehicle.make

new_vehicle.change_color("blue")


#This time we can inherit from a class we create if we want.
class BigTruck(Vehicle):
    """docstring for BigTruck class"""

    def __init__(self, make, model, color,has_4x4):
        #super refers to the class being inherited. We are simply
        #calling the constructor of the base class.
        super(ClassName, self).__init__(make, model, color)

        #We can reuse the properties of the general case, while adding
        #or changing stuff for a specific case!
        self.has_4x4 = has_4x4

new_truck = BigTruck("Ford","F350","white",True)




