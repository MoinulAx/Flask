from flask import Flask, render_template,request

app= Flask(__name__)

a=["I want to have been able to get an work experience that can aquire me some financial gain", "Get my drivers license"]

@app.route("/")
def index(): 
    return render_template(
        'todotem.html.jinja',a=a)

@app.route("/add",methods=['POST'])
def add():
    new_todo= request.form['new_todo']
    a.append(new_todo)        
    return (a)

        