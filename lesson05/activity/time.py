import os, time
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_coordinates():
	return str(time.time())

if __name__ == '__main__':
	port = int(os.environ.get('port', 6738))
	app.run(host='0.0.0.0', port=port)