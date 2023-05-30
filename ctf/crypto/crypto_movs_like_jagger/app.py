from flask import Flask, request, jsonify
from flask.templating import render_template
from navigation_system import calculatePointsInSpace, checkDestinationPoint
from utils import generateLocation

app = Flask(__name__)

E = None
Q, nQ = None, None
P, nP = None, None

FLAG = "HTB{--REDACTED--}"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            travel_result = checkDestinationPoint(request.form, P, nQ, E)
            location = generateLocation(travel_result)

            if travel_result:
                return render_template('travel.html', location=location, flag=FLAG)
            else:
                return render_template('travel.html', location=location)
        except ValueError as error:
            return render_template("index.html", error_message=str(error),
                                   departed_x=hex(Q.x()), departed_y=hex(Q.y()),
                                   present_x=hex(P.x()), present_y=hex(P.y()))
    return render_template('index.html', departed_x=hex(Q.x()),
                           departed_y=hex(Q.y()), present_x=hex(P.x()),
                           present_y=hex(P.y()))


@app.route('/api/coordinates', methods=['GET'])
def coordinates():
    points = {
        'departed_x': hex(Q.x()), 'departed_y': hex(Q.y()),
        'present_x': hex(P.x()), 'present_y': hex(P.y())
    }
    return points


@app.route('/api/get_flag', methods=['POST'])
def get_flag():
    try:
        travel_result = checkDestinationPoint(request.json, P, nQ, E)
        location = generateLocation(travel_result)

        if travel_result:
            return {"location": location, "flag": FLAG}
        else:
            return {"location": location}
    except ValueError as error:
        return {"error": error}


if __name__ == '__main__':
    Q, nQ, P, nP = calculatePointsInSpace()
    app.run(host='0.0.0.0', port=1337, debug=False, use_reloader=False)
