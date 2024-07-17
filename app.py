from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('fish_weight_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve data from the HTML form
    length1 = float(request.form['length1'])
    length2 = float(request.form['length2'])
    length3 = float(request.form['length3'])
    height = float(request.form['height'])
    width = float(request.form['width'])

    # Create a feature vector based on the model's requirements
    data = np.array([[length1, length2, length3, height, width, 0, 0, 0, 0, 0, 0]])

    # Perform prediction
    prediction = model.predict(data)[0]  # Assuming the model returns a single prediction

    # Pass prediction to the template
    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
