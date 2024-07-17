# Fish Weight Prediction App

This Flask web application determines a fish's weight by measuring it and determining its species. A linear regression model trained on the Fish dataset powers the application.

## Features

- Estimates fish weight by using dimensions and species.
- After the form is submitted, the forecast appears on the same page.
- Simple to use in render mode.

## Dataset

The following columns are included in the Fish dataset (`Fish.csv}), which is used by the application:

Weight, Species, Length, Length2, Length3, Height, Width

## Setup

1. Make a repository clone:

    `{{ cd fish-weight-prediction git clone https://github.com/yourusername/fish-weight-prediction.git

2. Establish and turn on a virtual environment:

    ``} python -m venv venv source venv/bin/activate # Use `venv\Scripts\activate} on Windows }}

3. Set up the necessary dependencies:

    The command pip install -r requirements.txt

4. Verify that LabelEncoder and the trained model, {model.pkl}, are located in the root directory.

# Usage

Launch the Flask app first.

    This is a flask run.

2. Go to {http://127.0.0.1:5000} in your browser after opening it.

3. Enter the fish's measurements and species, then select "Predict" to obtain the estimated weight.

## Render-Deployed

Using Render, to implement this application:

Visit [Render](https://render.com/) and register or log in.

2. Link your GitHub repository to a new Web Service that you create.

3. Should `app.py` not be in the root, specify the root directory.

`gunicorn app:app} should be the start command setting.

5. Select "Create Web Service" by clicking.
