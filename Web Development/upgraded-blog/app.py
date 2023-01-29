import os

from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)

posts_url = 'https://api.npoint.io/2306a432815ce8b775f1'
response = requests.get(posts_url)
posts_data = response.json()


FROM_EMAIL = os.getenv('FROM_EMAIL')
FROM_PASSWORD = os.getenv('FROM_PASSWORD')
TO_EMAIL = os.getenv('TO_EMAIL')


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
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        send_email(name=name, email=email, phone=phone, message=message)
        return render_template('form-success.html')
    return render_template('contact.html')


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(FROM_EMAIL, FROM_PASSWORD)
        connection.sendmail(FROM_EMAIL, TO_EMAIL, email_message)


if __name__ == '__main__':
    app.run(debug=True)
