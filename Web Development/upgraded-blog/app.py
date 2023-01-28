from flask import Flask, render_template
import requests

app = Flask(__name__)

posts_url = 'https://api.npoint.io/2306a432815ce8b775f1'
response = requests.get(posts_url)
posts_data = response.json()


@app.route('/')
def index():
    posts = posts_data
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
