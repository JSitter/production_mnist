from flask_restplus import Api, Resource, fields
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import os


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mnistdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mnistdb'
mongo = PyMongo(app)

api = Api(
  app, 
  version='1.0', 
  title="MNIST Dataset backend server", 
  description="This flask application serves a machine learning model trained on the MNIST dataset.")

ns = api.namespace(
  'api', 
  description="Api endpoints for predictions")

single_parser = api.parser()


@app.route('/')
def Index():
  '''Main Page'''
  # @api.doc(parser=single_parser, description='Get main page')
  something = mongo.db.something
  db_id = something.insert_one({"one": 'two'})
  ret = something.find_one({"_id":db_id})
  print(db_id)
  return "I'm feeling lucky"

# @ns.route('/predict', methods=['POST'])
# class Predictor():
#   @api.doc(parser=single_parser, description='Predict number')
#   def get(self):
#     return "This is working at least"
#   def post(self):
#     '''Post to retrive number from user'''
#     args = single_parser.parse_args()
#     print(args)
#     return True

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(host="0.0.0.0", debug=True)