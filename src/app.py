from flask import Flask, jsonify, request
import json
app = Flask(__name__)
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
# @app.route('/todos', methods=['GET'])
# def hello_world():
#     return jsonify(todos)
@app.route('/todos', methods=['GET','POST'])
def add_new_todo():
    # request_body = request.data
    # print("Incoming request with the following body", request_body)
    # return 'Response for the POST todo'
    if request.method == "POST":
        # print("POSTING")
        request_body = request.data
        # print(f"this is REQUEST BODY {request_body}")
        decoded_object = json.loads(request_body)
        # print(f"this is DECODED OBJECT {decoded_object}")
        todos.append(decoded_object)
        json_text = jsonify(todos)
        return json_text 
    elif request.method == "GET":
        return jsonify(todos)
    #print("Incoming request with the following body", request_body)
    #return 'Response for the POST todo'
    
@app.route('/todos/<int:position>', methods=["DELETE"])
def delete_todo(position):
    if request.method == "DELETE":
        todos.pop(position -1)
        print("This is the position to delete: " + str(position))
        return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)