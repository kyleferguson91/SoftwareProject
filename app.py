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
        username = request.form['username']
        password = request.form['password']
        return "name is " + username + "passwordis" + password


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/registernewuser', methods=['POST'])
def regnew():
    return "new user register here"


server = Server(app.wsgi_app)
server.watch("templates/*.*") 
server.watch("./static/css/*.*") 
server.serve(port=5000)