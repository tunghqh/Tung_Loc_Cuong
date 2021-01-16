class Customer:

    def __init__(self, customer_id=None, customer_name=None, contact_name=None, address=None, city=None, postal_code=None, country=None):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.contact_name = contact_name
        self.address = address
        self.city = city
        self.postal_code = postal_code
        self.country = country

    def fetch_data(self, row):
        self.customer_id = row[0]
        self.customer_name = row[1]
        self.contact_name = row[2]
        self.address = row[3]
        self.city = row[4]
        self.postal_code = row[5]
        self.country = row[6]

    def to_json(self):
        return {
            'customer_id': self.customer_id,
            'customer_name': self.customer_name,
            'contact_name': self.contact_name,
            'address': self.address,
            'postal_code': self.postal_code,
            'country': self.country,
            'city': self.city
        }
  

#--------------------------------------------------------

class Categories:



    def __init__(self, category_id=None, category_name=None, description=None):
        self.category_id = category_id
        self.category_name = category_name
        self.description = description
        
    def fetch_data(self, row):
        self.category_id = row[0]
        self.category_name = row[1]
        self.description = row[2]

    def to_json(self):
        return {
            'category_id': self.category_id,
            'category_name': self.category_name,
            'description': self.description
        }

        #------------------------------

class Employees:

    def __init__(self, employee_id=None, last_name=None, first_name=None, birth_date=None, photo=None, notes=None):
        self.employee_id = employee_id
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.photo = photo
        self.notes = notes

    def fetch_data(self, row):
        self.employee_id = row[0]
        self.last_name = row[1]
        self.first_name = row[2]
        self.birth_date = row[3]
        self.photo = row[4]
        self.notes = row[5]

    def to_json(self):
        return {
            'employee_id': self.employee_id,
            'last_name': self.last_name,
            'first_name': self.first_name,
            'birth_date': self.birth_date,
            'photo': self.photo,
            'notes': self.notes    
        }

        #------------------------------------------

class OrderDetails:

    def __init__(self, order_detail_id=None, order_id=None, product_id=None, quantity=None):
        self.order_detail_id = order_detail_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
       

    def fetch_data(self, row):
        self.order_detail_id = row[0]
        self.order_id = row[1]
        self.product_id = row[2]
        self.quantity = row[3]
    

    def to_json(self):
        return {
            'order_detail_id': self.order_detail_id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            
        }
 #---------------------------------------

class Suppliers:

    def __init__(self, supplier_id=None, supplier_name=None, contact_name=None, address=None, city=None, postal_code=None, country=None,phone =None):
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.contact_name = contact_name
        self.address = address
        self.city = city
        self.postal_code = postal_code
        self.country = country
        self.phone = phone

    def fetch_data(self, row):
        self.supplier_id = row[0]
        self.supplier_name = row[1]
        self.contact_name = row[2]
        self.address = row[3]
        self.city = row[4]
        self.postal_code = row[5]
        self.country = row[6]
        self.phone = row[7]

    def to_json(self):
        return {
            'supplier_id': self.customer_id,
            'supplier_name': self.customer_name,
            'contact_name': self.contact_name,
            'address': self.address,
            'postal_code': self.postal_code,
            'country': self.country,
            'city': self.city,
            'phone' : self.phone
        }

#---------------------------------------------

class Shippers:

    def __init__(self, shipper_id =None, shipper_name=None, phone=None):
        self.shipper_id = shipper_id 
        self.shipper_name = shipper_name
        self.phone = phone
       
    def fetch_data(self, row):
        self.shipper_id  = row[0]
        self.shipper_name = row[1]
        self.phone = row[2]
   

    def to_json(self):
        return {
            'shipper_id': self.shipper_id ,
            'shipper_name': self.shipper_name,
            'phone': self.phone
          
        }

#-----------------------------------------------

class Orders:

    def __init__(self,order_id=None, customer_id=None, employee_id=None, orderdate=None, shipper_id=None):
        self.order_id = order_id
        self.customer_id = customer_id
        self.employee_id= employee_id
        self.orderdate = orderdate
        self.shipper_id = shipper_id
        

    def fetch_data(self, row):
        self.order_id = row[0]
        self.customer_id = row[1]
        self.employee_id= row[2]
        self.orderdate = row[3]
        self.shipper_id = row[4]
   
      

    def to_json(self):
        return {
            'order_id': self.order_id,
            'customer_id': self.customer_id,
            'employee_id': self.employee_id,
            'orderdate': self.orderdate,
            'shipper_id': self.shipper_id
           
        }



#===================================================================


class Products:

 
    def __init__(self,product_id=None, product_name=None, supplier_id=None, category_id=None, unit=None,price =None):
        self.product_id = product_id
        self.product_name = product_name
        self.supplier_id  = supplier_id
        self.category_id = category_id
        self.unit = unit
        self.price = price 

    def fetch_data(self, row):
        self.product_id = row[0]
        self.product_name = row[1]
        self.supplier_id  = row[2]
        self.category_id = row[3]
        self.unit = row[4]
        self.price = row[5]
      
    def to_json(self):
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'supplier_id': self.supplier_id,
            'category_id': self.category_id,
            'unit': self.unit,
            'price': self.price
           
        }
