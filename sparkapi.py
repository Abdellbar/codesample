#!/usr/bin/python
import unirest
import json

class sparkapi:

  def __init( self, x=0):
      self.key = 'Bearer ZTg1ZGVlNTEtMDIyYy00YWU1LTllMTctYmRjMTMzNWI2MGIwNmE5YmMxNGYtNGU4'

  def get_msg(self,id):
    response = unirest.get("https://api.ciscospark.com/v1/messages/"+id,
      headers={
        "Authorization": "Bearer ZTg1ZGVlNTEtMDIyYy00YWU1LTllMTctYmRjMTMzNWI2MGIwNmE5YmMxNGYtNGU4"
      }
    )
    cmnd_text = response.body['text'].split(' ',1)
    print cmnd_text
    #cmnd_list = cmnd_text[1].split('|')
    #print string
    return cmnd_text
  def post_msg(self,grp,msg):
    response = unirest.post("https://api.ciscospark.com/v1/messages/",
      headers={
        "Authorization": "Bearer ZTg1ZGVlNTEtMDIyYy00YWU1LTllMTctYmRjMTMzNWI2MGIwNmE5YmMxNGYtNGU4",
        "Content-Type":"application/json"
      },
      params=json.dumps({"roomId":grp,"text":msg})
    )
    print response.body
  def post_file(self,grp,file_o):

    response = unirest.post("https://api.ciscospark.com/v1/messages/", 
      headers={
        "Authorization": "Bearer ZTg1ZGVlNTEtMDIyYy00YWU1LTllMTctYmRjMTMzNWI2MGIwNmE5YmMxNGYtNGU4",
        "Content-Type":"application/json"},
      params=json.dumps({"roomId":grp,"files":["https://secret-brushlands-95547.herokuapp.com/imgs/"+file_o]})
    )    

  def post_txt_file(self,grp,file_o):

    response = unirest.post("https://api.ciscospark.com/v1/messages/", 
      headers={
        "Authorization": "Bearer ZTg1ZGVlNTEtMDIyYy00YWU1LTllMTctYmRjMTMzNWI2MGIwNmE5YmMxNGYtNGU4",
        "Content-Type":"application/json"},
      params=json.dumps({"roomId":grp,"files":["https://secret-brushlands-95547.herokuapp.com/txt/"+file_o]})
    )  

"""    
app = sparkapi()

if __name__ == '__main__':
    #app.get_msg("Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYjg3Y2UyNDAtOTE0Mi0xMWU2LTk0YjktMTlhYzNjNGFkMTZj")
    app.post_msg('Y2lzY29zcGFyazovL3VzL1JPT00vMjk0YWUyODAtOTE1NS0xMWU2LTk0YjktMTlhYzNjNGFkMTZj','hellow world')

"""