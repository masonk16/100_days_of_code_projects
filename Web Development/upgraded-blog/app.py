from flask import Flask, render_template, request
import requests

app = Flask(__name__)

posts_url = 'https://api.npoint.io/2306a432815ce8b775f1'
response = requests.get(posts_url)
posts_data = response.json()


@app.route('/')
def index():
    posts = posts_data
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    requested_post = None
    for blog_post in posts_data:
        if blog_post['id'] == post_id:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)



@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact',  methods=["GET", "POST"])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')
    elif request.method == 'POST':
        return render_template('form-success.html')


# @app.route('/form-success', methods=["POST"])
# def receive_data():



if __name__ == '__main__':
    app.run(debug=True)
