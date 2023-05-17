# from flask import Flask, render_template, copy_current_request_context , Response
# from flask_socketio import SocketIO, emit, disconnect
# from threading import Lock
# from databaseService import *
# from haversine import haversine, Unit
# import cv2
# import os

# async_mode = None
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socket_ = SocketIO(app, async_mode=async_mode)
# thread = None
# thread_lock = Lock()
# camera = cv2.VideoCapture(0)

# @app.route('/')

# def index():
#     return render_template('index.html', async_mode=socket_.async_mode)

# @socket_.event
# def start(message):
#     print('client '+ message['data'])

# def gen_frames():  
#     while True:
#         success, frame = camera.read()  # read the camera frame
#         if not success:
#             break
#         else:
#             detector = cv2.CascadeClassifier('C:\\Users\\vasan\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\cascade.xml')
#             faces=detector.detectMultiScale(frame,1.1,7)
#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#              #Draw the rectangle around each face
#             for (x, y, w, h) in faces:
#                 cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/video_feed')
# def video_feed():
#     return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/admin')
# def admin():
#     return render_template("admin.html")

# @socket_.event
# def loc_changed(json):
#     coordinates = json['crd']
#     print("received json: "+str(coordinates['latitude'])+" "+str(coordinates['longitude']))
#     user_lat = coordinates['latitude']
#     user_lon = coordinates['longitude']
#     rajaji_lat = 9.927876668067677
#     rajaji_lon = 78.13048097430466
#     dbService = databaseService()
#     junction = dbService.getTableJunction();
#     count = 0
#     array =[9.931204, 78.094597]
#     #pt1 = (user_lat, user_lon)
#     pt1 = (array[0],array[1])
#     pt2 = (rajaji_lat,rajaji_lon)	
#     dt = haversine(pt1, pt2, unit=Unit.KILOMETERS)
#     dtm = dt * 1000
#     if(dtm<100):
#         print("near rajaji hospital")
#         disconnect()
#     else:
#         for x in junction:
#             lat =float(x.latitude)
#             lon = float(x.longitude)
#             point1 = (lat, lon)
#             point2 = (array[0], array[1])
#             distance = haversine(point1, point2, unit=Unit.KILOMETERS)
#             distance_in_m = distance * 1000
#             if(int(distance_in_m)<200):
#                 print("near  " + x.junctionName + "  switching signal for 30 seconds...")
#                 count += 1
#                 break                                                
#         if(count==0):
#             print("yet to arrive near signal")
#         else:
#             gen_frames()

#     #emit('output', {data: result})


# @socket_.event
# def disconnect_request():
#     @copy_current_request_context
#     def can_disconnect():
#         disconnect()
#     emit('stop', {data: 'client is disconneted'}, callback=can_disconnect)


# if __name__ == '__main__':
    
#     socket_.run(app, debug=True, allow_unsafe_werkzeug=True)


from flask import Flask, request
from math import sin,cos,sqrt,atan2,radians
from databaseService import *
from haversine import haversine, Unit
import cv2
import os

app = Flask(__name__)

def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            detector = cv2.CascadeClassifier('C:\\Users\\vasan\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\cascade.xml')
            faces=detector.detectMultiScale(frame,1.1,7)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
             #Draw the rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/admin')
def admin():
    return render_template("admin.html")


@app.route('/location', methods=['POST','GET'])
def location():
    data = request.data.decode('utf-8')
    user_lat, user_lon = data.split(',')
    print(f'Latitude: {user_lat}, Longitude: {user_lon}')

    rajaji_lat = 9.927876668067677
    rajaji_lon = 78.13048097430466
    dbService = databaseService()
    junction = dbService.getTableJunction();
    count = 0
    array =[9.931204, 78.094597]
    #pt1 = (user_lat, user_lon)
    pt1 = (array[0],array[1])
    pt2 = (rajaji_lat,rajaji_lon)	
    dt = haversine(pt1, pt2, unit=Unit.KILOMETERS)
    dtm = dt * 1000
    if(dtm<100):
        print("near rajaji hospital")
        disconnect()
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
                count += 1
                break                                                
        if(count==0):
            print("yet to arrive near signal")
        else:
            gen_frames()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
