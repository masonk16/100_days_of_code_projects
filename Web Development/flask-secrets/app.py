from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import Email

app = Flask(__name__)


class LoginForm(FlaskForm):
    email = EmailField('email', validators=[Email()])
    password = PasswordField('password')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
