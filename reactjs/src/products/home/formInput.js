import React, { useEffect } from "react";
import CRUD from "services/crud";
import { useHistory } from "react-router-dom";
import { Form, FormGroup, Button, Input, Label } from "reactstrap";

function FormInput({ onSubmitSuccess, type, updateID, updateItem }) {
  let history = useHistory(); 

  // onSubmitSuccess => onUpdateSuccess
  // Syntax js, defind {abc: "text", def: 12} => object (properties: abc, def)
  const [postData, setPostData] = React.useState({
    //Create postData state
    product_name: "",
    supplier_id: "",
    category_id: "",
    unit: "",
    price: "",
  });
 
  useEffect(() => {
    console.log("Update Item: " + JSON.stringify(updateItem));
    if (updateItem) {
      setPostData({
        product_name: updateItem.product_name,
        supplier_id: updateItem.supplier_id,
        category_id: updateItem.category_id,
        unit: updateItem.unit,
        price: updateItem.price,
      });
    }
  }, []);

  function handleChangeData(e) {
    setPostData({ ...postData, [e.target.name]: e.target.value }); //Only change customer name in postData
  }

  function handleOnClickSubmit(e) {
    // Handle event when click submit button
    console.log("POST DATA: " + JSON.stringify(postData));
    const crudType =
      type === "update"
        ? CRUD.updateOneProducts(updateID, postData)
        : CRUD.createProducts(postData);

    crudType
      .then((res) => {
        // set State check update success => true
        if (type === "create") {
          const check = res.data.message === "Insert successfully";

          onSubmitSuccess(check); // re-render if check is true
        } else if (type === "update") {
          if (res.data.message === "Updated successfully") history.goBack(); // Go back if update successfully
        }
      })
      .catch((err) => {
        alert(err || "Unknown Message"); // alert error messages
      });
    console.log("Products : " + JSON.stringify(postData));
  }

  function handleOnSubmit(e) {
    e.preventDefault(); // prevent reload page if submit
  }

  return (
    <Form onSubmit={handleOnSubmit}>
      <FormGroup>
        <Label for="Product name">Product name</Label>
        <Input
          type="text"
          name="product_name"
          value={postData.product_name}
          onChange={handleChangeData}
          placeholder="Product name"
        />
      </FormGroup>
      <FormGroup>
        <Label for="Supplier ID">Supplier ID</Label>
        <Input
          type="text"
          name="supplier_id"
          value={postData.supplier_id}
          onChange={handleChangeData}
          placeholder="Supplier ID"
        />
      </FormGroup>
      <FormGroup>
        <Label for="Category ID">Category ID</Label>
        <Input
          type="text"
          name="category_id"
          value={postData.category_id}
          onChange={handleChangeData}
          placeholder="Category ID"
          id=""
        />
      </FormGroup>

      <FormGroup>
        <Label for="Unit">Unit</Label>
        <Input
          type="text"
          name="unit"
          value={postData.unit}
          onChange={handleChangeData}
          placeholder="Unit"
          id=""
        />
      </FormGroup>

      <FormGroup>
        <Label for="Price">Price</Label>
        <Input
          type="text"
          name="price"
          value={postData.Price}
          onChange={handleChangeData}
          placeholder="price"
        />
      </FormGroup>

      <div className="text-center">
        <Button
          name="btnSubmit"
          value="Submit"
          onClick={handleOnClickSubmit}
          color="primary"
        >
          Submit{" "}
        </Button>
      </div>
    </Form>
  );
}
export default FormInput;
