# Efficient numerical arrays.
import numpy as np
# Data frames.
import pandas as pd
# Alternative statistics package.
import statsmodels.stats.weightstats as stat
# Mains statistics package.
import scipy.stats as ss
# Efficient numerical arrays.
import numpy as np
# Data frames.
import pandas as pd
# Alternative statistics package.
import statsmodels.stats.weightstats as stat
# Mains statistics package.
import scipy.stats as ss
# Plotting.
import matplotlib.pyplot as plt
# Fancier plotting.
import seaborn as sns

# Better sized plots.
plt.rcParams['figure.figsize'] = (12, 8)

# Nicer colours and styles for plots.
plt.style.use("fivethirtyeight")

# Load the powerproduction dataset from a csv file using read_csv function into dataframe called df
# adapted from Willems (2017) and McLoughlin (2019)
df = pd.read_csv("powerproduction.csv")

# Remove "Zero" Values
newdf = df[(df.power > 0)] 

# Display the dataframe
#print(newdf.describe())

'''Polynomial Regression'''
# Step 1: Import packages and classes - solution adapted from Stojiljkovic (2019).
# The class sklearn.linear_model.LinearRegression will be used to perform linear regression using the Ordinary Least Squares model
from sklearn.linear_model import LinearRegression
# import the class PolynomialFeatures from sklearn.preprocessing:
from sklearn.preprocessing import PolynomialFeatures

# Create array consisting of the two columns; x and y variables
predictors = newdf[['speed', 'power']]

#Step 2a: Provide data

XX = np.asarray(predictors['speed']) # https://docs.scipy.org/doc/numpy/reference/generated/numpy.asarray.html
# Convert 1 array XX into 2D array called X2 in the shape of a column vector by inserting an axis along second dimension
X2 = XX[:, np.newaxis] # https://medium.com/@ian.dzindo01/what-is-numpy-newaxis-and-when-to-use-it-8cb61c7ed6ae

#Step 2b: Transform input data
# degree is an integer 3 (2 by default) that represents the degree of the polynomial regression function.
x_4 = PolynomialFeatures(degree=10, include_bias=False).fit_transform(X2)
y = predictors['power']
model3 = LinearRegression(fit_intercept=False).fit(x_4, y)

# write a function that predicts a power output from an windspeed value entered by the user
def testSpeed(a):
    # print("\n\nWelcome")
    # print("-------------------------")
    # # get user to enter windspeed 
    # a = input("Enter Windspeed (in metres per second): ")
    # a = float(a)  # parse string into an integer, reference https://stackoverflow.com/a/19234631

    if a > 7.5 and a < 24.5: 
        Testspeed2 = np.array([a]) # https://docs.scipy.org/doc/numpy/user/basics.creation.html

        # Convert 1D array Xfit into 2D array in the shape of a column vector by inserting an axis along second dimension
        Testspeed2 = Testspeed2[:, np.newaxis] 
        # display the shape of an array Testbill
        Testspeed2.shape # adapted from https://stackoverflow.com/a/10200284
        s = PolynomialFeatures(degree=10, include_bias=False).fit_transform(Testspeed2)
        y_pred5 = model3.predict(s)
        return y_pred5
        # Predict powr output for wind speed of 15.5 meters/secons
        # To obtain the predicted response, use .predict():adapted from Stojiljkovic (2019).
        #print('Predicted output (kw) if windspeed is ', a, ' meters per second is:', y_pred5, 'kilowatts.')
        
    else:
        #rint('INVALID ENTRY: Enter a value between 7.5 and 24.5')
        return -1
#testSpeed(a)