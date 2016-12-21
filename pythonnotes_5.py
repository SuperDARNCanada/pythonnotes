"""
SciPy
https://www.scipy.org/

SciPy is an open source collection of software tailored to science, math, and
engineering. SciPy resources aren't all bundled together but they belong to the
same ecosystem. SciPy packages are not installed by default. Each of these
packages explains how to install them on their websites.

Some important packages:

NumPy - N-dimensional fast arrays

SciPy library - various fundamentals for scientific computing

Matplotlib - extensive plotting features

IPython/Jupyter - enhanced interpreter for creating notebooks. Useful for combining
code and plotting.

Sympy - Symbolic math

pandas - data analysis and modeling(good for statistics)

There is quite a bit of detail to each of these packages, so feel free
to explore them to see how they might fit your needs. I will cover some
basics of NumPy, SciPy lib, and Matplotlib.
"""

"""
NumPy
http://www.numpy.org/

We've seen how powerful Python lists are, but the trade off for generality
is slower speed and larger memory footprint. In science however, we don't
need the flexibility of the list since our data is usually all of one
numeric type and we want fast calculations. Here is where NumPy steps in.

NumPy is meant to be collection of features that allows you to use fast,
large numeric arrays. This is a fundamental piece of SciPy as most of the
packages operate on NumPy arrays.

NumPy is quite extensive, but lets look at some basic features.
"""

import numpy as np

#creating a numpy array of all ones. Arg is the length.

ones = np.ones(10)

#the type of a numpy array is the ndarray. They are objects like
#everything else and they have many important properties.

type(ones) #type 'numpy.ndarray'

#How about if we want to know the data type of an ndarray? Well
#they contain a property called dtype which will tell you. When
#we create our arrays we can optionally specify a different dtype
#if we need a different type.

ones_type = ones.dtype #dtype('float64')
int_ones = np.ones(10,dtype=np.int32) #dtype('int32')

#It is very common to start with a Python list and need to convert
#to a ndarray. You may use functions that return lists or tuples
#but you want numpy data instead. When we create an array in this
#manner, numpy will use the dtype that is closest to the original
#Python type.

python_list = [0,1,2,3,4,5]
numpy_array = np.array(python_list) #dtype('int64')

#Again, we can create an array with a different dtype if we want.
numpy_array = np.array(python_list,dtype=np.float32)

#The ndarray is called so because they can be n-dimensional. The
#shape property tells us the dimension of an ndarray if we need it

nd_array = np.array([[0,1],[2,3]])
shape = nd_array.shape #(2, 2)


#Common array/matrix operations:

A = np.random.randn(64).reshape((8,8))
B = np.random.randn(64).reshape((8,8))

#transpose an array/matrix
A.T, B.T

#Add/subtract two arrays/matrices. Can add scalers too.
C = A + B - 1

#Multiply arrays/matrices via dot product. This is true matrix multiplication.
C = np.dot(A,B)

#Multiply arrays/matrices elementwise. Can multiply scalers too.
C = A * B * 1

#Invert an array/matrix.
C = np.linalg.inv(A)



"""
Matplotlib
http://matplotlib.org/

Matplotlib is an extensive set of plotting tools for Python. You could take an
entire course on all the features of matplotlib, but I will show the basics to
plotting that you can use to create basic plots to see your data. Matplotlib
expects data in the form of Numpy arrays. You should convert your data whenever
possible.

Matplotlib tries to follow a very similar model to Matlab plotting.
Matplotlib plots can be described as follows: the whole window and everything
contained is called the "figure". Any plots, textboxes, drawings, etc are all
contained within the this "figure" object. The "axes" child of a "figure" can
be thought of as the plot. The "axes" object contains a set of "axis" objects
(2 for 2D plots and 3 for 3D plots) as well as the data visualization. The
"axis" objects can be used to control things like data limits on each axis of
the plot.

More info here: http://matplotlib.org/faq/usage_faq.html#parts-of-a-figure


"""

#matplotlib uses different image creation backends depending on whether
#you are saving your figures to file or if you are interactively plotting.
#The default backend doesn't work on my computer so this how you change
#the image backend if you need to.
#More here: http://matplotlib.org/faq/usage_faq.html#what-is-a-backend
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

#Create some data
y_data1 = np.random.randn(25)
x_data1 = np.arange(len(y_data1))

y_data2 = np.random.randn(25)
x_data2 = np.arange(len(y_data2))

#plotting both sets in one window
fig1 = plt.figure() #creates a 'new window'

# add a new plot. The numbers specify grid parameters. In this
# case "1x1 grid, 1st subplot".
ax = fig1.add_subplot(111) #returns us a new "Axes" object to work with
ax.plot(x_data1,y_data1,'-o')
ax.plot(x_data2,y_data2,'-xr')
ax.set_title("Plot of two sets of random data")
ax.set_xlabel("Sample number")
ax.set_ylabel("Random sample value")


#or we could create two seperate windows
fig2 = plt.figure() #we can create more windows by creating a new figure
ax = fig2.add_subplot(111)
ax.plot(x_data1,y_data1,'-o')
ax.set_title("Plot of first random data")
ax.set_xlabel("Sample number")
ax.set_ylabel("Random sample value")

fig3 = plt.figure()
ax = fig3.add_subplot(111)
ax.plot(x_data2,y_data2,'-xr')
ax.set_title("Plot of second random data")
ax.set_xlabel("Sample number")
ax.set_ylabel("Random sample value")

# "Fast and easy" way to plot. Skip the "Axes" object and
# plot straight to the figure. This is useful for quick plots
# but will probably lead to issues if you are making complicated
# or publication quality plots.

fig4 = plt.figure()
plt.plot(x_data2,y_data2)

plt.show()