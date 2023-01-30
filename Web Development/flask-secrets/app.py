from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import EmailField, PasswordField

app = Flask(__name__)

app.secret_key = 'pajmheckxbinpgsmgzgeqzawvubkyqowifgbupjetxwhxcmwrbhrqnkfzjwdhyas'
csrf = CSRFProtect(app)


class LoginForm(FlaskForm):
    email = EmailField('email')
    password = PasswordField('password')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
