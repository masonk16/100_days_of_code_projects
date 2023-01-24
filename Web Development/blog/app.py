from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blogs_url = ' https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blogs_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:blog_id>')
def get_blog(blog_id):
    blogs_url = ' https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blogs_url)
    all_posts = response.json()
    requested_post = None
    for blog_post in all_posts:
        if blog_post['id'] == blog_id:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
