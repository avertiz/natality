![Python application test with Github Actions](https://github.com/avertiz/natality/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg?branch=main)
# Natality
This is a repository that holds all code necessary to deploy a model that predicts a child's birth weight when born. Google Cloud Platform is needed for the machine learning portion. Google BigQuery has this dataset available for free, but it can also be found elsewhere on th internet. 

## Here is an overview of what each file accomplishes
#### requirements.txt
  * Packages needed for this project
#### Makefile
  * Basic scoffolding for environment setup and package installation
#### `test.py`
  * script for testing
#### `predict.py`
  * The script that calls the model to make a prediction based on inputs given by the user.
  * The model was generated using the natality dataset and Google BigQuery ML https://cloud.google.com/bigquery-ml/docs/introduction
#### `main.py`
  * The script that generated the web app.
  * This is run on the the Flask framework.
#### `app.yaml`
  * basic yaml file that Google App Engine needs to deploy the app
#### `templates/input.html`
  * The html script for the web app that `main.py` calls. 
