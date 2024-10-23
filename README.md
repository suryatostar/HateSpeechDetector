# Hate Speech Detection

This repository contains a machine learning project aimed at detecting hate speech in text data. The project involves training a Logistic Regression model to classify text as hate speech or not, using various features extracted from the text data.
Project Overview

The increasing use of the internet and social media has led to the proliferation of online hate speech. Manual detection and removal of such content are nearly impossible given the scale and volume of data. This project addresses this issue by leveraging machine learning to automate the detection of hate speech in text.
Key Features

    Dataset: The model is trained on a dataset of over 700,000 data points.
    Preprocessing: The text data undergoes several preprocessing steps such as tokenization, vectorization, and scaling.
    Model: Logistic Regression is used for classification, and it achieves high performance in terms of accuracy and F1 score.
    Evaluation: The model's performance is evaluated using a confusion matrix and ROC curve.
    Pipeline: A complete pipeline is implemented, combining vectorization, standard scaling, and the Logistic Regression model.

## Files in this Repository

    Hate Speech Detection.ipynb: The Jupyter notebook containing the entire workflow, from data preprocessing to model training and evaluation.
    hateSpeech.pkl: The trained machine learning model saved for future use.

## Dependencies

### To run this project, you will need the following Python packages:

    pandas
    numpy
    scikit-learn
    matplotlib
    seaborn
    joblib

## You can install the dependencies by running:

bash

''' pip install -r requirements.txt '''

## Usage

    Clone the repository:

bash

""" git clone https://github.com/yourusername/hate-speech-detection.git '''

    Install the required dependencies.

    Run the Jupyter notebook to train the model or use the saved model for predictions.

    To make predictions using the saved model:

python
"""
import joblib
model = joblib.load("hateSpeech.pkl")
predictions = model.predict(your_input_data) """

Model Performance

## The model achieves the following metrics on the test dataset:

    Accuracy: 85.34%
    F1 Score: 85.53%

## Conclusion

Machine learning provides an effective solution for detecting hate speech online. This project demonstrates the use of a Logistic Regression model trained on a large dataset to automate the detection of harmful content.
License

### This project is licensed under the MIT License.
