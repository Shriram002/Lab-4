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

1. Made a repository clone:

    `{{ cd fish-weight-prediction git clone https://github.com/Shriram002/Shriram002-Enterprise-System-determine-the-Fish-Weight

2. Established and turn on a virtual environment:

    ``} python -m venv venv source venv/bin/activate # Use `venv\Scripts\activate} on Windows }}

3. Set up the necessary dependencies:

    The command pip install -r requirements.txt

4. Verifyied that LabelEncoder and the trained model, {model.pkl}, are located in the root directory.

# Usage

Launched the Flask app first.

Enter the fish's measurements and species, then select "Predict" to obtain the estimated weight.

## Render-Deployed

Using Render, to implement this application:

1. Link your GitHub repository to a new Web Service that you create.

2. Should `app.py` not be in the root, specify the root directory.

3. gunicorn app:app should be the start command setting.

4. Select "Create Web Service" by clicking.
