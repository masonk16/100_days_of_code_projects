from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/')
def hello_world():
    # Rendering HTML within the return
    return '<h1 style="text-align: center; ">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://i.pinimg.com/originals/e6/0a/b2/e60ab23aa17dff0db3e76312bb4d7ec2.jpg" style="margin: auto;">' \
           '<img src="https://media.giphy.com/media/8GehNdh9Cj6es/giphy.gif">'


@make_bold
@make_emphasis
@make_underlined
@app.route('/bye')
def say_bye():
    return 'Bye!'


# Creating variable paths and converting the path to a specified data type
@app.route("/<string:name>/<int:number>")
def greeting(name, number):
    return f'Hello {name}, you are {number} years old!'


if __name__ == "__main__":
    # Run app in debug mode to auto-reload and access Flask debugger.
    app.run(debug=True)
