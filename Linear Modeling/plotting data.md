# Plotting the Data

Everything in python is an object, even modules. 
Your goal in this exercise is to review the use of the 
object-oriented interfaces to the python library matplotlib in order to 
visualize measured data in a more flexible and extendable work flow.
The general plotting work flow looks like this:

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

# Hint

    Create figure and axis objects using plt.subplots().
    Call the plot() method on the axis object.
    Pass in the data variables and any key word arguments needed.
    To display the figure, use plt.show().


# Plotting the Model on the Data

Continuing with the same measured data from the previous exercise, your goal is to use a predefined model() and measured data times and measured_distances to compute modeled distances, and then plot both measured and modeled data on the same axis.

context figure
Instructions
70 XP
Instructions
70 XP

    Use model_distances = model(times, measured_distances) to compute the modeled values.
    Use plt.subplots() to create figure and axis objects.
    Use axis.plot() to plot times vs measured_distances with options linestyle=" ", marker="o", color="black".
    Use axis.plot() to also plot times vs model_distances with options linestyle="-", color="red".

Hint

The general form of the modeling and plotting work-flow will look like the following:

x2 = x1
y2 = model(x1, y1)
fig, axis = plt.subplots()
axis.plot(x1, y1, color="black")
axis.plot(x2, y2, color="red")
plt.show()
