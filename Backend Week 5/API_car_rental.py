from flask import Flask
from flask import request
import os
import psycopg2
from psycopg2.extras import RealDictCursor

connection = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="postgres",
    dbname="postgres",
)
print("Connected to the database")

cursor=connection.cursor(cursor_factory=RealDictCursor)
cursor.execute("SELECT version();")
print("Query executed")


app = Flask(__name__)

@app.route("/users",methods=["POST"])
def insert_user():
    data=request.get_json()
    if not data:
        return {"error": "invalid request"}, 400
    name=data["name"]
    username = data["username"]
    password = data["password"]
    email = data["email"]
    birth_date = data["birth_date"]
    account_status = data["account_status"]
    cursor.execute(
        """
        INSERT INTO lyfter_car_rental.users
        (name, username,password,email,birth_date,account_status)
        VALUES (%s,%s,%s,%s,%s,%s);
        """,
        (name,username,password,email,birth_date,account_status))
    print("Query executed")
    connection.commit()
    print("connection changes commited.")
    return {"message": "user created"}, 201

@app.route("/cars", methods=["POST"])
def insert_car():
    data=request.get_json()
    if not data:
        return {"error": "invalid request"}, 400
    brand=data["brand"]
    model=data["model"]
    mfg_year=data["mfg_year"]
    car_status=data["car_status"]
    cursor.execute(
        """
        INSERT INTO lyfter_car_rental.cars
        (brand,model,mfg_year,car_status)
        VALUES (%s,%s,%s,%s);
        """,
        (brand,model,mfg_year,car_status)
    )
    connection.commit()
    print("connection changes commited.")
    return {"message": "car created"}, 201

@app.route("/rentals",methods=["POST"])
def insert_rent():
    data=request.get_json()
    if not data:
        return {"error": "invalid request"}, 400
    car_id=data["car_id"]
    user_id=data["user_id"]
    cursor.execute(
        """
        INSERT INTO lyfter_car_rental.rentals
        (car_id,user_id)
        VALUES (%s,%s);
        """,
        (car_id,user_id)
    )
    connection.commit()
    return {"message": "rental created"}, 201

@app.route("/cars/<int:id>/status",methods=["PATCH"])
def car_status_change(id):
    cursor.execute(
    """
UPDATE lyfter_car_rental.cars
SET car_status = NOT car_status
WHERE id = %s 
""", (id,)
    )
    connection.commit()
    return {"message":"car status updated"}

@app.route("/users/<int:id>/status",methods=["PATCH"])
def user_status_change(id):
    cursor.execute(
        """
UPDATE lyfter_car_rental.users
SET account_status = NOT account_status
WHERE id = %s 
""", (id,)
    )
    connection.commit()
    return {"message":"user status updated"}

@app.route("/rentals/<int:id>/complete", methods=["PATCH"])
def complete_rental(id):
    cursor.execute(
        """
UPDATE lyfter_car_rental.rentals
SET rental_status=FALSE 
WHERE id = %s """,(id,))
    cursor.execute("""
    UPDATE lyfter_car_rental.cars
    SET car_status =TRUE 
    WHERE id= (SELECT car_id FROM lyfter_car_rental.rentals WHERE id= %s);
    """,(id,))
    connection.commit()
    return {"message": "rental completed"}

@app.route("/rentals/<int:id>/status", methods=["PATCH"])
def rent_status_change(id):
    cursor.execute(
        """
UPDATE lyfter_car_rental.rentals
SET rental_status= NOT rental_status
WHERE id= %s
""",(id,))
    connection.commit()
    return{"message":"rent status changed"}

@app.route("/users/<int:id>/delinquent",methods=["PATCH"])
def flag_user(id):
    cursor.execute("""
UPDATE lyfter_car_rental.users
SET account_status = FALSE 
WHERE id = %s
""",(id,))
    connection.commit()
    return {"message":"user flagged"}

@app.route("/users", methods=["GET"])
def get_users():
    username = request.args.get("username")
    email = request.args.get("email")
    account_status = request.args.get("account_status")

    query = "SELECT * FROM lyfter_car_rental.users WHERE 1=1"
    values = []

    if username:
        query += " AND username = %s"
        values.append(username)

    if email:
        query += " AND email = %s"
        values.append(email)

    if account_status:
        query += " AND account_status = %s"
        values.append(account_status)

    cursor.execute(query, tuple(values))

    users = cursor.fetchall()

    return {"users": users}

@app.route("/cars", methods=["GET"])
def get_cars():
    brand = request.args.get("brand")
    model = request.args.get("model")
    mfg_year = request.args.get("mfg_year")
    car_status = request.args.get("car_status")

    query = "SELECT * FROM lyfter_car_rental.cars WHERE 1=1"
    values = []

    if brand:
        query += " AND brand = %s"
        values.append(brand)

    if model:
        query += " AND model = %s"
        values.append(model)

    if mfg_year:
        query += " AND mfg_year = %s"
        values.append(mfg_year)

    if car_status:
        query += " AND car_status = %s"
        values.append(car_status)

    cursor.execute(query, tuple(values))

    cars = cursor.fetchall()

    return {"cars": cars}


@app.route("/rentals", methods=["GET"])
def get_rentals():

    user_id = request.args.get("user_id")
    car_id = request.args.get("car_id")
    rental_status = request.args.get("rental_status")

    query = "SELECT * FROM lyfter_car_rental.rentals WHERE 1=1"
    values = []

    if user_id:
        query += " AND user_id = %s"
        values.append(user_id)

    if car_id:
        query += " AND car_id = %s"
        values.append(car_id)

    if rental_status:
        query += " AND rental_status = %s"
        values.append(rental_status)

    cursor.execute(query, tuple(values))

    rentals = cursor.fetchall()

    return {"rentals": rentals}
