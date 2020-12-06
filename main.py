from flask import Flask, request, render_template, redirect
import predict
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def my_form():
    if request.method == 'POST':
        ismale = request.form['ismale']
        gestation_weeks = request.form['gestation_weeks']
        mother_age = request.form['mother_age']
        mother_race = request.form['mother_race']
        prediction = predict.predict_weight(ismale, gestation_weeks, mother_age, mother_race)
        return('Predicted birth weight: {} lbs'.format(str(prediction)))
    else:
        return render_template('input.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080, debug = True)