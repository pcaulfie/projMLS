# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np
import pandas as pd
from powerapp import testSpeed

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Add uniform route.
@app.route('/api/uniform')
def uniform():
  return {"value": np.random.uniform()}

# Add normal route.
@app.route('/api/normal')
def normal(params):
  #params = {'windspeed':15.75}
  x = params.get("windspeed")
  #print(x)
  arr = testSpeed(x)
  # ts = arr.astype('f')
  # ans = {"value": ts}
  # print(ans)
  # return {"value": testSpeed(15.5)}
  # print(str(ans))
  df = pd.DataFrame(arr)
  ts = df.iloc[0][0] # Access the first (only) row as a Series using iloc, and then the value using the column name
  return {"value": ts}
  #print(ts)
 
# @app.route('/api/normal', methods=['PUT'])
# def update():
#     rates = {
#         "windspeed": request.json["windspeed"]
#     }

#     return jsonify(ordersDao.create(order))
#normal()
