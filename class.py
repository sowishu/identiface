import mysql.connector
class Profile:
  def __init__(self,name,lastname,gender,age,address,phone,aadhar,mail):
      self.name=name
      self.lastname=lastname
      self.gender=gender
      self.age=age
      self.address=address
      self.phone=phone
      self.aadhar=aadhar
      self.mail=mail
      
class ProfileManager:
    
    def __init__(self):
        print("welcome")
         
    def createProfile(self,p):
        self.connection = self.__open()
        self.cursor = self.connection.cursor()
        sql = "INSERT INTO reg(name,lastname,gender,age,address,phone,aadhar,mail)VALUES('{}','{}','{}',{},'{}',{},'{}','{}')".format(p.name,p.lastname,p.gender,p.age,p.address,p.phone,p.aadhar,p.mail)
        print("sql:" +sql)
        self.cursor.execute(sql);
        self.connection.commit();
        
    def updateProfile(self,xyz,mail):
        self.connection = self.__open()
        self.cursor = self.connection.cursor()
        sql="update reg set age={} where mail='{}'".format(xyz,mail);
        print("sql:" +sql)
        self.cursor.execute(sql);
        self.connection.commit();
        self.connection=self.__close()
        
    def deleteProfile(self,mail):
        self.connection=self.__open()
        self.cursor=self.connection.cursor()
        sql="DELETE FROM reg where mail='{}'".format(mail);
        print("sql:"+sql)
        self.cursor.execute(sql);
        self.connection.commit();
        self.connection=self.__close()
        
    def __open(self):
        print("connection opened")
        self.connection=mysql.connector.connect(host='127.0.0.1',user='root',passwd='root' ,database='ishu')
        return self.connection
        
        
        
   
        
    def __close(self):
        print("connection closed")
        self.connection.close()
               
        
    
p=Profile("saavithri","hari","male",22,"north street",8978675432,"4444333222145","sivu@gmail.com")
#p1=Profile("dhivya","T","female",34,"first new street",9999999999,"77878787","jjj@hotmail.com")
manager = ProfileManager();
manager.createProfile(p)
#manager.deleteProfile("ishu@gmail.com");
#manager.updateProfile(55,"sivahari@gmail.com");

