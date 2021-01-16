CREATE TABLE TblCustomers (
    CustomerID SERIAL PRIMARY KEY,
    CustomerName varchar(255),
    ContactName varchar(255),
    Address varchar(255),
    City varchar(255),
    PostalCode varchar(255),
    Country varchar(255)
);
CREATE TABLE TblCategories (
     CategoryID SERIAL PRIMARY KEY,
    CategoryName varchar(255),
    Description varchar(255)

);
CREATE TABLE TblEmployees (
    EmployeeID SERIAL PRIMARY KEY,
    LastName varchar(255),
    FirstName varchar(255),
    BirthDate Date,
    Photo varchar(255),
    Notes varchar(255)
);
CREATE TABLE TblOrderDetails (
    OrderDetailID SERIAL PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT
   
);
CREATE TABLE TblSuppliers (
    SupplierID SERIAL PRIMARY KEY,
    SupplierName varchar(255),
    ContactName varchar(255),
    Address varchar(255),
    City varchar(255),
    PostalCode varchar(255),
    Country varchar(255),
    Phone INT

);
CREATE TABLE TblOrders (
    OrderID SERIAL PRIMARY KEY,
    CustomerID varchar(255),
    EmployeeID varchar(255),
    OrderDate DATE,
    ShipperID varchar(255) 
);


CREATE TABLE TblProducts(
    ProductID SERIAL PRIMARY KEY,
    ProductName varchar(255),
    SupplierID varchar(255),
    CategoryID varchar(255),
    Unit varchar(255),
    Price varchar(255)
);


CREATE TABLE TblShippers (
    ShipperID SERIAL PRIMARY KEY,
    ShipperName varchar(255),
    Phone varchar(255)
)



