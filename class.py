from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import app
from app import result
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'
mysql = MySQL(app)

@app.route('/')
def student():
   return render_template('DataEntry.html')


@app.route('/', methods=['GET', 'POST'])
def result():
    if request.method == "POST":
        result = request.form
        name=result.get('name')

    class Profile:
        def __init__(self, name):
            self.name = name

    return render_template('DataEntry.html')


class ProfileManager:

    def __init__(self):
        print("welcome")

    def createProfile(self, p):
        self.connection = self.__open()
        self.cursor = self.connection.cursor()
        sql = "INSERT INTO summa(name)VALUES('{}')".format(
            p.name)
        print("sql:" + sql)
        self.cursor.execute(sql);
        self.connection.commit();

    def updateProfile(self, age, mail):
        self.connection = self.__open()
        self.cursor = self.connection.cursor()
        sql = "update reg set age={} where mail='{}'".format(age, mail);
        print("sql:" + sql)
        self.cursor.execute(sql);
        self.connection.commit();
        self.connection = self.__close()

    def deleteProfile(self, mail):
        self.connection = self.__open()
        self.cursor = self.connection.cursor()
        sql = "DELETE FROM reg where mail='{}'".format(mail);
        print("sql:" + sql)
        self.cursor.execute(sql);
        self.connection.commit();
        self.connection = self.__close()

    def __open(self):
        print("connection opened")
        self.connection = mysql.connector.connect(host='127.0.0.1', user='root', passwd='root', database='chennai')
        return self.connection

        # def help(self):
        self.insert(p)
        self.__open

    def __close(self):
        print("connection closed")
        self.connection.close()


#p = Profile(name)
# p1=Profile("dhivya","T","female",34,"first new street",9999999999,"77878787","jjj@hotmail.com")
#manager = ProfileManager();
#manager.createProfile(p)
# manager.deleteProfile("ishu@gmail.com");
# manager.updateProfile(55,"sivahari@gmail.com");






if __name__ == '__main__':
    app.run()