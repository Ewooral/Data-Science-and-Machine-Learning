# Descending into ML: Linear Regression

    It has long been known that crickets (an insect species) chirp more frequently on hotter days than on cooler days. For decades, professional and amateur scientists have cataloged data on chirps-per-minute and temperature. As a birthday gift, your Aunt Ruth gives you her cricket database and asks you to learn a model to predict this relationship. Using this data, you want to explore this relationship.

First, examine your data by plotting it:
Raw data of chirps/minute (x-axis) vs. temperature (y-axis).

## Figure 1. Chirps per Minute vs. Temperature in Celsius.

As expected, the plot shows the temperature rising with the number of chirps. Is this relationship between chirps and temperature linear? Yes, you could draw a single straight line like the following to approximate this relationship:
Best line establishing relationship of chirps/minute (x-axis) vs. temperature (y-axis).

## Figure 2. A linear relationship.

True, the line doesn't pass through every dot, but the line does clearly show the relationship between chirps and temperature. Using the equation for a line, you could write down this relationship as follows:
    
 *   y = mx + b

### where:

* **y** is the temperature in Celsius—the value we're trying to predict.
* **m** is the slope of the line.
* **x** is the number of chirps per minute—the value of our input feature.
* **b** is the y-intercept.

By convention in machine learning, you'll write the equation for a model slightly differently:
*  y^1 = b + w1.x1

where:

* **y^1** is the predicted label (a desired output).
* **b** is the bias (the y-intercept), sometimes referred to as w0
.
* **w1** is the weight of feature 1. Weight is the same concept as the "slope" *m* in the traditional equation of a line.

* **x1**  is a feature (a known input).

To infer (predict) the temperature *y^1*
for a new chirps-per-minute value *w1*, just substitute the *w1* value into this model.

Although this model uses only one feature, a more sophisticated model might rely on multiple features, each having a separate weight (*w1*, *w2* etc.). For example, a model that relies on three features might look as follows:
* y^1 = b + w1.x1 + w2.x2 + w3.x3
 
## Key Terms

bias	
inference
linear regression
weight 