from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response

@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') # get the parameter from url
  if pref:
    for student in data: # iterate dataset
      if student['pref'] == pref: # select only the students with a given meal preference
        result.append(student) # add match student to the result
    return jsonify(result) # return filtered set if parameter is supplied
  return jsonify(data) # return entire dataset if no parameter supplied

@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id: # filter out the students without the specified id
      return jsonify(student)
    return f"No student id number {id} exists"

@app.route('/stats')
def get_stats():
  stats= {}

  for student in data:
    if student['pref'] not in stats:
      stats[student['pref']] = 1
    else:
      stats[student['pref']] += 1

    if student['programme'] not in stats:
      stats[student['programme']] = 1
    else:
      stats[student['programme']] += 1

  return jsonify(stats)

@app.route('/add/<int:a>/<int:b>')
def add(a,b):
  return str(a+b)

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a,b):
  return str(a-b)

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a,b):
  return str(a*b)

@app.route('/divide/<int:a>/<int:b>')
def divide(a,b):
  return str(a/b)

app.run(host='0.0.0.0', port=8080, debug=True)
