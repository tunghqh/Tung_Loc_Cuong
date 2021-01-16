from flask import Flask
from flask import request
from flask import jsonify

import os

from BusinessObject import Customer as CustomerEntity
from DataObject import Customer

from BusinessObject import Categories as CategoriesEntity
from DataObject import Categories

from BusinessObject import Employees as EmployeesEntity
from DataObject import Employees

from BusinessObject import OrderDetails as OrderDetailsEntity
from DataObject import OrderDetails

from BusinessObject import Suppliers as SuppliersEntity
from DataObject import Suppliers

from BusinessObject import Orders as OrdersEntity  
from DataObject import Orders

from BusinessObject import Products as ProductsEntity  
from DataObject import Products

from BusinessObject import Shippers as ShippersEntity 
from DataObject import Shippers

app = Flask(__name__)


connection_data = dict()
connection_data['host'] = os.getenv('host')
connection_data['user'] = os.getenv('user')
connection_data['password'] = os.getenv('password')
connection_data['port'] = os.getenv('port')
connection_data['database'] = os.getenv('database')

@app.route('/')
def home():
    return 'This is backend'

@app.route('/index', methods=['GET'])
def index():
    return 'This is index page'

# CRUD(Create, Read, Update, Delete)
# POST, GET, PUT, DELETE

@app.route('/customer', methods=['POST'])
def add_customer():
    data = request.json
    customer = CustomerEntity(customer_name=data['customer_name'],
                                contact_name=data['contact_name'],
                                address=data['address'],
                                city=data['city'],
                                postal_code=data['postal_code'],
                                country=data['country'])
    c = Customer(connection_data)
    message = c.insert(customer)
    if message is None:
        return jsonify({
            'message': 'Cannot insert data'
        }), 500
    return jsonify({
        'message': message
    })

@app.route('/customer/all')
def get_all_customer():
    c = Customer(connection_data)
    result = c.get_all()
    return jsonify({
        'data': result
    })

@app.route('/customer/<int:id>', methods=['DELETE', 'PUT'])
def delete_customer_by_id(id):
    if request.method == 'DELETE':
        # Delete user by id
        customer = CustomerEntity(customer_id=id)
        c = Customer(connection_data)
        result = c.delete(customer)
        return jsonify({
            'message': result[0]
        }), result[1]
    else:
        # Update user by id
        data = request.json
        customer = CustomerEntity(customer_id=id,
                                    customer_name=data['customer_name'],
                                    contact_name=data['contact_name'],
                                    address=data['address'],
                                    city=data['city'],
                                    postal_code=data['postal_code'],
                                    country=data['country'])
        c = Customer(connection_data)
        result = c.update(customer)
        return jsonify({
            'message': result[0]
        }), result[1]
        #--------------------bang 2  ----------------------------------------------
        

@app.route('/categories', methods=['POST'])
def add_categories():
    data = request.json
    categories = CategoriesEntity(category_name=data['category_name'],
                                description=data['description']
                               )
    c = Categories(connection_data)
    message = c.insert(categories)
    if message is None:
        return jsonify({
            'message': 'Cannot insert data'
        }), 500
    return jsonify({
        'message': message
    })

@app.route('/categories/all')
def get_all_categories():
    c = Categories(connection_data)
    result = c.get_all()
    return jsonify({
        'data': result
    })

@app.route('/categories/<int:id>', methods=['DELETE', 'PUT'])
def delete_categories_by_id(id):
    if request.method == 'DELETE':
        # Delete user by id
        categories = CategoriesEntity(category_id=id)
        c = Categories(connection_data)
        result = c.delete(categories)
        return jsonify({
            'message': result[0]
        }), result[1]
    else:
        # Update user by id
        data = request.json
        categories = CategoriesEntity(category_id=id,
                                     category_name=data['category_name'],
                                    description=data['description']
                                   )
        c = Categories(connection_data)
        result = c.update(categories)
        return jsonify({
            'message': result[0]
        }), result[1]

        #---------------------------bang 3-----------------------------

@app.route('/employees', methods=['POST'])
def add_employees():
    data = request.json
    employees = EmployeesEntity(last_name=data['last_name'],
                                first_name=data['first_name'],
                                birth_date=data['birth_date'],
                                photo=data['photo'],
                                notes=data['notes']
                                )
    c = Employees(connection_data)
    message = c.insert(employees)
    if message is None:
        return jsonify({
            'message': 'Cannot insert data'
        }), 500
    return jsonify({
        'message': message
    })

@app.route('/employees/all')
def get_all_employees():
    c = Employees(connection_data)
    result = c.get_all()
    return jsonify({
        'data': result
    })

@app.route('/employees/<int:id>', methods=['DELETE', 'PUT'])
def delete_employees_by_id(id):
    if request.method == 'DELETE':
        # Delete user by id
        employees = EmployeesEntity(employee_id=id)
        c = Employees(connection_data)
        result = c.delete(employees)
        return jsonify({
            'message': result[0]
        }), result[1]
    else:
        # Update user by id
        data = request.json
        employees = EmployeesEntity(employee_id=id,
                                    last_name=data['last_name'],
                                    first_name=data['first_name'],
                                    birth_date=data['birth_date'],
                                    photo=data['photo'],
                                    notes=data['notes']
                                    )
        c = Employees(connection_data)
        result = c.update(employees)
        return jsonify({
            'message': result[0]
        }), result[1]

        #--------------------------------------------------------------


@app.route('/orderdetails', methods=['POST'])
def add_orderdetails():
    data = request.json
    orderdetails = OrderDetailsEntity(order_id=data['order_id'],
                                product_id=data['product_id'],
                                quantity=data['quantity']
                                )
    c = OrderDetails(connection_data)
    message = c.insert(orderdetails)
    if message is None:
        return jsonify({
            'message': 'Cannot insert data'
        }), 500
    return jsonify({
        'message': message
    })

@app.route('/orderdetails/all')
def get_all_orderdetails():
    c = OrderDetails(connection_data)
    result = c.get_all()
    return jsonify({
        'data': result
    })

@app.route('/orderdetails/<int:id>', methods=['DELETE', 'PUT'])
def delete_orderdetails_by_id(id):
    if request.method == 'DELETE':
        # Delete user by id
        orderdetails = OrderDetailsEntity(order_detail_id=id)
        c = OrderDetails(connection_data)
        result = c.delete(orderdetails)
        return jsonify({
            'message': result[0]
        }), result[1]
    else:
        # Update user by id
        data = request.json
        orderdetails = OrderDetailsEntity(order_detail_id=id,
                                    order_id=data['order_id'],
                                    product_id=data['product_id'],
                                    quantity=data['quantity']
                                    )
        c = OrderDetails(connection_data)
        result = c.update(orderdetails)
        return jsonify({
            'message': result[0]
        }), result[1]

        #----------------------------------------------------------------

@app.route('/suppliers', methods=['POST'])
def add_suppliers():
    data = request.json
    suppliers = SuppliersEntity(supplier_name=data['supplier_name'],
                                contact_name=data['contact_name'],
                                address=data['address'],
                                city=data['city'],
                                postal_code=data['postal_code'],
                                country=data['country'],
                                phone=data['phone'])
    c = Suppliers(connection_data)
    message = c.insert(suppliers)
    if message is None:
        return jsonify({
            'message': 'Cannot insert data'
        }), 500
    return jsonify({
        'message': message
    })

@app.route('/suppliers/all')
def get_all_suppliers():
    c = Suppliers(connection_data)
    result = c.get_all()
    return jsonify({
        'data': result
    })

@app.route('/suppliers/<int:id>', methods=['DELETE', 'PUT'])
def delete_suppliers_by_id(id):
    if request.method == 'DELETE':
        # Delete user by id
        suppliers = SuppliersEntity(supplier_id=id)
        c = Suppliers(connection_data)
        result = c.delete(suppliers)
        return jsonify({
            'message': result[0]
        }), result[1]
    else:
        # Update user by id
        data = request.json
        suppliers = SuppliersEntity(supplier_id=id,
                                    supplier_name=data['supplier_name'],
                                    contact_name=data['contact_name'],
                                    address=data['address'],
                                    city=data['city'],
                                    postal_code=data['postal_code'],
                                    country=data['country'],
                                    phone=data['phone'])
        c = Suppliers(connection_data)
        result = c.update(suppliers)
        return jsonify({
            'message': result[0]
        }), result[1]

        #-------------------------------------------------

@app.route('/shippers', methods=['POST'])
def add_shippers():
    data = request.json
    shippers = ShippersEntity(shipper_name=data['shipper_name'],
                                phone=data['phone']
                                )
    c = Shippers(connection_data)
    message = c.insert(shippers)
    if message is None:
        return jsonify({
            'message': 'Cannot insert data'
        }), 500
    return jsonify({
        'message': message
    })

@app.route('/shippers/all')
def get_all_shippers():
    c = Shippers(connection_data)
    result = c.get_all()
    return jsonify({
        'data': result
    })

@app.route('/shippers/<int:id>', methods=['DELETE', 'PUT'])
def delete_shippers_by_id(id):
    if request.method == 'DELETE':
        # Delete user by id
        shippers = ShippersEntity(shipper_id=id)
        c = Shippers(connection_data)
        result = c.delete(shippers)
        return jsonify({
            'message': result[0]
        }), result[1]
    else:
          # Update user by id
        data = request.json
        shippers = ShippersEntity(shipper_id=id,
                                    shipper_name=data['shipper_name'],
                                phone=data['phone'])
        c = Shippers(connection_data)
        result = c.update(shippers)
        return jsonify({
            'message': result[0]
        }), result[1]

#=============================================================================


@app.route('/orders', methods=['POST'])
def add_orders():
    data = request.json
    orders = OrdersEntity(customer_id =data['customer_id'],
                                employee_id=data['employee_id'],
                                orderdate=data['orderdate'],
                                shipper_id=data['shipper_id']                            
                                )
    c = Orders(connection_data)
    message = c.insert(orders)
    if message is None:
        return jsonify({
            'message': 'Cannot insert data'
        }), 500
    return jsonify({
        'message': message
    })

@app.route('/orders/all')
def get_all_orders():
    c = Orders(connection_data)
    result = c.get_all()
    return jsonify({
        'data': result
    })

@app.route('/orders/<int:id>', methods=['DELETE', 'PUT'])
def delete_orders_by_id(id):
    if request.method == 'DELETE':
        # Delete user by id
        orders = OrdersEntity(order_id=id)
        c = Orders(connection_data)
        result = c.delete(orders)
        return jsonify({
            'message': result[0]
        }), result[1]
    else:
        # Update user by id
        data = request.json
        orders= OrdersEntity(order_id=id,
                                customer_id =data['customer_id'],
                                employee_id=data['employee_id'],
                                orderdate=data['orderdate'],
                                shipper_id=data['shipper_id'] )
        c = Orders(connection_data)
        result = c.update(orders)
        return jsonify({
            'message': result[0]
        }), result[1]
        


#=============================================================================



@app.route('/products', methods=['POST'])
def add_products():
    data = request.json
    products = ProductsEntity(product_name =data['product_name'],
                                supplier_id=data['supplier_id'],
                                category_id=data['category_id'],
                                unit=data['unit'],                             
                                price=data['price'])
    c = Products(connection_data)
    message = c.insert(products)
    if message is None:
        return jsonify({
            'message': 'Cannot insert data'
        }), 500
    return jsonify({
        'message': message
    })



@app.route('/products/all')
def get_all_products():
    c = Products(connection_data)
    result = c.get_all()
    return jsonify({
        'data': result
    })

@app.route('/products/<int:id>', methods=['DELETE', 'PUT'])
def delete_products_by_id(id):
    if request.method == 'DELETE':
        # Delete user by id
        products = ProductsEntity(product_id=id)
        c = Products(connection_data)
        result = c.delete(products)
        return jsonify({
            'message': result[0]
        }), result[1]
    else:
        data = request.json
        products = ProductsEntity(product_id=id,
                                    product_name =data['product_name'],
                                    supplier_id=data['supplier_id'],
                                    category_id=data['category_id'],
                                    unit=data['unit'],                             
                                    price=data['price'])
        c = Products(connection_data)
        result = c.update(products)
        return jsonify({
            'message': result[0]
        }), result[1]
