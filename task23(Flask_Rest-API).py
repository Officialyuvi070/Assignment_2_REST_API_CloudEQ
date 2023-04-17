from flask import Flask, jsonify, request

comp = Flask(__name__)

info = [
    {
        'employee_id': 1,
        'name': 'Rohit',
        'Company_name':'CloudEQ',
        'Position': 'Software Trainee'     
    },
    {
      'employee_id': 2,
      'name': 'Mohit',
      'Company_name':'CloudEQ',
      'Position': 'DevOps Engineer' 
    }
]

@comp.route('/')
def welcome():
    return "Welcome To CloudEQ"

@comp.route('/add-data', methods=['POST'])
def add_info():
    if not request.json:
        return jsonify({
            "status":"ERROR",
            "message":"Please Provide the data!"
        },400)
    
    info_1 = {
        'employee_id': info[-1]['employee_id'] +1,
        'name': request.json['name'],
        'Company_name': request.json.get('Company_name',""),
        'Position': request.json['Position']
    }
    info.append(info_1)
    return jsonify({
        "status":"SUCCESS",
        "message": "info_1 added successfully"
    })

@comp.route("/get-data")
def get_info():
    return jsonify({
        "data" : info
    })    

if (__name__ == "__main__"):
    comp.run(debug=True)