#venv\Scripts\activate
#python app.py


from flask import Flask, render_template, request, jsonify, session

from livereload import Server
import database, requests, mongodatabase
from flask_session import Session


#setup app and sessoin
app = Flask(__name__)
app.debug = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem" 
Session(app)


@app.route('/')
def mainpage():
    #create mongo database too!
    database.createLoginDB()
    mongodatabase.createMongoDB()
    return render_template('landing.html')


@app.route('/submit', methods=['POST'])

def submit():
        username = request.form['username']
        password = request.form['password']
        
        #function to check if user is in the database, if so we will proceed to homepage
        # if not in database we will direct to the register form!

        if(database.userExists(username, password)):
            id = database.getUserID(username)
            
            mongodatabase.addUserToMongo(username, id)
            print("redirect to homepage", "username = ", username, "userid = ", id)

            session["userid"] = id  
            print(session["userid"])
            #configure session to store userid across files


            return render_template('userhomepage.html', name=username, userid = id)
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
    id = database.getUserID(username)
    session["userid"] = id  
    mongodatabase.addUserToMongo(username, id)
    print("redirect to homepage", "username = ", username, "userid = ", id)
    return render_template('userhomepage.html', name=username, userid = id)






@app.route("/addplant", methods=["POST"])
def add_plant():
    try:
        data = request.json  
        plantid = data.get("plantid")
        plantobj = data.get("plantobj", {})
        where = data.get("where")

        if not plantid or not where:
            return jsonify({"error": "Missing required fields"}), 400
        id = session["userid"]
        print("preparing to add ", plantid, "to ", where, "at user id", id, plantobj )
        #details coming through ok, now to add to the certain garden
        mongodatabase.addPlantDetailstoMongo(plantid, plantobj, where)
        print("added plant to mongo")
        return "added"
    except Exception as e:
        print("did not add plant to mongo")
        return jsonify({"error": str(e)}), 500
    
 
@app.route("/removeplant", methods=["POST"])   
def remove_plant():
    data = request.json  
    plantid = data.get("plantid")
    where = data.get("where")
    print("remove plant logic here")
    mongodatabase.removePlant(where, plantid)
    return "removed"


@app.route('/populatefavsgarden', methods=['POST'])
def populatefavsgarden():
    
    #get an array from mongo db based on the current user, either garden or favs items
    id = session["userid"]
    data = request.json  
    where = data.get("where")
    
    
    print("populatefavsgardencalled where equals", where)
    collection = mongodatabase.returnPlantDetails(where)
    print (collection, "collection from populatefavfarden app.py")
    if not collection:
            return 404
    return collection
    
        
        
 



server = Server(app.wsgi_app)
server.watch("templates/*.*") 
server.watch("./static/css/*.*") 
server.serve(port=5000)

