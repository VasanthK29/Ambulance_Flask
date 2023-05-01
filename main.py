# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, disconnect
from threading import Lock
from databaseService import *

async_mode = None
app = Flask(__name__, static_url_path='/assets')
app.config['SECRET_KEY'] = 'secret!'
socket_ = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def index():
	return render_template('index.html', async_mode=socket_.async_mode);

@socket_.on('loc_changed', namespace='/geoLocation')
def geoLocation_changed(json):
	print("received json: "+str(json))

# def hello_world():
# 	dbService = databaseService()
# 	junction = dbService.getTableJunction();
# 	for x in junction:
# 		print(x.latitude)


# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	socket_.run(app, debug=True)
