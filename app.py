from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo

app = Flask(__name__) # Main constructor
app.config['SECRET_KEY'] ='f5c489e7d6f1d7f1baf21fc0af63bd81da37aa78'
app.config['MONGO_URI'] = "mongodb+srv://retsuko64:<Password>@userdatabase.y6dccqo.mongodb.net/user?retryWrites=true&w=majority"
# Replace <Password> with your own password


# Set up MongoDB
mongodb_client = PyMongo(app)
db = mongodb_client.db


@app.route('/', methods=['POST', 'GET']) # Login Page
def index():
   
    if request.method == 'POST': 
        # Getting the inputted information
        chk_login = request.form['email']
        chk_password = request.form['password']

        # Checking for if the user exist then check their password if it's correct
        
        chk_user = db.user_collection.find_one({"email": chk_login}) # retrieve user
        if chk_user['email'] is not None: # if found
            if chk_user['password'] == chk_password: # check their password
                return redirect(url_for('result')) # if correct go to 'result.html' page

    else:
        return render_template('index.html')


@app.route('/register', methods=['POST', 'GET']) # Register Page
def register():
    if request.method == 'POST': #if user clicks on the register button

        # Getting the inputted information
        new_email = request.form['email']
        new_password = request.form['password']
        new_name = request.form['name']
        new_surname = request.form['surname']

        # Note that the variable 'user_collection' can be any other name
        db.user_collection.insert_one(
            {
            "email": new_email,
            "password": new_password,
            "name": new_name,
            "surname": new_surname
            })
        return redirect(url_for('index')) # Go back to login page
    
    else: # If user asks for the page
        return render_template('register.html')
    
@app.route('/result') # result page
def result():
    return render_template('result.html')
    

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

    
