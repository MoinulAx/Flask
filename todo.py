from flask import Flask, render_template,request, redirect
import pymysql.cursors
import pymysql

app= Flask(__name__)


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
    cursor.execute("SELECT * FROM `Todo`")

    result= cursor.fetchall()
    
    print(result[0]['Description'])

    print(type(result))



    return render_template(
        'todotem.html.jinja',result=result)
    

@app.route("/add",methods=['POST'])
def add():
    new_todo= request.form['new_todo']
    a.append(new_todo)        
    cursor.execute(f"INSERT INTO `Todo`(`Description`) VALUES ('{new_todo}') ")

    return redirect(('/'))






        