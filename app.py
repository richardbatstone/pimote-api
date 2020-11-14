from flask import Flask, jsonify, json, request

sockets = {
    'socket_1': True,
    'socket_2': False
}

app = Flask(__name__)

@app.route('/')
def hello():
	return "<h1>Hello, World!</h1>"

@app.route('/sockets/', methods=['POST'])
def set_socket_values():
    if not request.json or not 'socket_1' in request.json:
        return jsonify({'error':'error 1 set a socket'}), 400
    if type(request.json['socket_1']) == bool:
        sockets['socket_1'] = request.json['socket_1']
        return jsonify({'message': 'set socket'}), 201
    else:
        return jsonify({'error':'error 2 set a socket'}), 400

@app.route('/sockets/', methods=['GET'])
def get_socket_values():
    return jsonify(sockets)

if __name__ == '__main__':
	app.run(debug=True)