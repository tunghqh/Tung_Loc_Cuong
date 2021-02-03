import "./App.css";
import React from "react";
import HomeCustomers from "./customers/home";
import UpdatePageCustomers from "./customers/update";

import HomeCategories from "./categories/home";
import UpdatePageCategories from "./categories/update";

import HomeEmployees from "./employees/home";
import UpdatePageEmployees from "./employees/update";

import HomeOrders from "./orders/home";
import UpdatePageOrders from "./orders/update";

import { BrowserRouter, Switch, Route ,Link } from "react-router-dom";

import HomeOrderDetails from "./orderdetails/home";
import UpdatePageOrderDetails from "./orderdetails/update";

import HomeProducts from "./products/home";
import UpdatePageProducts from "./products/update";

import HomeShippers from "./shippers/home";
import UpdatePageShippers from "./shippers/update";


import HomeSuppliers from "./suppliers/home";
import UpdatePageSuppliers from "./suppliers/update";

function App() {



  return (
    
    <BrowserRouter>

      <div id="menu">
                <ul>
                  <li><a href="App">HOME</a></li>
                  <li><a href="customers">Customers</a></li>
                  <li><a href="categories">Categories</a></li>
                  <li><a href="employees">Employee</a></li>
                  <li><a href="orders">Orders</a></li>
                  <li><a href="orderdetails">Orderdetails</a></li>
                  <li><a href="products">Products</a></li>
                  <li><a href="shippers">Shippers</a></li>
                  <li><a href="suppliers">Suppliers</a></li>

                </ul>
          </div>
        
      <Switch>

        <Route path="/customers" exact>
          <HomeCustomers />
        </Route>
        <Route path="/customers/update/:id">
          <UpdatePageCustomers />
        </Route>


        <Route path="/categories" exact>
          <HomeCategories />
        </Route>
        <Route path="/categories/update/:id">
          <UpdatePageCategories />
        </Route>

        <Route path="/employees" exact>
          <HomeEmployees />
        </Route>
        <Route path="/employees/update/:id">
          <UpdatePageEmployees />
        </Route>


        <Route path="/orders" exact>
          <HomeOrders />
        </Route>
        <Route path="/orders/update/:id">
          <UpdatePageOrders />
        </Route>


        <Route path="/orderdetails" exact>
          <HomeOrderDetails />
        </Route>
        <Route path="/orderdetails/update/:id">
          <UpdatePageOrderDetails />
        </Route>


        <Route path="/products" exact>
          <HomeProducts />
        </Route>
        <Route path="/products/update/:id">
          <UpdatePageProducts />
        </Route>


        <Route path="/shippers" exact>
          <HomeShippers />
        </Route>
        <Route path="/shippers/update/:id">
          <UpdatePageShippers />
        </Route>


        <Route path="/suppliers" exact>
          <HomeSuppliers />
        </Route>
        <Route path="/suppliers/update/:id">
          <UpdatePageSuppliers />
        </Route>


      </Switch>
    </BrowserRouter>
  );
}

export default App;
