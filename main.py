from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return '<h1 style = "text-align: center">Hello, World!</h1>'\
           '<p>Giddy Up.</p>'\
           '<img src ="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTdkMDVqYndyeGp4YWkwcjlnanE1eDM1cmpuanB5MXUwYnBodW5pbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2A75RyXVzzSI2bx4Gj/giphy.webp" width = 500>'


@app.route("/bye")
def say_bye():
    return "Bye!"

@app.route("/username/<name>/<int:number>")
def say_name(name, number):
    return f"Hello, {name}! you are {number} year old "

if __name__ == "__main__":
    app.run(debug=True)