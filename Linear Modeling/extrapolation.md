# Reasons for Modeling: Extrapolation

Another common use of modeling is extrapolation to estimate data values "outside" or "beyond" the range (min and max values of time) of the measured data.
In this exercise, we have measured distances for times 0 through 5 hours, but we are interested in estimating how far we'd go in 8 hours. Using the same data set from the previous exercise, we have prepared a linear model distance = model(time). Use that model() to make a prediction about the distance traveled for a time much larger than the other times in the measurements.

context figure
Instructions
100 XP

    Use distance = model(time) to extrapolate beyond the measured data to time=8 hours.
    Print the distance predicted and then check whether it is less than or equal to 400.
    If your car can travel, at most, 400 miles on a full tank, and it takes 8 hours to drive home, will you make it without refilling? You should have answer=True if you'll make it, or answer=False if you will run out of gas.

Hint

    Use the model() function to compute a distance for an input arg of time=8, for 8 hours.
    Assign answer=True if the resulting distance is less than or equal to 400. 



# Reasons for Modeling: Estimating Relationships

Another common application of modeling is to compare two data sets by building models 
for each, and then comparing the models. In this exercise, you are given data for a road trip two cars took together. The cars stopped for
gas every 50 miles, but each car did not need to fill up the same amount, because the cars 
do not have the same fuel efficiency (MPG). Complete the function efficiency_model(miles, gallons) 
to estimate efficiency as average miles traveled per gallons of fuel consumed. Use the provided 
dictionaries car1 and car2, which both have keys car['miles'] and car['gallons'].



    Complete the function definition for efficiency_model(miles, gallons).
    Use the function to compute the efficiency of the provided cars (dicts car1, car2).
    Store your answers as car1['mpg'] and car2['mpg'].
    Complete the following logic statement to print which car (if either) has the best efficiency.

Hint

    Inside efficiency_model(), use numpy to compute the mean of the ratio of miles over gallons.
    Use the efficiency_model() function to compute and assign car1['mpg'] and car2['mpg'].
    Use the comparison operators > and < to complete the logic statement in the final step.
