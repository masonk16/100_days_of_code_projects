from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.secret_key = 'pajmheckxbinpgsmgzgeqzawvubkyqowifgbupjetxwhxcmwrbhrqnkfzjwdhyas'
csrf = CSRFProtect(app)


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
