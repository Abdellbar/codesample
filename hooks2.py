#!/usr/bin/python
from flask import Flask
from flask import request
import flask
import json
from sparkapi import sparkapi
from memeapi import memeapi
import shutil
import os


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
   roomId = data['data']['roomId']
   print msg_id
   input_ret = sparkbot.get_msg(str(msg_id))
   #print input_list
   #print word.split()[1]
   print str(input_ret[1])

   if str(input_ret[1]) == 'help' :
      print "in help"
      with open ("help.txt", "r") as myfile:
           help_file=myfile.readlines()

      sparkbot.post_msg(str(roomId),help_file)
   else: 
      print "in genral "
      input_list = input_ret[1].split('|')
      image_file=memegen.get_image(input_list[0],input_list[1],input_list[2])
      print  "done"

      image_name = str(msg_id) +'.jpeg'
      with open(image_name, 'wb') as out_file:
            shutil.copyfileobj(image_file.raw, out_file)
      del image_file


      
      print roomId
      sparkbot.post_msg(str(roomId),"got that")
      print "hello"

      sparkbot.post_file(str(roomId),image_name)

      try:
          os.remove(image_name)
      except Exception as error:
          app.logger.error("Error removing or closing downloaded file handle", error)
          print "error removing file" 
          print error
  

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
       print error
   return "OK"

if __name__ == '__main__':
   app.run()
