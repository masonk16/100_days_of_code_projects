from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', random_number=random_number, year=current_year)


@app.route('/guess/<string:name>')
def guess(name):
    gender_response = requests.get(f'https://api.genderize.io?name={name}')
    gender = gender_response.json()['gender']
    age_response = requests.get(f'https://api.agify.io?name={name}')
    age = age_response.json()['age']

    return render_template('guessing.html', name=name, gender=gender, age=age)


@app.route('/blog')
def blog():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
