# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, copy_current_request_context
from flask_socketio import SocketIO, emit, disconnect
from math import sin,cos,sqrt,atan2,radians
from threading import Lock
from databaseService import *
from haversine import haversine, Unit

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
	user_lat = coordinates['latitude']
	user_lon = coordinates['longitude']
	rajaji_lat = 9.927876668067677
	rajaji_lon = 78.13048097430466
	dbService = databaseService()
	junction = dbService.getTableJunction();
	count = 0
	array = [9.928265, 78.130602]
	#pt1 = (user_lat, user_lon)
	pt1 = (array[0],array[1])
	pt2 = (rajaji_lat,rajaji_lon)	
	dt = haversine(pt1, pt2, unit=Unit.KILOMETERS)
	dtm = dt * 1000
	if(dtm<100):
		print("near rajaji hospital")
	else:
		for x in junction:
			lat =float(x.latitude)
			lon = float(x.longitude)
			point1 = (lat, lon)
			point2 = (array[0], array[1])
			distance = haversine(point1, point2, unit=Unit.KILOMETERS)
			distance_in_m = distance * 1000
			if(int(distance_in_m)<200):
				print("near  " + x.junctionName + "  switching signal for 30 seconds...")
				count = 1
		if(count==0):
			print("yet to arrive near signal")
		else:
			sleep(10)
	#emit('output', {data: result})


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
