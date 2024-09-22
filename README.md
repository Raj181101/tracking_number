# Setup

Download Python by using link [download python](https://www.python.org/downloads/).

## Clone the repository

To get the repository, run the following command to clone the project

`git clone https://github.com/Raj181101/tracking_number.git`

Now move to project folder after completion of clone using following command

`cd tracking_number`

## Installation

Install virtual environment module using pip.

`pip install virtualenv`

Create virtual environment using following commands after virtualenv installed

`virtualenv venv` or `python -m venv venv`

Activate virtual environment after venv is created by using following command

`venv\Scripts\activate` #Windows

`source venv\bin\activate` #Linux

Now install all required dependencies from requirements.txt file using below command

`pip install -r requirements.txt`


## Run Server

After completion of all above steps, now run the django server by using below command

`python manage.py runserver` 

The above command will start the server in [localhost](http://127.0.0.1:8000/) http://127.0.0.1:8000/.


## Test the application

Test the Api endpoint in postman or by pasting in browser

Api Endpoint without query params: [Api Endpoint](http://127.0.0.1:8000/apis/next-tracking-number/) , if you click on this link it will throw 400 bad request status with the message of required query params

Api Endpoint with query params : [Api Endpoint](http://127.0.0.1:8000/apis/next-tracking-number/?origin_country_id=MY&destination_country_id=ID&weight=1.335&customer_id=de619854-b59b-425e-9db4-943979e1bd49&customer_name=bhargav%20reddy), if you click on this link it will give 200 status with successful generation of 16 length tracking number along with time with all mentioned considerations

