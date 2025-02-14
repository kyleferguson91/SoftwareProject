#venv\Scripts\activate
#python app.py


from flask import Flask, render_template, request
from livereload import Server
import database

app = Flask(__name__)
app.debug = True

@app.route('/')
def mainpage():
    database.createLoginDB()
    return render_template('landing.html')


@app.route('/submit', methods=['POST'])

def submit():
        username = request.form['username']
        password = request.form['password']
        
        #function to check if user is in the database, if so we will proceed to homepage
        # if not in database we will direct to the register form!

        if(database.userExists(username, password)):
            print("user exists go to login")
            return render_template('userhomepage.html', name=username)
        else:
            print("user does not exist go to register")
            return render_template('register.html')
      
        
        #database call in here!
    
    

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/registernewuser', methods=['POST'])
def regnew():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    database.addUsertoDb(username, password, email)
    #we should re route to a homepage now
    print("redirect to homepage")
    return render_template('userhomepage.html', name=username)


server = Server(app.wsgi_app)
server.watch("templates/*.*") 
server.watch("./static/css/*.*") 
server.serve(port=5000)