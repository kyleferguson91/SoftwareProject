import mysql.connector
from mysql.connector import Error
import os

#r root mycatiscool  sql8.3
def createLoginDB():
    try:
        connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mycatiscool'

        )
        if connection.is_connected():
            print("connected")
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS blossomblueprint")
            cursor.execute("use blossomblueprint")
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(25) NOT NULL,
            password VARCHAR(25) NOT NULL,
            email VARCHAR(30) NOT NULL
    
            )
            ''')
            connection.commit()
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            print("Connected MySQL Server Version:", version[0])
            print("database and user table created")


    except Error as e:
        print(f"errror: {e}")
    finally:    
        if connection.is_connected:
           cursor.close()
           connection.close()
           
           
           
           
def getDBConnection():
    try:
        connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mycatiscool'
     
        )
    except Error as e:
        print(f"error: {e}")
    finally:
        if connection.is_connected:
            print("connection granted via getDBconnection")
            return connection


def addUsertoDb(username, password, email):
    try:
        connection = getDBConnection()
        if connection.is_connected:
            print("connection established adding user now")
            cursor = connection.cursor()
            cursor.execute("use blossomblueprint")
            insert_query = f'''
                INSERT INTO users (username, password, email)
                VALUES ('{username}', '{password}', '{email}')
            '''
            if (userExists(username, password) != True):
                cursor.execute(insert_query)
                connection.commit()
                print("user has been added!")
            else:
                print("user exists!")
    except Error as e:
        print(f"error: {e}")
    finally:
        cursor.close()
        connection.close()
        
    

def userExists(username, password):
    try:
        connection = getDBConnection()
        if connection.is_connected:
                #successful connection we want to use the ddatabase
                 cursor = connection.cursor()
                 cursor.execute("use blossomblueprint")
                 query = "select * from users WHERE username = %s and password =%s"
                 cursor.execute(query, (username, password))
                 result = cursor.fetchone()
                 
                 if result:
                     return True
                 else:
                    return False
    #here we query database and check if the username and password match!
    # if we get a result return true if not return false!
    except Error as e:
        print(f"error: {e}")
    finally:
        connection.close()
        cursor.close()
        print("login in db, proceed to home page")



def createGardenTable():
    try:
        connection = getDBConnection()
        if connection.is_connected:
                #successful connection we want to use the ddatabase
                 cursor = connection.cursor()
                 cursor.execute("use blossomblueprint")
                 cursor.execute('''
                                CREATE TABLE IF NOT EXISTS garden (
                                    garden_id INTEGER PRIMARY KEY,
                                    garden_name TEXT NOT NULL,
                                    user_id INTEGER,
                                    FOREIGN KEY (user_id) REFERENCES users(id)
                                )
                            ''')
                 connection.commit()

    except Error as e:
        print(f"error: {e}")
    finally:
        connection.close()
        cursor.close()
        print("garden table created")


def createPlantTable():
    try:
        connection = getDBConnection()
        if connection.is_connected:
                #successful connection we want to use the ddatabase
                 cursor = connection.cursor()
                 cursor.execute("use blossomblueprint")
                 cursor.execute('''
                                CREATE TABLE IF NOT EXISTS plant (
                                    plant_id INTEGER PRIMARY KEY,
                                    plat_name TEXT NOT NULL,
                                    plant_type TEXT,
                                    
                                )
                            ''')
                 connection.commit()

    except Error as e:
        print(f"error: {e}")
    finally:
        connection.close()
        cursor.close()
        print("garden table created")


def createUserGardenTable():
    try:
        connection = getDBConnection()
        if connection.is_connected:
                #successful connection we want to use the ddatabase
                 cursor = connection.cursor()
                 cursor.execute("use blossomblueprint")
                 cursor.execute('''
                                CREATE TABLE IF NOT EXISTS user_garden_plants (
                                    garden_id AUTO_INCREMENT INTEGER PRIMARY KEY,
                                    plant_id TEXT NOT NULL,
                                    quantity INTEGER NOT NULL
                                    PRIMARY KEY (garden_id, plant_id),  
                                    FOREIGN KEY (garden_id) REFERENCES garden(garden_id),
                                    FOREIGN KEY (plant_ID) REFERENCES plant(plant_id)
                                )
                            ''')
                 connection.commit()

    except Error as e:
        print(f"error: {e}")
    finally:
        connection.close()
        cursor.close()
        print("garden table created")

