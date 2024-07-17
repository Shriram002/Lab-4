from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model and LabelEncoder
with open('model.pkl', 'rb') as f:
    model, le = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    df = pd.DataFrame([data])
    
    # Encode the 'Species' column
    df['Species'] = le.transform(df['Species'])
    
    # Convert the input data to float
    for column in df.columns:
        df[column] = df[column].astype(float)
    
    prediction = model.predict(df)
    prediction_result = round(prediction[0], 2)
    
    return render_template('index.html', prediction_text=f'Predicted Weight: {prediction_result} grams')

if __name__ == '__main__':
    app.run(debug=True)
