from flask import Flask, render_template, request, jsonify
from chat import get_response
import numpy as np
import pandas as pd
import pickle
import os
from wsgiref import simple_server

with open('model_pickle', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('temp.html')


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # we now see if the message is valid one or not
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


@app.route('/pred', methods=['POST'])
def pred():
    if (request.method == 'POST'):
        city = int(request.form['City'])
        location = int(request.form['Location'])
        cuisine = int(request.form['Cuisine'])
        no_of_reviews = int(request.form['No. of Reviews'])
        price = int(request.form['Price'])

        final_features = [np.array((city, location, cuisine, no_of_reviews, price))]
        # std_data = scaler.transform(final_features)

        prediction = model.predict(final_features)
        output = round(prediction[0], 2)

        if output <= 3.2:
            return render_template('temp.html', output=f"Predicted Rating is :  {str(output)}/5 \U0001F61E")
        elif 3.2 < output < 3.6:
            return render_template('temp.html', output=f"Predicted Rating is :  {str(output)}/5 \U0001F610")
        elif 3.6 < output <= 3.9:
            return render_template('temp.html', output=f"Predicted Rating is :  {str(output)}/5 \U0001F607")
        elif 3.9 < output <= 4.2:
            return render_template('temp.html', output=f"Predicted Rating is :  {str(output)}/5 \U0001F60B")
        elif 4.2 < output <= 4.8:
            return render_template('temp.html', output=f"Predicted Rating is :  {str(output)}/5 \U0001F63B")
        else:
            return render_template('temp.html')



if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    #clApp = ClientApp()
    host = '0.0.0.0'
    httpd = simple_server.make_server(host=host,port=port, app=app)
    httpd.serve_forever()

# Heroku Procfile rule
# https://medium.com/@gitaumoses4/deploying-a-flask-application-on-heroku-e509e5c76524
