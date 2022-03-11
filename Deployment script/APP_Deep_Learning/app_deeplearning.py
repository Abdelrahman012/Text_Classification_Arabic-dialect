from flask import Flask, render_template, request
from preprocessing import processing_Data
import pickle
from model_loading import Model
import numpy as np
DL_Model=Model().get_model()
with open("E:\\AIM_APP\\Any additional files\\Models\\encoder.pickle", 'rb') as handle:
    encoder = pickle.load(handle)



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/prediction',methods=['POST'])
def prediction():
    if request.method == 'POST':

        text = request.form['rawtext']
        print(text)
        features=processing_Data(text)
        print(features[0])
        cc=DL_Model.predict(features)
        print(cc)
    xc = encoder.inverse_transform(np.argmax(cc,axis=1).reshape(-1,1))

    return render_template('home.html',recived=xc)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)



