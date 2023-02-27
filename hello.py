from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def index(): 
    return render_template(
        'home.html.jinja',
        my_variable="assfsffwf",
        my_list=['apples','bananas','orange'])



@app.route("/ping")
def ping():
    return"<p>pong</p>"

@app.route("/hello/<name>")
def hello(name):
    return f"<p>hello,{name}!</p>"
