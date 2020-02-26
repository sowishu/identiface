from flask import Flask, render_template, request

from flaskext.mysql import MySQL

mysql=MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='my_db'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)

@app.route('/')
def my_form():
    return render_template('exa.html')
@app.route('/', methods=["POST"])
def Authenticate():
    name=request.form['name']
    lastname = request.form['lastname']
    gender=request.form['gender']
    age = request.form['age']
    address = request.form['address']
    phone = request.form['phone']
    aadhar = request.form['aadhar']
    mail = request.form['mail']


    cursor=mysql.connect().cursor()
    cursor.execute("INSERT INTO register(name,lastname,gender, age, address, phone, aadhar, mail ) VALUES ('"+name+"','"+lastname+"','"+gender+"', "+age+",'"+address+"',"+phone+",'"+aadhar+"','"+mail+"' ")
    




if __name__ == '__main__':
    app.run()
