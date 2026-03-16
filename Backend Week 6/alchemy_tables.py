import sqlalchemy
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey,insert,select,update,delete

DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)

try:
    connection = engine.connect()
    print("Connection successful!")
    connection.close()  # Cerramos la conexion cuando terminamos
except Exception as e:
    print("Connection failed:", e)

metadata_obj=MetaData()

user_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30), nullable=False),
    Column("fullname", String, nullable=False),
)

addresses_table = Table(
    "addresses",
    metadata_obj,
    Column("id", Integer, primary_key=True), 
    Column("email", String, nullable=False),
    Column("user_id", ForeignKey("users.id"), nullable=False), #De esta manera declaramos una FK
)

cars_table=Table(
    "cars",
    metadata_obj,
    Column("id",Integer,primary_key=True),
    Column("user_id",ForeignKey("users.id"),nullable=True),
    Column("brand",String,nullable=False),
    Column("model",String,nullable=False),
    Column("mfg_year",Integer,nullable=False),
)
metadata_obj.create_all(engine)

class Cars():
    def __init__(self,cars_table):
        self.cars_table=cars_table

    def insert_car(self,brand_,model_,year_,user_id_=None):
        stmt=insert(self.cars_table).values(brand=brand_, model=model_,mfg_year=year_,user_id=user_id_)
        try:
            with engine.connect() as conn:
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print ("Database error:",e)

    def get_all_cars(self):
            stmt= select(self.cars_table)
            try:
                with engine.connect() as conn:
                    result = conn.execute(stmt)
                    return result.fetchall()
            except Exception as e:
                print ("Database error:",e)
    
    def update_car(self,id,**kwargs):
        stmt=(
            update(self.cars_table)
            .where(self.cars_table.c.id == id)
            .values(**kwargs)
        )
        try:
            with engine.connect() as conn:
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print ("Database error:",e)
        

    def assign_car_to_user(self, car_id, user_id):
        stmt = (
            update(self.cars_table)
            .where(self.cars_table.c.id == car_id)
            .values(user_id=user_id)
        )
        try:
            with engine.connect() as conn:
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print ("Database error:",e)

    def delete_car(self,id):
        stmt=(
            delete(self.cars_table)
            .where(self.cars_table.c.id==id)
        )
        try:
            with engine.connect() as conn:
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print ("Database error:",e)

class Users():
    def __init__(self,users_table_):
        self.users_table=users_table_
    
    def insert_user(self,name_,fullname_):
        stmt=insert(self.users_table).values(name=name_, fullname=fullname_)
        try:
            with engine.connect() as conn:
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print ("Database error:",e)

    def get_all_users(self):
        stmt= select(self.users_table)
        try:
            with engine.connect() as conn:
                result = conn.execute(stmt)
                return result.fetchall()
        except Exception as e:
            print("Database error:",e)
        
    def update_user(self,id,**kwargs):
        stmt=(
            update(self.users_table)
            .where(self.users_table.c.id == id)
            .values(**kwargs)
        )
        try:
            with engine.connect() as conn:
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print ("Database error:",e)

    def delete_user(self,id):
        stmt=(
            delete(self.users_table)
            .where(self.users_table.c.id==id)
        )
        try:
            with engine.connect() as conn:
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print ("Database error:",e)

class Addresses():
    def __init__(self,addresses_table):
        self.addresses_table=addresses_table
    
    def insert_address(self,email_,user_id_):
        stmt=insert(self.addresses_table).values(email=email_, user_id=user_id_)
        try:
            with engine.connect() as conn:
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print ("Database error:",e)

    def get_all_addresses(self):
        stmt= select(self.addresses_table)
        try:
            with engine.connect() as conn:
                result = conn.execute(stmt)
                return result.fetchall()
        except Exception as e:
            print("Database error:",e)
        
    def update_address(self,id,**kwargs):
        stmt=(
            update(self.addresses_table)
            .where(self.addresses_table.c.id == id)
            .values(**kwargs)
        )
        try:
            with engine.connect() as conn:
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print ("Database error:",e)
            
    def delete_address(self,id):
        stmt=(
            delete(self.addresses_table)
            .where(self.addresses_table.c.id==id)
        )
        try:
            with engine.connect() as conn:
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print ("Database error:",e)