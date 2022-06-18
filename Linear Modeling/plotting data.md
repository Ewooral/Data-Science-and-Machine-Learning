Plotting the Data

Everything in python is an object, even modules. Your goal in this exercise is to review the use of the object oriented interfaces to the python library matplotlib in order to visualize measured data in a more flexible and extendable work flow. The general plotting work flow looks like this:

import matplotlib.pyplot as plt 
fig, axis = plt.subplots()
axis.plot(x, y, color="green", linestyle="--", marker="s")
plt.show()

context figure
Instructions
100 XP

    Use plt.subplots() to create figure and axis objects.
    Data have been provided in two predefined numpy arrays, times and distances.
    Use axis.plot() to plot times on the horizontal and distances on the vertical.
    Use the input key word args linestyle=" ", marker="o", and color="red" when calling axis.plot().
