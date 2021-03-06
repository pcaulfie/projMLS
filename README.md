# Project 2020

## Course: Machine Learning and Statistics

* Student Name: Paul Caulfield
* Student No: G00376342

* Lecturer: Ian McLoughlin 

An assignment submitted in part fulfilment of the requirements of the Higher Diploma in Science - Data Analytics: 2020-2021, Galway Mayo Institute of Technology.

## Introduction
This repository contains my submission for Project 2020 for Machine Learning and Statistics. The objective of this project is to create a web service that uses machine learning to make predictions based on the *powerproduction* data set.

![Wind Turbines](static/wind-turbines.jpg)
(Image courtesy: Shutterstock/Robert-Lucian-Crusitu)

The repository contains the following:

## Contents 

| File |      Title                | Description |Link|
|------|---------------------------|---------|------|
| 1    | Project 2020 - Machine Learning and Statistics.ipynb | A jupyter notebook, where I train several models using machine learning to make predictions based on the *powerproduction* data set. Contained in the notebook, I explain each model and give an analysis of its accuracy.|https://github.com/pcaulfie/projMLS/blob/main/Project%202020%20-%20Machine%20Learning%20and%20Statistics.ipynb|
| 2    | windapp.py | A python script, which uses the best model. This script will run the web service. |https://github.com/pcaulfie/projMLS/blob/main/windapp.py|
| 3    | Dockerfile | A dockerfile to build and run the web service in a container.[1]  This will respond with predicted power values based on speed values sent as HTTP requests.  |https://github.com/pcaulfie/projMLS/blob/main/Dockerfile
| 4    | powerproduction.csv | A file containing the data set used to develop the model. |https://github.com/pcaulfie/projMLS/blob/main/powerproduction.csv|
| 5   | requirements.txt | A file which lists all packages needed to run the script. [1]  |https://github.com/pcaulfie/projMLS/blob/main/requirements.txt|
| 6    | index.html | A web interface, using jquery to pass data to and from windapp.py script. |https://github.com/pcaulfie/projMLS/blob/main/static/index.html|
| 7    | .dockerignore | File containing a list of files and/or directories instructs the docker daemon to ignore when building the image (docker build). [1] |https://github.com/pcaulfie/projMLS/blob/main/.dockerignore|
| 9    |.gitignore | A file used to tell git which files are not needed to be added to the repository. |https://github.com/pcaulfie/projMLS/blob/main/.gitignore|

## Installation
  
### Clone This Repository [4]
| Step |      Task                | Instructions |
|------|---------------------------|---------|
| 1    | Install Anaconda distribution of python which contains all the libraries used.| [Anaconda](https://www.anaconda.com/distribution/)|
| 2    | Launch Cmder or other similar console.| cmder|
| 3    | create a folder where you want to clone the repository.| for example *cd folder/to/clone-into/*|
| 4    | Specify URL of the repository you want to clone.| *git clone https://github.com/pcaulfie/projMLS.git*|

### Requirements.txt
Here is a list of the packages needed to run this application. 

click==7.1.2
Flask==1.1.2
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
numpy==1.19.4
pandas==1.2.0
scikit-learn==0.23.1
python-dateutil==2.8.1
pytz==2020.5
six==1.15.0
Werkzeug==1.0.1

### Set Up Flask Server [2]
| Step |      Task                | Windows |Mac / Linux|
|------|---------------------------|---------|------|
| 1    | set environmental variables  | SET FLASK_APP=windapp|export FLASK_APP=windapp |
| 2    | set DEBUG MODE   | export FLASK_ENV=development |export FLASK_DEBUG=1 |
| 3   | run flask server   | python -m flask run |python3 -m flask run |
| 4    | open web app on local host   | http://127.0.0.1:5000/ | http://127.0.0.1:5000/ |


### Set Up Docker [3]
| Step |      Task                | Command |
|------|---------------------------|---------|
| 1    | Install Docker Desktop  | https://docs.docker.com/docker-for-windows/install/|
| 2    | Build Image   | docker build -t power-app . |
| 3   | Run   | docker run --name power-container -d -p 5000:5000 power-app |
| 4    | open web app on local host   | http://127.0.0.1:5000/ |

### Troubleshooting Docker Issues [3]
1. Open Docker Desktop and check that the container you built is running - see screenshot below to see an example.
![Step1](static/Screenshot3.JPG)
2. Click on the container name to view the logs - see screenshot below to see an example.
![Step2](static/Screenshot4.JPG)

### How to Use The App
1. Open web app on local host http://127.0.0.1:5000/
2. Enter Wind Speed Value in white input box: input a value between 7.5 and 24.5 meters per second. 
![Step1](static/Screenshot1.JPG)
3. Click on Predict Power Values (Blue Button) and the result will be displayed in greyed out box - this result displayed is the wind turbine power output prediction in kilowatts.
![Step2](static/Screenshot2.JPG)

## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
- **[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)**

### References
* [1] McLoughlin, I., “Dockerfiles ,”
2020, [Online; accessed 5-January-2021]. [Online]. Available: https://web.microsoftstream.com/video/03bfee62-fdeb-4dbe-a7d2-393d1aa40b66
* [2] McLoughlin, I., “Random numerical app ,”
2020, [Online; accessed 5-January-2021]. [Online]. Available: https://github.com/ianmcloughlin/random-app/blob/master/README.md
* [3] Docker.com, “Install Docker Desktop on Windows ,”
2017, [Online; accessed 5-January-2021]. [Online]. Available: https://docs.docker.com/docker-for-windows/install/
* [4] Github, “Cloning a repository ,”
2020, [Online; accessed 27-December-2020]. [Online]. Available: https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository

## Contact

Paul Caulfield -  paul.caulfield@se.com & g00376342@gmit.ie
