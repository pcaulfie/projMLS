# Project 2020

## Project for Machine Learning and Statistics in 2020.

## Introduction
This repository contains my submission for the Tasks assessment for Machine Learning and Statistics in 2020.

The repository contains the following:

1. A file containing the data set called *powerproduction.csv*.
1. A [Jupyter notebook](https://github.com/pcaulfie/projMLS/blob/main/Project%202020%20-%20Machine%20Learning%20and%20Statistics.ipynb) that trains a model using the data set. 
1. Python script *powerapp.py* that runs a web service based on the model, as above.
1. Dockerfile *xxxx* to build and run the web service in a container.
1. Requirements.txt file which lists all packages needed to run the script.
1. Gitignore file
1. Images folder containing some images used in the readme and jupyter notebook.
1. Licence
1. Readme

## Summary
The objective of this project is to create a web service that uses machine learning to make predictions based on the *powerproduction* data set. The project consiste of the following elements:
* A jupyter notebook, where I train a number of models which aim to accurately predicts wind turbine power output from wind speed values, found in the data set. Contained in the notebook, I explain each model and give an analysis of its accuracy.
* A python script, which uses the best model. This script will run the web service.
* A dockerfile to build and run the web service in a container. This will respond with predicted power values based on speed values sent as HTTP requests. 

## Installation

- I recommend that you install the [Anaconda](https://www.anaconda.com/distribution/) distribution of python which contains all the libraries used, as well as an instance of Jupyter notebook.

## Instructions
  ### Windows
  set FLASK_APP=powerapp.py
  python -m flask run
  
  docker build . -t powerapp-image
  docker run --name powerapp-container -d -p 5000:5000 powerapp-image
 
 ### Linux
  export FLASK_APP=powerapp.py
  python3 -m flask run

### Clone

- Clone this repository to your local machine use the following link `https://github.com/pcaulfie/projMLS.git`

### References

## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
- **[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)**

## Contact

Paul Caulfield -  paul.caulfield@se.com & g00376342@gmit.ie
