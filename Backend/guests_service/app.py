import requests
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

@app.route('/guests', methods=['GET'])
def get_guests():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM guests")
    rows = cur.fetchall()
    return jsonify(rows)

@app.route('/guests', methods=['POST'])
def add_guest():
    room_nr = request.json['room_nr']
    room = requests.get(f'http://localhost:5001/rooms?room_nr={room_nr}').json()
    if not room:
        return jsonify({'error': 'Room not found'})
    cur = mysql.connection.cursor()
    name = request.json['name']
    telefon = request.json['telefon']
    cur.execute("INSERT INTO guests (name, telefon, room_nr) VALUES (%s, %s, %s)", (name, telefon, room_nr))
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run(port=5002, debug=True)
