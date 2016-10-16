#!/usr/bin/python
from flask import Flask
from flask import request
import flask
import json
from sparkapi import sparkapi
from memeapi import memeapi
import shutil


app = Flask(__name__)
sparkbot = sparkapi()
memegen  = memeapi()



@app.route('/hello',methods=['POST'])
def parsing():
   print "got that reqest "
   data = request.json
   print "parrsed"
   #print format(data['data']['id'])
   msg_id = data['data']['id']
   input_list = sparkbot.get_msg(str(msg_id))
   #print input_list
   #print word.split()[1]
   
   image_file=memegen.get_image(input_list[0],input_list[1],input_list[2])
   print  "done"

   image_name = str(msg_id) +'.jpeg'
   with open(image_name, 'wb') as out_file:
         shutil.copyfileobj(image_file.raw, out_file)
   del image_file


   roomId = data['data']['roomId']
   print roomId
   sparkbot.post_msg(str(roomId),"got that")
   print "hello"

   sparkbot.post_file(str(roomId),image_name)


   return 'OK'

@app.route("/imgs/<path:path>")
def images(path):
    #generate_img(path)
    fullpath =  path # "./imgs/" + path
    resp = flask.make_response(open(fullpath).read())
    resp.content_type = "image/jpeg"
    return resp

@app.route("/delete/<path:path>")
def removefile(path):
   try:
       os.remove(path)
   except Exception as error:
       app.logger.error("Error removing or closing downloaded file handle", error)
       print "error removing file"
   return response

if __name__ == '__main__':
   app.run()
