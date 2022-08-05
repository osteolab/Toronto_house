import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#procfile.txt 
#web: gunicorn app:app
#first file that we have to run first : flask server name
app = Flask(__name__)
#pkl_file = open('model.pkl','rb')
model = pickle.load(open('model.pkl', 'rb'))
#index_dict = pickle.load(pkl_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    if request.method=='POST':
        result = request.form

        new_vector = [0,0,0, 0,0,0 ,0,0,0, 0,0,0]
        new_vector[0] = int(result['bed'])
        new_vector[1] = int(result['bath'])
        new_vector[2] = float(result['Latitude'])
        new_vector[3] = float(result['Longitude'])

        if result['city'] == 'Brampton':
          new_vector[4] = 1
        if result['city'] == 'Markham':
          new_vector[5] = 1
        if result['city'] == 'Mississauga':
          new_vector[6] = 1
        if result['city'] == 'Toronto':
          new_vector[7] = 1
        if result['city'] == 'Vaughan':
          new_vector[8] = 1
        if result['type'] == 'CONDO':
          new_vector[9] = 1
        if result['type'] == 'SINGLE_FAMILY':
          new_vector[10] = 1
        if result['type'] == 'TOWNHOUSE':
          new_vector[11] = 1

    new = [new_vector]
    print(new)
    prediction = model.predict(new)
    print(prediction)
    return render_template('index.html', Predict_score ='Your house estimate price of ({}bed-{}bath-{}-{}) is  CA$ {}'.format(new_vector[0],new_vector[1],result['city'],result['type'],int(prediction)))


if __name__ == "__main__":
    app.run(debug=True)
