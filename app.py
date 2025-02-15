#venv\Scripts\activate
#python app.py


from flask import Flask, render_template, request, jsonify

from livereload import Server
import database, requests

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
    
    
TREFLE_API_TOKEN = "HNuaT0HHqWTCpIbUeoRL8tc8EIz6fsOjX0htmSl6VFE"
API_URL = "https://permapeople.org/api"
HEADERS = {
    "Content-Type": "application/json",
    "x-permapeople-key-id": "lTCNgEvhGFlD",
    "x-permapeople-key-secret": "d577227e-ba13-4ce3-8bf0-3242029d8498"
    }
@app.route("/search", methods=["GET"])
def search_plants():

    try:
        q = request.args.get("q")

        response = requests.post("https://permapeople.org/api/search?q="+q, headers= HEADERS)
        print(q, response)
        # Check if response is successful
        response.raise_for_status()
        data = response.json()
       
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    finally:
        print('api search')

    '''
    print("backend /searchroute")
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Missing query parameter"}), 400

    trefle_url = f"https://trefle.io/api/v1/plants/search?token={TREFLE_API_TOKEN}&q={query}"

    try:
        response = requests.get("https://trefle.io/api/v1/plants?token=HNuaT0HHqWTCpIbUeoRL8tc8EIz6fsOjX0htmSl6VFE")
    
        return response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
    '''


@app.route("/randomplants", methods=["GET"])
def random_plants():
    try:
        index = request.args.get("lastid", default=0, type=int)
        
        api_url =  f"https://permapeople.org/api/plants?lastid={index}"
        print("index in randomplants api is ", index)
        print("url is ", api_url)
        response = requests.get(api_url, headers= HEADERS)
        print(response)
        # Check if response is successful
        response.raise_for_status()
        data = response.json()
        print(data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    finally:
        print('api random plants')

    

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