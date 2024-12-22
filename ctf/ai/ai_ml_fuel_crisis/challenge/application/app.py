import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
from flask import Flask, request
from flask.templating import render_template
from utils import Station, Spaceship, DockingException
from flag import flag
import tensorflow as tf
import random
import numpy as np

app = Flask(__name__)
first_model = None
second_model = None
x,y = None, None
b1_4s3d_station = None

UPLOAD_FOLDER = './application/models'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'h5'}

def generateRandomIdImage(id):
    id_list = [int(x) for x in str(id)]
    id_image = []
    for num in id_list:
        while True:
            index = random.randint(0,len(y))
            if y[index] == num:
                image = x[index].reshape(1,28,28,1)
                pred = first_model.predict(image)
                if np.argmax(pred) == num:
                    id_image.append(x[index])
                    break
    return id_image

def generateSpaceships(infoList):
    spaceships = []
    for info in infoList:
        id_image = generateRandomIdImage(info[0])
        spaceship = Spaceship(info[0],info[1], id_image)
        spaceships.append(spaceship)
    return spaceships

def allowed_file(filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    

@app.route('/', methods=['GET', 'POST'])
def index():

    ids = []
    for spaceship in b1_4s3d_station.spaceships:
        ids.append(spaceship.idToBase64())

    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', ids = ids, response = "File upload failed.")
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', ids = ids, response = "File upload failed.")
        if file and allowed_file(file.filename):
            try:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], "uploaded.h5"))
                b1_4s3d_station.second_gate = tf.keras.models.load_model("./application/models/uploaded.h5")
            except:
                return render_template('index.html', ids = ids, response = "File upload failed.")
        return render_template('index.html', ids = ids, response = "File upload was successfull.")
    else:
        return render_template('index.html', ids = ids)

@app.route('/dock', methods=['POST'])
def dock():
    try:
        for spaceship in b1_4s3d_station.spaceships:
            id, id_confidence = b1_4s3d_station.passFirstGate(spaceship.id_image)
            if spaceship.name == "Phalcon":
                b1_4s3d_station.passSecondGate(id, spaceship.id_image, id_confidence, validation_check=False)
            else:
                b1_4s3d_station.passSecondGate(id, spaceship.id_image, id_confidence)
    except DockingException as de:
        return render_template('dock.html', response = spaceship.name+str(de))
    except Exception as e:
        return render_template('dock.html', response = 'Unexpected error while docking.')
    return render_template('dock.html', response = flag)


if __name__ == '__main__':
    (x, y), _ = tf.keras.datasets.mnist.load_data()
    print("loaded dataset...")
    first_model = tf.keras.models.load_model('./application/models/model.h5')
    second_model = tf.keras.models.load_model('./application/models/model.h5')
    print("loaded models...")
    spaceships = generateSpaceships([[13376, "IFG-Wing"], [66594,"Nebulon-B"], 
                                    [10054,"Star Destroyer"], [88519,"IFG-Gunship"], 
                                    [32166,"Phalcon"]])
    print("generated spaceships...")
    b1_4s3d_station = Station(spaceships, first_model, second_model)
    print("running app...")
    app.run(host='0.0.0.0', port=1337, debug=False)
