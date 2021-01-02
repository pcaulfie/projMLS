# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np
from powerapp import testSpeed

# # Create a new web app.
# app = fl.Flask(__name__)

# # Add root route.
# @app.route("/")
# def home():
#   return app.send_static_file('index.html')

# # Add uniform route.
# @app.route('/api/uniform')
# def uniform():
#   return {"value": np.random.uniform()}

# Add normal route.
#@app.route('/api/normal')
def normal():
  ans = {"value": testSpeed(15.5)}
  print(ans)
  #return {"value": testSpeed(15.5)}

normal()
