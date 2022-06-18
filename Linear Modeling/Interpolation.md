# Reasons for Modeling: Interpolation

One common use of modeling is interpolation to determine a value "inside" or "in between" the 
measured data points. In this exercise, you will make a prediction for the value of the 
dependent variable distances for a given independent variable times that falls "in between" two 
measurements from a road trip, where the distances are those traveled for the given elapse times.



    Inspect the predefined data arrays, times and distances, and the preloaded plot.
    Based on your rough inspection, estimate the distance_traveled away from the starting position as of elapse_time = 2.5 hours.
    Assign your answer to distance_traveled.

Hint

    Method 1: Visual Inspection: Look at the plot and make a guess. You will likely be right! :)
    Method 2: Quantitative: Compute the average_speed using the first and last points. Then compute the distance_traveled as the product average_speed * time_elapsed. 