# How to run

1. Stop and remove old container: ```docker stop flask-backend && docker rm flask-backend```
1. Build image: ```docker build -t backend .```
1. Run the container: ```docker run -d --name flask-backend -e password=postgres -p 5000:5000 backend```

# Entity
## Customer
* id: int
* customer_name: string
* contact_name: string
* address: string
* city: string
* postal_code: string
* country: string
## Categories
* id: int
* category_name: string
* description: string
## Employees
* id: int
* last_name: string
* first_name: string
* birth_date: date
* photo: string
* notes: string
## OrderDetails
* id: int
* order_id: int
* product_id: int
* quantity: int
## Orders
* id: int
* customer_id: int
* employee_id: int
* order_date: date
* shipper_id: int
## Products
* id: int
* product_name: string
* supplier_id : int
* category_id: int
* unit: string
* price : int
## Shippers
* id: int
* shipper_name: string
* phone : int
## Suppliers
* id: int
* supplier_name: string
* contact_name: string
* address: string
* city: string
* postal_code: string
* country: string
* phone :string




# API
## Customer
### Get all customer
* Request
    * Method: GET
    * Endpoint: /customer/all
    * Params: None
    * Body: None
* Response: [Customer]
### Add a customer
* Request
    * Method: POST
    * Endpoint: /customer
    * Body:
        * customer_name: string
        * contact_name: string
        * address: string
        * city: string
        * postal_code: string
        * country: string
* Response: Message
### Update a customer
* Request:
    * Method: PUT
    * Endpoint: /customer/:customer_id
    * Body:
        * customer_name: string
        * contact_name: string
        * address: string
        * city: string
        * postal_code: string
        * country: string
* Response: Message

### Delete a customer
* Request:
    * Method: DELETE
    * Endpoint: /customer/:customer_id
* Response: message
## Categories
### Get all Categories
* Request
    * Method: GET
    * Endpoint: /categories/all
    * Params: None
    * Body: None
* Response: [Categories]
### Add a categories
* Request
    * Method: POST
    * Endpoint: /categories
    * Body:
        * category_name: string
        * description: string
* Response: Message
### Update a categories
* Request:
    * Method: PUT
    * Endpoint: /customer/:category_id
    * Body:
        * category_name: string
        * description: string
* Response: Message

### Delete a categories
* Request:
    * Method: DELETE
    * Endpoint: /customer/:category_id
* Response: message
## Employees
### Get all employees
* Request
    * Method: GET
    * Endpoint: /employees/all
    * Params: None
    * Body: None
* Response: [Employees]
### Add a employees
* Request
    * Method: POST
    * Endpoint: /employees
    * Body:
        * last_name: string
        * first_name: string
        * birth_date: date
        * photo: string
        * notes: string
* Response: Message
### Update a employees
* Request:
    * Method: PUT
    * Endpoint: /customer/:employees_id
    * Body:
       * last_name: string
        * first_name: string
        * birth_date: date
        * photo: string
        * notes: string
* Response: Message

### Delete a employees
* Request:
    * Method: DELETE
    * Endpoint: /customer/:employees_id
* Response: message

.....
