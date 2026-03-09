# import flask
import base64
from datetime import date
from flask_cors import CORS
from flask import *
# importing pymysql
import pymysql
# importing the cursor from pymysql
import pymysql.cursors

# CORS = Cross Origin Resource Sharing

# initialise the flask app
app = Flask(__name__)
CORS(app)

import os
app.config["UPLOAD_FOLDER"] = "static/images"

# define route/end-point for the corresponding web application function
@app.route("/api/signup", methods= ['POST'])
# function corresponding to the route
# below is signup in route
def signup():
    # getting user inputs
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    phone = request.form["phone"]

    # establishing a connection to our database
    connection = pymysql.connect (user="vicmakau", host="mysql-vicmakau.alwaysdata.net", password="modcom1234", database="vicmakau_sokogarden")
    
    # defining the cursor
    cursor = connection.cursor()
    
    # sql query to insert data into the database
    sql = "insert into users(username, password, email, phone) values(%s, %s, %s, %s)"
    # defining the data to replace the placeholders
    data = (username, password, email, phone)

    # execute the SQL query
    cursor.execute(sql, data)

    # commiting changes to the database
    connection.commit()

    return jsonify ({"Success": "Thank you for signing up"})

# Below is the login/sign in route
@app.route("/api/signin", methods=["POST"])
def signin():
    if request.method == "POST":
        # extract the two details entered on the form 
        email = request.form["email"]
        password  = request.form["password"]

        # prnt out the details entered
        # print(email, password)

        # create/establish a connection to the database
        connection = pymysql.connect(host="mysql-vicmakau.alwaysdata.net", user="vicmakau", password="modcom1234", database="vicmakau_sokogarden")

        # create a cursor
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        # structure the sql query that will check whether the email and password entered are correct
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"

        # put the data received from the form in a tuple
        data = (email, password)


        # by use of the cursor execute the sql
        cursor.execute(sql, data)

        # check whetehr there are rules and store the on a variable
        count= cursor.rowcount
        # print(count)

        # if there are records returned it means that the password and emails are correct otherwise it means they are wrong
        if count== 0:
            return jsonify({"Message":"login fail"})
        else:
            # there must be a user so we create a variable that will hold the details of the user fetched from the database
            user=cursor.fetchone()
            # return the details to th front end as well as a message
            return jsonify({"Message":"User logged in successfully", "user":user})    

# add_product api
# creating the route for add_products
@app.route("/api/add_product", methods= ['POST'])

# define the corresponding web application function
def add_product():
    # get user inputs
    product_name = request.form["product_name"]
    product_description = request.form["product_description"]
    product_cost = request.form["product_cost"]
    # extracting the image data
    photo = request.files["product_photo"]
    # extracting the image filename
    filename = photo.filename

    # defining the photos file path
    photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    # Saving the file path
    photo.save(photo_path)
        
    # establish a connection to the database
    connection = pymysql.connect(user="vicmakau", host="mysql-vicmakau.alwaysdata.net", password="modcom1234", database="vicmakau_sokogarden")

    # define the cursor
    cursor= connection.cursor()

    # define the sql query
    sql = "insert into product_details (product_name, product_description, product_cost, product_photo) values(%s, %s, %s, %s)"

    # prepare/define the data
    data = (product_name, product_description, product_cost, filename)

    # execute SQL query
    cursor.execute(sql,data)

    # commit/save to databse
    connection.commit()

    # Return a response to the user
    return jsonify ({"Message": "Product has been added successfully"})


# get_product_details API
# defining the route
@app.route("/api/get_product_details")
# defining the corresponding web application function
def get_product_details ():

    # establish connection to the database
    connection = pymysql.connect(user ="vicmakau", host ="mysql-vicmakau.alwaysdata.net", password ="modcom1234", database ="vicmakau_sokogarden")

    # define the cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # defining the sql query
    sql = "select * from product_details"

    # execute the sql query
    cursor.execute(sql)

    # fetching all rows retrieved by  the sql query
    product_details = cursor.fetchall()
    
    # closing the database connection
    connection.close()
    # return a response to the user
    return jsonify(product_details)



# Mpesa Payment Route/Endpoint 
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth
 
@app.route('/api/mpesa_payment', methods=['POST'])
def mpesa_payment():
    if request.method == 'POST':
        amount = request.form['amount']
        phone = request.form['phone']
        # GENERATING THE ACCESS TOKEN
        # create an account on safaricom daraja
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"
 
        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
 
        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']
 
        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')
 
        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",  # use 1 when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/api/confirmation.php",
            "AccountReference": "account",
            "TransactionDesc": "account"
        }
 
        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }
 
        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL
 
        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return jsonify({"message": "Please Complete Payment in Your Phone and we will deliver in minutes"})
# run the app
# app.run(debug= True) --- IGNORE ---