from flask import Flask, render_template,request, redirect
import pymysql.cursors
import pymysql
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app= Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


connection= pymysql.connect(
   
    host="10.100.33.60",
    user="mkhan",
    password='221085624',
    database='mkhan_2ndTable',
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True

)


a=["I want to have been able to get an work experience that can aquire me some financial gain", "Get my drivers license"]
cursor= connection.cursor()
 
@app.route("/")
def index(): 
    cursor.execute("SELECT * FROM `Todo` ORDER BY `COMPLETED`")
    result= cursor.fetchall()
    
    print(result[0]['Description'])

    print(type(result))



    return render_template(
        'todotem.html.jinja',result=result)
    
@app.route("/add",methods=['POST'])
@auth.login_required
def add():
    new_todo= request.form['new_todo']
    a.append(new_todo)        
    cursor.execute(f"INSERT INTO `Todo`(`Description`) VALUES ('{new_todo}') ")
    return redirect("/")
    
@app.route("/complete", methods = ['POST'])
def complete():

    todo_id = request.form ['todo_id']

    cursor = connection.cursor()
    
    cursor.execute(f"UPDATE `Todo` SET `Completed` = 1 WHERE `id` = {todo_id}" )

    return redirect("/")





        