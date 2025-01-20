#venv\Scripts\activate
#python app.py


from flask import Flask, render_template, request
from livereload import Server

app = Flask(__name__)
app.debug = True

@app.route('/')
def mainpage():
    return render_template('landing.html')


@app.route('/submit', methods=['POST'])

def submit():
        name = request.form['name']
        name1 = request.form['name1']
        return "name is " + name + " " + name1

server = Server(app.wsgi_app)
server.watch("templates/*.*") 
server.watch("./static/css/*.*") 
server.serve(port=5000)