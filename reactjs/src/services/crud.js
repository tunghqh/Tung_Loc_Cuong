import HttpRequest from "./http-common";

const getAll = async () => {
  return await HttpRequest.get("http://172.27.118.17:5000/customers/all");
};

const create = (data) => {
  return HttpRequest.post("http://localhost:5000/customers", data);
};

const deleteOne = (id) => {
  return HttpRequest.delete(`http://localhost:5000/customers/${id}`);
};

const updateOne = (id, data) => {
  return HttpRequest.put(`http://localhost:5000/customers/${id}`, data);
};



const getAllCategories = async () => {
  return await HttpRequest.get("http://127.0.0.1:5000/categories/all");
};

const createCategories = (data) => {
  return HttpRequest.post("http://localhost:5000/categories", data);
};

const deleteOneCategories = (id) => {
  return HttpRequest.delete(`http://localhost:5000/categories/${id}`);
};

const updateOneCategories= (id, data) => {
  return HttpRequest.put(`http://localhost:5000/categories/${id}`, data);
};



const getAllEmployees = async () => {
  return await HttpRequest.get("http://127.0.0.1:5000/employees/all");
};

const createEmployees = (data) => {
  return HttpRequest.post("http://localhost:5000/employees", data);
};

const deleteOneEmployees = (id) => {
  return HttpRequest.delete(`http://localhost:5000/employees/${id}`);
};

const updateOneEmployees= (id, data) => {
  return HttpRequest.put(`http://localhost:5000/employees/${id}`, data);
};


const getAllOrders = async () => {
  return await HttpRequest.get("http://127.0.0.1:5000/orders/all");
};

const createOrders = (data) => {
  return HttpRequest.post("http://localhost:5000/orders", data);
};

const deleteOneOrders = (id) => {
  return HttpRequest.delete(`http://localhost:5000/orders/${id}`);
};

const updateOneOrders= (id, data) => {
  return HttpRequest.put(`http://localhost:5000/orders/${id}`, data);
};




const getAllProducts = async () => {
  return await HttpRequest.get("http://127.0.0.1:5000/products/all");
};

const createProducts= (data) => {
  return HttpRequest.post("http://localhost:5000/products", data);
};

const deleteOneProducts = (id) => {
  return HttpRequest.delete(`http://localhost:5000/products/${id}`);
};

const updateOneProducts= (id, data) => {
  return HttpRequest.put(`http://localhost:5000/products/${id}`, data);
};




const getAllShippers = async () => {
  return await HttpRequest.get("http://127.0.0.1:5000/shippers/all");
};

const createShippers = (data) => {
  return HttpRequest.post("http://localhost:5000/shippers", data);
};

const deleteOneShippers = (id) => {
  return HttpRequest.delete(`http://localhost:5000/shippers/${id}`);
};

const updateOneShippers = (id, data) => {
  return HttpRequest.put(`http://localhost:5000/shippers/${id}`, data);
};



const getAllOrderDetails = async () => {
  return await HttpRequest.get("http://127.0.0.1:5000/orderdetails/all");
};

const createOrderDetails = (data) => {
  return HttpRequest.post("http://localhost:5000/orderdetails", data);
};

const deleteOneOrderDetails = (id) => {
  return HttpRequest.delete(`http://localhost:5000/orderdetails/${id}`);
};

const updateOneOrderDetails= (id, data) => {
  return HttpRequest.put(`http://localhost:5000/orderdetails/${id}`, data);
};




const getAllSuppliers = async () => {
  return await HttpRequest.get("http://127.0.0.1:5000/suppliers/all");
};

const createSuppliers = (data) => {
  return HttpRequest.post("http://localhost:5000/suppliers", data);
};

const deleteOneSuppliers = (id) => {
  return HttpRequest.delete(`http://localhost:5000/suppliers/${id}`);
};

const updateOneSuppliers= (id, data) => {
  return HttpRequest.put(`http://localhost:5000/suppliers/${id}`, data);
};







export default { getAll, create, deleteOne, updateOne,
                 getAllShippers, createShippers, deleteOneShippers, updateOneShippers,
                 getAllOrderDetails, createOrderDetails, deleteOneOrderDetails, updateOneOrderDetails,
                 getAllCategories, createCategories, deleteOneCategories, updateOneCategories,
                 getAllSuppliers, createSuppliers, deleteOneSuppliers, updateOneSuppliers,
                 getAllEmployees, createEmployees, deleteOneEmployees, updateOneEmployees,
                 getAllProducts, createProducts, deleteOneProducts, updateOneProducts,
                 getAllOrders, createOrders, deleteOneOrders, updateOneOrders
};
