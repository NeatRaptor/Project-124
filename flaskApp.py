from flask import Flask,jsonify, request

app = Flask(__name__)

contacts = [
    {
        'Contact': u'9142536435',
        'Name': u'Rahul',
        'done': False,
        'id': 1
    },
    {
        'Contact': u'9253243546',
        'Name': u'Sasank',
        'done': False,
        'id': 2
    }
]


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data"
        },400)

    task = {
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    contacts.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)