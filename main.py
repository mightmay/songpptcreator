import os



from flask import Flask, request, send_from_directory, send_file 



@app.route('/')
def hello_world():

    #createppt.getsongdata(lyricfile,1,1,1)
    try:
        return "test"
    except Exception as e:
        return str(e)
    

if __name__ == '__main__':
  app.run()
