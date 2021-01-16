import psycopg2

from BusinessObject import Customer as CustomerEntity

from BusinessObject import Categories as CategoriesEntity

from BusinessObject import Employees as EmployeesEntity

from BusinessObject import OrderDetails as OrderDetailsEntity

from BusinessObject import Suppliers as SuppliersEntity

from BusinessObject import Orders as OrdersEntity             
from BusinessObject import Products as ProductsEntity         
from BusinessObject import Shippers as ShippersEntity

class Customer:

    def __init__(self, connection_data):
        self.connection_data = connection_data

    def insert(self, customer: CustomerEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """INSERT INTO TblCustomers(CustomerName, ContactName, Address, City, PostalCode, Country)
                VALUES(%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (customer.customer_name, customer.contact_name, customer.address, customer.city, customer.postal_code, customer.country))
        conn.commit()
        return 'Insert successfully'
    
    def get_all(self):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "SELECT * FROM TblCustomers"
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        result = []
        for row in rows:
            customer = CustomerEntity()
            customer.fetch_data(row)
            result.append(customer.to_json())
        return result

    def delete(self, customer: CustomerEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "DELETE FROM TblCustomers WHERE CustomerID = %s"
        cursor.execute(sql, (customer.customer_id, ))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Deleted successfully', 200
        return 'Id not found', 404

    def update(self, customer: CustomerEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """UPDATE TblCustomers SET
                    CustomerName=%s, ContactName=%s, Address=%s,
                    City=%s, PostalCode=%s, Country=%s WHERE CustomerID=%s"""
        cursor.execute(sql, (customer.customer_name, customer.contact_name, customer.address, customer.city, customer.postal_code, customer.country, customer.customer_id))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Updated successfully', 200
        return 'Id not found', 404

        #------------------------------------------------------------------
        
class Categories:

    def __init__(self, connection_data):
        self.connection_data = connection_data

    def insert(self, categories: CategoriesEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """INSERT INTO TblCategories(CategoryName, Description)
                VALUES(%s, %s)"""
        cursor.execute(sql, (categories.category_name, categories.description))
        conn.commit()
        return 'Insert successfully'
    
    def get_all(self):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "SELECT * FROM TblCategories" 
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        result = []
        for row in rows:
            categories = CategoriesEntity()
            categories.fetch_data(row)
            result.append(categories.to_json())
        return result

    def delete(self, categories: CategoriesEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "DELETE FROM TblCategories WHERE CategoryID = %s"
        cursor.execute(sql, (categories.category_id, ))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Deleted successfully', 200
        return 'Id not found', 404

    def update(self, categories: CategoriesEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """UPDATE TblCategories SET
                    CategoryName=%s, Description=%s WHERE CategoryID = %s""" 
        cursor.execute(sql, (categories.category_name, categories.description, categories.category_id))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Updated successfully', 200
        return 'Id not found', 404
#--------------------------------------------

class Employees:

    def __init__(self, connection_data):
        self.connection_data = connection_data

    def insert(self, employees: EmployeesEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """INSERT INTO TblEmployees(LastName, FirstName, BirthDate, Photo, Notes)
                VALUES(%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (employees.last_name, employees.first_name, employees.birth_date, employees.photo, employees.notes))
        conn.commit()
        return 'Insert successfully'
    
    def get_all(self):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "SELECT * FROM TblEmployees"
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        result = []
        for row in rows:
            employees = EmployeesEntity()
            employees.fetch_data(row)
            result.append(employees.to_json())
        return result

    def delete(self, employees: EmployeesEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "DELETE FROM TblEmployees WHERE EmployeeID = %s"
        cursor.execute(sql, (employees.employee_id, ))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Deleted successfully', 200
        return 'Id not found', 404

    def update(self, employees: EmployeesEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """UPDATE TblEmployees SET
                    LastName=%s, FirstName=%s, BirthDate=%s,
                    Photo=%s, Notes=%s WHERE EmployeeID=%s"""
        cursor.execute(sql, (employees.last_name, employees.first_name, employees.birth_date, employees.photo, employees.notes,employees.employee_id))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Updated successfully', 200
        return 'Id not found', 404

        #------------------------------------------------------------

class OrderDetails:

    def __init__(self, connection_data):
        self.connection_data = connection_data

    def insert(self, orderdetails: OrderDetailsEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """INSERT INTO TblOrderDetails(OrderID, ProductID, Quantity)
                VALUES(%s, %s, %s)"""
        cursor.execute(sql, (orderdetails.order_id, orderdetails.product_id, orderdetails.quantity))
        conn.commit()
        return 'Insert successfully'
    
    def get_all(self):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "SELECT * FROM TblOrderDetails"
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        result = []
        for row in rows:
            orderdetails = OrderDetailsEntity()
            orderdetails.fetch_data(row)
            result.append(orderdetails.to_json())
        return result

    def delete(self, orderdetails: OrderDetailsEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "DELETE FROM TblOrderDetails WHERE OrderDetailID = %s"
        cursor.execute(sql, (orderdetails.order_detail_id, ))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Deleted successfully', 200
        return 'Id not found', 404

    def update(self, orderdetails: OrderDetailsEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """UPDATE TblOrderDetails SET
                    OrderID=%s, ProductID=%s, Quantity=%s
                     WHERE OrderDetailID=%s"""
        cursor.execute(sql, (orderdetails.order_id, orderdetails.product_id, orderdetails.quantity, orderdetails.order_detail_id))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Updated successfully', 200
        return 'Id not found', 404
#------------------------------------------------------------------------------

class Suppliers:

    def __init__(self, connection_data):
        self.connection_data = connection_data

    def insert(self, suppliers: SuppliersEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """INSERT INTO TblSuppliers(SupplierName, ContactName, Address, City, PostalCode, Country,Phone)
                VALUES(%s, %s, %s, %s, %s, %s,%s)"""
        cursor.execute(sql, (suppliers.supplier_name, suppliers.contact_name, suppliers.address, suppliers.city, suppliers.postal_code, suppliers.country,suppliers.phone))
        conn.commit()
        return 'Insert successfully'
    
    def get_all(self):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "SELECT * FROM TblSuppliers"
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        result = []
        for row in rows:
            suppliers = SuppliersEntity()
            suppliers.fetch_data(row)
            result.append(suppliers.to_json())
        return result

    def delete(self, suppliers: SuppliersEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "DELETE FROM TblSuppliers WHERE SupplierID = %s"
        cursor.execute(sql, (suppliers.supplier_id, ))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Deleted successfully', 200
        return 'Id not found', 404

    def update(self, suppliers: SuppliersEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """UPDATE TblSuppliers SET
                    SupplierName=%s, ContactName=%s, Address=%s,
                    City=%s, PostalCode=%s, Country=%s ,Phone =%s WHERE SupplierID=%s"""
        cursor.execute(sql, (suppliers.supplier_name, suppliers.contact_name, suppliers.address, suppliers.city, suppliers.postal_code, suppliers.country,suppliers.phone, suppliers.supplier_id))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Updated successfully', 200
        return 'Id not found', 404

        #----------------------------------------------------
class Shippers:


    def __init__(self, connection_data):
        self.connection_data = connection_data

    def insert(self, shippers: ShippersEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """INSERT INTO TblShippers(ShipperName, Phone)
                VALUES(%s, %s)"""
        cursor.execute(sql, (shippers.shipper_name, shippers.phone))
        conn.commit()
        return 'Insert successfully'
    
    def get_all(self):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "SELECT * FROM TblShippers"
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        result = []
        for row in rows:
            shippers = ShippersEntity()
            shippers.fetch_data(row)
            result.append(shippers.to_json())
        return result

    def delete(self, shippers: ShippersEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "DELETE FROM TblShippers WHERE ShipperID = %s"
        cursor.execute(sql, (shippers.shipper_id, ))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Deleted successfully', 200
        return 'Id not found', 404

    def update(self, shippers: ShippersEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """UPDATE TblShippers SET
                    ShipperName=%s, Phone=%s WHERE ShipperID=%s
                    """
        cursor.execute(sql, (shippers.shipper_name, shippers.phone, shippers.shipper_id))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Updated successfully', 200
        return 'Id not found', 404
#===============================================================

class Orders:

    

    def __init__(self, connection_data):
        self.connection_data = connection_data

    def insert(self, orders: OrdersEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """INSERT INTO TblOrders(CustomerID, EmployeeID, OrderDate, ShipperID)
                VALUES(%s, %s, %s, %s)"""
        cursor.execute(sql, (orders.customer_id, orders.employee_id, orders.orderdate, orders.shipper_id))
        conn.commit()
        return 'Insert successfully'
    
    def get_all(self):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "SELECT * FROM TblOrders"
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        result = []
        for row in rows:
            orders = OrdersEntity()
            orders.fetch_data(row)
            result.append(orders.to_json())
        return result

    def delete(self, orders: OrdersEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "DELETE FROM TblOrders WHERE OrderID = %s"
        cursor.execute(sql, (orders.order_id, ))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Deleted successfully', 200
        return 'Id not found', 404

    def update(self, orders: OrdersEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """UPDATE TblOrders SET
                    CustomerID=%s, EmployeeID=%s, OrderDate=%s,
                    ShipperID=%s WHERE OrderID=%s"""
        cursor.execute(sql, (orders.customer_id, orders.employee_id, orders.orderdate, orders.shipper_id, orders.order_id))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Updated successfully', 200
        return 'Id not found', 404


#===============================================================

class Products:

    def __init__(self, connection_data):
        self.connection_data = connection_data

    def insert(self, products: ProductsEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """INSERT INTO TblProducts(ProductName, SupplierID, CategoryID, Unit, Price)
                VALUES(%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (products.product_name, products.supplier_id, products.category_id, products.unit, products.price))
        conn.commit()
        return 'Insert successfully'

    
    def get_all(self):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "SELECT * FROM TblProducts"
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        result = []
        for row in rows:
           products = ProductsEntity()
           products.fetch_data(row)
           result.append(products.to_json())
        return result

    def delete(self, products: ProductsEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "DELETE FROM TblProducts WHERE ProductID = %s"
        cursor.execute(sql, (products.product_id, ))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Deleted successfully', 200
        return 'Id not found', 404


    def update(self, products: ProductsEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """UPDATE TblProducts SET
                    ProductName=%s, SupplierID=%s, CategoryID=%s,
                    Unit=%s, Price=%s WHERE ProductID=%s"""
        cursor.execute(sql, (products.product_name, products.supplier_id, products.category_id, products.unit, products.price,products.product_id))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Updated successfully', 200
        return 'Id not found', 404
