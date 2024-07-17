from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the model
model = joblib.load('fish_weight_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(request.form['length1']),
            float(request.form['length2']),
            float(request.form['length3']),
            float(request.form['height']),
            float(request.form['width'])]
    
    prediction = model.predict([data])
    
    return jsonify({'prediction': prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
