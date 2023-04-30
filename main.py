# imported Flask and render_template class from flask module
from flask import Flask, render_template

# imported FlaskForm class from flask_wtf module
from flask_wtf import FlaskForm

# imported StringField class from wtforms module
from wtforms import StringField, PasswordField, SubmitField


# created an instance of the Flask class and stored it in a variable called app
app = Flask(__name__)

# variable to store the secret key
app.secret_key = 'dfvwejnilo3442-hjguuiuygl32r23!@#'

"""class to create a form with a username and password field"""
class Login_Form(FlaskForm):
    email = StringField(label='Email')
    password = PasswordField(label='Password')
    submit = SubmitField(label='Log In')

# created a route decorator to tell Flask what URL should trigger our function
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    login_form = Login_Form()
    return render_template('login.html', form=login_form)

# check if the executed file is the main program and run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)