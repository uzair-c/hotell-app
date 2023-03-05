from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'hotel_booking_app'
mysql = MySQL(app)

@app.route('/rooms', methods=['GET'])
def get_rooms():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM rooms")
    rows = cur.fetchall()
    return jsonify(rows)

@app.route('/rooms', methods=['POST'])
def add_room():
    room_nr = request.json['room_nr']
    price = request.json['price']
    floor = request.json['floor']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO rooms (room_nr, price, floor) VALUES (%s, %s, %s)", (room_nr, price, floor))
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
