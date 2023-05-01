# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, copy_current_request_context
from flask_socketio import SocketIO, emit, disconnect
from threading import Lock
from databaseService import *

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket_ = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def index():
	return render_template('index.html', async_mode=socket_.async_mode);

@socket_.event
def start(message):
    print('client '+ message['data'])

@socket_.event
def loc_changed(json):
	coordinates = json['crd']
	print("received json: "+str(coordinates['latitude'])+" "+str(coordinates['longitude']))

@socket_.event
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()
    emit('stop', {data: 'client is disconneted'}, callback=can_disconnect)

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
