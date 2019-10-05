# From https://www.youtube.com/watch?v=UbCWoMf80PY
# To extend this app to Docker, follow http://containertutorials.com/docker-compose/flask-simple-app.html
# Run this app as follows
# >_ export FLASK_APP = # $env:FLASK_APP = "app"
# >_ python app.py # >_ flask run --host 0.0.0.0 --port 4041

import numpy as np
from flask import Flask, request, jsonify, render_template, make_response
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    print(int_features) # print to terminal, for debugging
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    if request.is_json:
        data = request.get_json(force=True)
        prediction = model.predict([np.array(list(data.values()))])

        output = prediction[0]
        return make_response(jsonify(output), 200)
    else:
        return "Request was not JSON", 400


if __name__ == "__main__":
    app.run(debug=True)