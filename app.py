from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)
model = pickle.load(open('titanic_prediction.pkl', 'rb'))

# Get the port from the environment variable, default to 5000 if not set
port = int(os.getenv('FLASK_PORT', 5000))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        prediction = model.predict([features])
        output = 'Survived' if prediction[0] == 1 else 'Did Not Survive'
        return render_template('index.html', prediction_text=f'Prediction: {output}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    # Run the app on the port dynamically set by the environment variable
    app.run(host='0.0.0.0', port=port)
