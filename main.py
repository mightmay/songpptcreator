from flask import Flask
import sys
import traceback
app = Flask(__name__)

@app.route('/')
def hello_world():
    returnstring="start..."
    returnstring=returnstring+"import..."
#    import createppt
    returnstring=returnstring+"createppt.imported..."
#    try:
#        import lxml
#    except Exception:
#        tb=str(traceback.format_exc())
#        return(tb)

    return(returnstring)

if __name__ == '__main__':
    app.run()
