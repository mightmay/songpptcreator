



from flask import Flask, request, send_from_directory, send_file 



@app.route('/')
def hello_world():

    return 'Hello, World!'

    

if __name__ == '__main__':
  app.run()
