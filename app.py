#venv\Scripts\activate
#python app.py


from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)
app.debug = True

@app.route('/')



def mainpage():
    return render_template('landing.html')






server = Server(app.wsgi_app)
server.watch("templates/*.*") 
server.watch("./static/css/*.*") 
server.serve(port=5000)