# Efficient numerical arrays.
import numpy as np
# Data frames.
import pandas as pd
# flask for web app.
import flask as fl
from flask import url_for, request, redirect, abort, jsonify, session, render_template

# Load the powerproduction dataset from a csv file using read_csv function into dataframe called df
# adapted from Willems (2017) and McLoughlin (2019)
df = pd.read_csv("powerproduction.csv")

# Remove "Zero" Values
newdf = df[(df.power > 0)] 

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
# degree is an integer 10 (2 by default) that represents the degree of the polynomial regression function.
x_4 = PolynomialFeatures(degree=10, include_bias=False).fit_transform(X2)
y = predictors['power']
model3 = LinearRegression(fit_intercept=False).fit(x_4, y)

# function to predicts a power output from an windspeed value entered by the user in webservice
def predict(a):
    
    if a > 7.5 and a < 24.5: 
        Testspeed2 = np.array([a]) # https://docs.scipy.org/doc/numpy/user/basics.creation.html

        # Convert 1D array Xfit into 2D array in the shape of a column vector by inserting an axis along second dimension
        Testspeed2 = Testspeed2[:, np.newaxis] 
        # display the shape of an array Testspeed2
        Testspeed2.shape # adapted from https://stackoverflow.com/a/10200284
        s = PolynomialFeatures(degree=10, include_bias=False).fit_transform(Testspeed2)
        y_pred5 = model3.predict(s)
        return y_pred5
                
    else:
        # INVALID ENTRY: will not return a prediction')
        return -1

# Create a new web app.
app = fl.Flask(__name__, static_url_path='', static_folder='static')

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')
 
'''this route is working'''
@app.route('/api/model')
def model():
  
  # windspeed value passed from web service, default 0 - adapted from https://github.com/ianmcloughlin/flask-distros/blob/master/distros.py
  wind = float(fl.request.args.get("wind", "0.0"))
  # pass wind value to predict() and output result to 'arr'
  arr = predict(wind)
  # convert arr to pandas dataframe
  df = pd.DataFrame(arr)
  prediction = df.iloc[0][0] # Access the first (only) row as a Series using iloc, and then the value using the column name - adapted from stackoverflow posts
  # return prediction to web service
  return {"value": prediction}
