import glob
import urllib
import base64

import face_recognition
from flask import Flask, request, render_template

from dbop import Profile, ProfileManager
from binascii import a2b_base64
import base64
import datetime
import time
import calendar
import cv2
from cv2 import imread
import os



app = Flask(__name__)
#def student():!pip install cmake dlib face_recognition numpy opencv-python


@app.route('/dataentry',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      name = result.get('name')
      lastname=result.get('lastname')
      gender=result.get('gender')
      age=result.get('age')
      address=result.get('address')
      phone=result.get('phone')
      aadhar= result.get('aadhar')
      mail=result.get('mail')
      imgUrl = result.get('img')


      up = urllib.parse.urlparse(imgUrl)
      head, data = up.path.split(',', 1)
      bits = head.split(';')
      mime_type = bits[0] if bits[0] else 'text/plain'
      charset, b64 = 'ASCII', False
      for bit in bits:
         if bit.startswith('charset='):
            charset = bit[8:]
         elif bit == 'base64':
            b64 = True

      # Do something smart with charset and b64 instead of assuming
      #plaindata = data.decode("base64")
      plaindata = base64.b64decode(data)

      epoch = time.time()
      print(epoch)
      e2 = calendar.timegm(time.gmtime())
      e1=str(e2)+".jpg"
      print("Current Image saved :"+e1)

      # Do something smart with mime_type
      with open(e1, 'wb') as f:
         f.write(plaindata)

      p=Profile(e2,name,lastname,gender,age,address,phone, aadhar,mail);
      pm=ProfileManager();
      pm.createProfile(p);
   return render_template('DataEntry.html')

@app.route('/fetch',methods = ['POST', 'GET'])
def fetch():
   if request.method == 'POST':
      result = request.form
      imgUrl = result.get('img')

      up = urllib.parse.urlparse(imgUrl)
      head, data = up.path.split(',', 1)
      bits = head.split(';')
      mime_type = bits[0] if bits[0] else 'text/plain'
      charset, b64 = 'ASCII', False
      for bit in bits:
         if bit.startswith('charset='):
            charset = bit[8:]
         elif bit == 'base64':
            b64 = True

      plaindata = base64.b64decode(data)
      with open("tmp.jpg", 'wb') as f:
         f.write(plaindata)

      curr_img = face_recognition.face_encodings(face_recognition.load_image_file("tmp.jpg"))[0]
      matchingFile = ""
      for file in glob.glob("*.jpg"):
        if(file != "tmp.jpg" and matchingFile == ""):
          dir_img = face_recognition.face_encodings(face_recognition.load_image_file(file))[0]
          img_result = face_recognition.compare_faces([dir_img], curr_img)
          print("Compare " + file + " and tmp.jpg")
          print(img_result)
          if(img_result == [True]):
             matchingFile = file

   id,txt = matchingFile.split('.',1)
   print("Matching file : "+matchingFile)
   p=Profile(id,'','','','','','','','');
   pm=ProfileManager();
   row=pm.select(p);
   return render_template('DataResult.html',Rname=row[0],Rlastname=row[1],Rgender=row[2],Rage=row[3],Raddress=row[4],Rphone=row[5],Raadhar=row[6],Rmail=row[7])


if __name__ == '__main__':
   app.run(debug = True)