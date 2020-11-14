from flask import Flask, jsonify, json, request

sockets = {
    'socket_1': False,
    'socket_2': False
}

app = Flask(__name__)

@app.route('/')
def hello():
	return "<h1>Pimote api</h1>"

@app.route('/sockets/', methods=['POST'])
def set_socket_values():
    if not request.json:
        return jsonify({'error':'error 1, send json'}), 400
    if 'socket_1' and 'socket_2' in request.json:
        if type(request.json['socket_1']) == bool and type(request.json['socket_2']) == bool:
            sockets['socket_1'] = request.json['socket_1']
            sockets['socket_2'] = request.json['socket_2']
            return jsonify({'message': 'sockets set'}), 201
        else:
            return jsonify({'error':'set booleans'}), 400
    else:
        return jsonify({'error':'set sockets'}), 400

@app.route('/sockets/', methods=['GET'])
def get_socket_values():
    return jsonify(sockets)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)