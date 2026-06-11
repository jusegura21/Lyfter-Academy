from db import DB_Manager, products_table,invoice_table
from jwt_manager import JWTManager
from sqlalchemy import select
from flask import Flask, request, Response, jsonify


app = Flask("user-service")
db_manager = DB_Manager()
jwt_manager = JWTManager('RS256')

def get_product_data():
    data = request.args
    allowed_fields = {'name', 'price', 'entry_date', 'qty'}
    return {k: v for k, v in data.items() if k in allowed_fields}

def get_update_data():
    data = request.get_json()
    allowed_fields = {'name', 'price', 'entry_date', 'qty'}
    return {k: v for k, v in data.items() if k in allowed_fields}

def get_invoice_data():
    data = request.get_json()
    allowed_fields = {'product_id', 'qty'}
    return {k: v for k, v in data.items() if k in allowed_fields}

def get_user_id_from_token():
    token=request.headers.get('Authorization').split(" ")[1]
    payload=jwt_manager.decode(token)
    return payload['id']


def require_role(*roles):
    def decorator(f):
        def wrapper(*args, **kwargs):
            auth = request.headers.get('Authorization')
            if not auth:
                return Response(status=401)
            token=auth.split(" ")[1]
            payload = jwt_manager.decode(token)
            if not payload:
                return Response(status=401)
            if payload.get('role') not in roles:
                return Response(status=403)  
            return f(*args, **kwargs)
        wrapper.__name__ = f.__name__
        return wrapper
    return decorator

@app.route("/liveness")
def liveness():
    return "<p>Hello, World!</p>"


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # data is empty
    if(data.get('username') == None or data.get('password') == None):
        return Response(status=400)
    else:
        result = db_manager.insert_user(data.get('username'), data.get('password'))
        user_id = result[0]
        role=result[1]

        token = jwt_manager.encode({'id':user_id, 'role':role})
        
        return jsonify(token=token)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # data is empty
    if(data.get('username') == None or data.get('password') == None):
        return Response(status=400)
    else:
        result = db_manager.get_user(data.get('username'), data.get('password'))

        if(result == None):
            return Response(status=403)
        else:
            user_id = result[0]
            role=result[3]
            token = jwt_manager.encode({'id':user_id, 'role':role})
        
            return jsonify(token=token)

@app.route('/me')
@require_role('admin','user')
def me():
    try:
        user_id=get_user_id_from_token()
        user = db_manager.get_user_by_id(user_id)
        return jsonify(id=user_id, username=user[1])
    except Exception as e:
        return Response(status=500)
    
    
@app.route('/products', methods=["GET"])
@require_role('admin','user')
def get_products():
    data=get_product_data()
    result = db_manager.get_product(products_table, data.get("name"), data.get("price"), data.get("entry_date"), data.get("qty"))
    return jsonify(result),200   
    

@app.route('/products/<int:id>', methods=["PATCH"])
@require_role('admin')
def update_product_table(id):
    data=get_update_data()
    if data:
            result=db_manager.update_product_table(products_table,id,data)
            if result== 0: 
                return Response(status=404)
            else:
                return Response (status=200)
    else: 
        return Response(status=400)
    
    
@app.route('/products/<int:id>', methods=["DELETE"])
@require_role('admin')
def delete_product_from_table(id):
    result=db_manager.delete_product(products_table,id)
    if result == 0:
        return Response(status=404)
    else:
        return Response(status=200)


@app.route('/products', methods=["POST"])
@require_role('admin')
def products():
    data = get_update_data()
    required_fields = {'name', 'price', 'entry_date', 'qty'}
    if not required_fields.issubset(data.keys()):
        return Response(status=400)
    else: 
        result=db_manager.create_product(products_table,data["name"], data["price"],data["entry_date"],data["qty"])
        return jsonify(id=result), 201
    
@app.route('/purchase', methods=["POST"])
@require_role('admin','user')
def purchase_product():
    require_fields={'product_id','qty'}
    user_id=get_user_id_from_token()
    invoice_data=get_invoice_data()
    if not require_fields.issubset(invoice_data.keys()):
        return Response(status=400)            
    result=db_manager.purchase_product(products_table,invoice_table,invoice_data["product_id"],user_id,invoice_data["qty"])
    if result=="not_found":
        return jsonify(error=result), 404 
    elif result=="no_stock":
        return jsonify(error=result),400
    else:
        return jsonify(id=result),201

    
@app.route('/myinvoices',methods=["GET"])
@require_role('admin','user')
def get_my_invoices():
    try:
        user_id=get_user_id_from_token()
        result=db_manager.get_invoices(invoice_table,user_id)
        return jsonify(result), 200
    except Exception as e:
        return Response(status=401)

if __name__ == '__main__':
    app.run(debug=True)