from flask import Flask, request, redirect, render_template
import re

app=Flask(__name__)
app.config['DEBUG']=True 

@app.route("/")
def display_user_signup_form():
    print("Inside sign up form")
    return render_template('form.html')

@app.route("/validate_form", methods=['POST'])
def validate():
    username_error_txt = ""
    password_error_txt = ""
    re_password_error_txt = ""
    email_error_txt = ""

    username_txt = request.form["username"]
    if(username_txt == ""):
        username_error_txt = "User Name should not be an empty!"
    
    if(username_txt != "" ):
        if(" " in username_txt):
            username_error_txt = "User Name should not contain space between"
        
        if(len(username_txt) < 3 or len(username_txt) > 20):
            username_error_txt = "User Name should not be less tha 3 or more than 20 characters"
    
    password_txt = request.form["password"]
    if(password_txt == ""):
        password_error_txt = "Password should not be an empty!"
    
    if(password_txt != ""):
        if(" " in password_txt):
            password_error_txt = "Password should not contain space between"

        if(len(password_txt) < 3 or len(password_txt)  > 20):
            password_error_txt = "Password should not be less tha 3 or more than 20 characters"
    

    re_password_txt = request.form["re_password"]
    if((re_password_txt == "" and password_txt != "") or (password_txt != re_password_txt)):
       re_password_error_txt = "Passwords don't match"

    email_txt = request.form["email"]

    if(email_txt != ""):
        if(len(email_txt) < 3 or len(email_txt)  > 20):
            email_error_txt = "Email should not be less tha 3 or more than 20 characters"

        if(not (re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email_txt))):
            email_error_txt = "That's not a valid email"

    if(not username_error_txt and not password_error_txt and not re_password_error_txt and not email_error_txt):
        return render_template('welcome.html', username = username_txt)
    else:
        return render_template('form.html', username_error = username_error_txt, password_error = password_error_txt, re_password_error = re_password_error_txt, email_error = email_error_txt, username = username_txt, email = email_txt)


app.run()