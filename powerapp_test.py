# flask for web app.
import flask as fl
from flask import url_for, request, redirect, abort, jsonify, session, render_template
# numpy for numerical work.
import numpy as np
import pandas as pd
from powerapp import testSpeed

# Create a new web app.
app = fl.Flask(__name__, static_url_path='', static_folder='static')

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Add uniform route.
@app.route('/api/uniform')
def uniform():
  return {"value": np.random.uniform()}

# Add normal route.
@app.route('/api/power')
def getPower():
  #data = float(fl.request.args.get())
  data = float(fl.request.get_json())
  #x = request.args.get('windspeed')
  #params = {"windspeed": request.json["windspeed"]}
  # params = {'windspeed':15.75}
  # x = params.get("windspeed")
  # arr = testSpeed(x)
  # # # ts = arr.astype('f')
  # # # ans = {"value": ts}
  # # # print(ans)
  # # # return {"value": testSpeed(15.5)}
  # # # print(str(ans))
  # df = pd.DataFrame(arr)
  # ts = df.iloc[0][0] # Access the first (only) row as a Series using iloc, and then the value using the column name
  # return {"value": ts}
  #return jsonify(ts)
  #return jsonify(getPower())
  return jsonify(data)


# @app.route('/api/normal', methods=['GET','PUT']) # THIS WORKS
# def getPower2():
#   params = {'windspeed':15.75}
#   x = params.get("windspeed")
#   arr = testSpeed(x)
#   df = pd.DataFrame(arr)
#   ts = df.iloc[0][0] # Access the first (only) row as a Series using iloc, and then the value using the column name
#   return {"value": ts}
  
 
@app.route('/api/normal')
def normal():
  
  # loc = float(fl.request.args.get("loc", "0.0"))
  loc = float(fl.request.args.get("loc", "0.0"))
  #return fl.jsonify(np.random.normal(loc, scale, size).tolist())
  # return {"value": testSpeed(15.5)}
  # params = {'windspeed':15.75}
  # x = params.get("windspeed")
  arr = testSpeed(loc)
  df = pd.DataFrame(arr)
  ts = df.iloc[0][0] # Access the first (only) row as a Series using iloc, and then the value using the column name
  return {"value": ts}
  #return fl.jsonify(np.random.normal(loc, scale, size).tolist())
  #return {"value": loc}