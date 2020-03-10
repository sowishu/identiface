import mysql.connector


class Profile:
    def __init__(self, id,name,lastname,gender,age,address,phone,aadhar, mail):
     print("test")
     self.name = name;
     self.lastname=lastname;
     self.gender=gender;
     self.age=age;
     self.address=address;
     self.phone=phone;
     self.aadhar=aadhar;
     self.mail=mail;
     self.id=id;



class ProfileManager:
    def __init__(self):
        print("welcome");

    def createProfile(self, p):

        self.connection = self.__open()
        self.cursor = self.connection.cursor()
        sql = "INSERT INTO profile(id,name, lastname,gender, age, address, phone, aadhar, mail)" \
              "VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')"\
            .format(p.id,p.name,p.lastname, p.gender, p.age, p.address,p.phone, p.aadhar, p.mail)
        print("sql:" + sql)
        self.cursor.execute(sql);
        self.connection.commit();
        self.connection = self.__close();

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

    def select(self,p):
        self.connection=self.__open();
        self.cursor=self.connection.cursor();
        sql="SELECT name ,lastname,gender,age,address,phone, aadhar,mail from profile where id='{}'".format(p.id);
        print(sql)
        self.cursor.execute(sql)
        row=self.cursor.fetchone()

        self.connection = self.__close()
        return row

    #'sowndarya', 'murali', 'None', '23', '115A, east chitra', '9876543210', '54678934658712', 'sow@gmail.com'



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

#p=Profile('ishu')
#p=Profile("dhivya","T","female",34,"first new street",9999999999,"77878787","jjj@hotmail.com")
#manager = ProfileManager();
#manager.createProfile(p)
# manager.deleteProfile("ishu@gmail.com");
# manager.updateProfile(55,"sivahari@gmail.com");