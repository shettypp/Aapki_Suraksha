from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

states_names = [
    'Andhra Pradesh',
    'Arunachal Pradesh',
    'Assam',
    'Bihar',
    'Chhattisgarh',
    'Goa',
    'Gujarat',
    'Haryana',
    'Himachal Pradesh',
    'Jharkhand',
    'Karnataka',
    'Kerala',
    'Madhya Pradesh',
    'Maharashtra',
    'Manipur',
    'Meghalaya',
    'Mizoram',
    'Nagaland',
    'Odisha',
    'Punjab',
    'Rajasthan',
    'Sikkim',
    'Tamil Nadu',
    'Telangana',
    'Tripura',
    'Uttar Pradesh',
    'Uttarakhand',
    'West Bengal'
]


def sql(state_name):
    con = sqlite3.connect("emergency_numbers.db")
    cur = con.cursor()
    cur.execute("select * from emergencyNumbers where state=(?)", (state_name,))
    rows = cur.fetchall()
    return rows


@app.route('/')
def index():
    return render_template('sos.html', info=states_names, state_numbers=[])


@app.route('/emergency', methods=['GET'])
def get_numbers():
    state = request.args.get('state')
    state_numbers = sql(state)
    return render_template('sos.html', info=states_names, state_numbers=state_numbers)

@app.route('/stategov')
def stategov():
    return render_template("stategov.html")

@app.route('/indiangov')
def indiangov():
    return render_template("indiangov.html")

if __name__ == '__main__':
    app.run(debug=True)
