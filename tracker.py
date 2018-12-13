import flask
from flask import request, jsonify, send_file

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/image/<string>', methods=['GET'])
def home(string):
	filename = 'ok.jpg'
	print('iamge is opened.')
	return send_file(filename, mimetype='image/gif')


app.run(host='0.0.0.0', port=80)