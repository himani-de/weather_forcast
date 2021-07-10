## Weather Forecast Platform

### Table of Contents
1. [Overview](#Overview)
2. [Design-Overview](#Design-Overview)
3. [Usage](#Usage)
4. [Project-layout](#Project-layout)
5. [Project-Details](#Project-Details)
6. [Output](#Output)
7. [Notes](#Notes)

#### Overview
Who am I ! I am an weather forecaster application where you can check the weather data of today and plan your day accordingly.
I provide not only the basic parameters like temperature, rain forecast but more than that like humidity, uv index, maximum and minimum temperature etc so that you have a better idea about 
how the day is going to be.

#### Design-Overview:
- We are using https://weatherstack.com/ & https://openweathermap.org/ two websites api which provides the weather data.
- We are interested in the present day data so that the restaurant owner can plan outside sitting arrangements for that day.
- We are accessing the apis of the above mentioned website and extracting required data.
- As both the api are somehow providing some similar data like temperature, humidity, feels like & some different parameters as well.
- so, we are carefully creating the final dataframe in such a way that all columns are different and have data from both the apis.
- Finally, to provide a UI for the end user we are rendering the table, so that user can access it in form of a website.

#### Usage
* **Step 1**: Save the project folder in your local system.
* **Step 2**: `cd weather_forecast`
* **Step 3**: Run `pip install -r requirements.txt`.
* **Step 4**: Run `python app.py`
* **Step 4**: Access the web page using $machine_ip:9090

#### Project-layout
```
├── static
├── templates
|── .env
├── app.py
├── weather_data.py
├── weather_main.py
├── requirements.txt
├── README.md
```

#### Project-Details
- static: It contains the css styling file which will style the html page.
- templates- It has the index.html file which creates an html page for our app.
- .env- It contains the api access key for bor both the apis.
- app.py- It is the main file which we will run in order to see the data in web page.
- weather_data.py: This file gets the data from "open-weather api" % def "get_data_open_weather" stores the data.
- Weather_main.py: This file gets the data from "weatherstack.com" and calls the definition "get_data_open_weather"
- to create the combined dataframe from both the apis.
- requiremets.txt: It has all the libraries which we have used in creating this app.
- README.md: Deatiled information about the app.

#### Output
![Output](img/Output.png)

#### Notes
- This app provides data of present day:
- The weatherstack.com api provides the data of current time.
- The open weather api gives the data of every 3 hours of the day starting from 12 am to 9 pm.
- In order to access the json data use this api using "$machine_ip:9090/api"
- The api keys are stored in .env file and are encrypted using git-secret.

### Limitation
This code has been tested on following operating systems.
 * MacOS 11.4

This code has been tested on following Python Versions.
* Python 3.8.3