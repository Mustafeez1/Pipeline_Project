from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('titanic_prediction.pkl', 'rb'))

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
    app.run(host='0.0.0.0', port=5000)  # Port set to 9090
