from sqlalchemy import create_engine
from sqlalchemy import MetaData, ForeignKey
from sqlalchemy import Table, Column, Integer, String, Date, Numeric
from sqlalchemy import insert, select,update, delete
from datetime import date

metadata_obj = MetaData()

user_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String(30)),
    Column("password", String),
    Column("role",String, default="user")
)


products_table = Table(
    "products",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("price", Numeric(10,2)),
    Column("entry_date", Date),
    Column ("qty", Integer),
)

invoice_table = Table(
    "invoice",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("product_id", Integer,ForeignKey("products.id")),
    Column("qty", Integer),
    Column("total", Numeric(10,2)),
    Column("purchase_date", Date),
)

class DB_Manager:
    def __init__(self):
        self.engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')
        metadata_obj.create_all(self.engine)
        
    def insert_user(self, username, password):
        stmt = insert(user_table).returning(user_table.c.id,user_table.c.role).values(username=username, password=password)
        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        return result.all()[0]

    def get_user(self, username, password):
        stmt = select(user_table).where(user_table.c.username == username).where(user_table.c.password == password)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()

            if(len(users)==0):
                return None
            else:
                return users[0]

    def get_user_by_id(self, id):
        stmt = select(user_table).where(user_table.c.id == id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()
            if(len(users)==0):  
                return None
            else:
                return users[0]
    
    def get_product(self,table,name, price, entry_date, qty):
        query=select(table)
        if name:
            query = query.where(table.c.name == name)
        if price:
            query = query.where(table.c.price == price)
        if entry_date:
            query = query.where(table.c.entry_date == entry_date)
        if qty:
            query = query.where(table.c.qty == qty)
        with self.engine.connect() as conn:
            result = conn.execute(query)
            products = result.fetchall()
            return {"products": [dict(row._mapping) for row in products]}
        
    def get_product_by_id(self,table,id):
        query=select(table).where(table.c.id == id)
        with self.engine.connect() as conn:
            result = conn.execute(query)
            product = result.fetchone()
            return product

    def update_product_table(self,table,id,data):
        stmt = (
                update(table)
                .where(table.c.id==id)
                .values(**data))
        with self.engine.begin() as conn:
            result=conn.execute(stmt)
            return result.rowcount
        
    def delete_product(self,table,id):
        stmt= (
            delete(table)
            .where(table.c.id==id)
        )
        with self.engine.begin() as conn:
            result=conn.execute(stmt)
            return result.rowcount
    
    def create_product(self,table,name,price,entry_date,qty):
        stmt=(
            insert(table)
                .values(name=name, price=price,entry_date=entry_date,qty=qty))
        
        with self.engine.begin() as conn:
            result=conn.execute(stmt)
            return result.inserted_primary_key[0]
    
    def purchase_product(self,product_table,invoice_table,product_id,user_id,qty):
        row=self.get_product_by_id(product_table,product_id)
        if row:
            if row.qty>=qty:
                price=row.price*qty
                new_qty=row.qty-qty
                stmt=(
                    insert(invoice_table)
                    .values(user_id=user_id, product_id=product_id, qty=qty,total=price,purchase_date=date.today())
                )
                stmt2=(update(products_table)
                .where(products_table.c.id==product_id).values(qty=new_qty))
                with self.engine.begin() as conn:
                    result=conn.execute(stmt)
                    conn.execute(stmt2)
                    return result.inserted_primary_key[0]
            else:
                return "no_stock"
        else:   
            return "not_found"
        
    def get_invoices(self,invoice_table,user_id):
        query=select(invoice_table).where(invoice_table.c.user_id==user_id)
        with self.engine.connect() as conn:
            result=conn.execute(query)
            invoices=result.fetchall()
            return {"invoices": [dict(row._mapping) for row in invoices]}
