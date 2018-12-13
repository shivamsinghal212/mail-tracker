import flask
from flask import request, jsonify, send_file

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/image', methods=['GET'])
def home():
	filename = 'ok.jpg'
	print('iamge is opened.')
	return send_file(filename, mimetype='image/gif')


app.run()