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
    order_id: "",
    product_id: "",
    quantity: "",
  });

  useEffect(() => {
    console.log("Update Item: " + JSON.stringify(updateItem));
    if (updateItem) {
      setPostData({
        order_id: updateItem.order_id,
        product_id: updateItem.product_id,
        quantity: updateItem.quantity,
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
        ? CRUD.updateOneOrderDetails(updateID, postData)
        : CRUD.createOrderDetails(postData);

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
    console.log("Shipper Name : " + JSON.stringify(postData));
  }

  function handleOnSubmit(e) {
    e.preventDefault(); // prevent reload page if submit
  }

  return (
    <Form onSubmit={handleOnSubmit}>
      <FormGroup>
        <Label for="Order ID">Order ID</Label>
        <Input
          type="text"
          name="order_id"
          value={postData.order_id}
          onChange={handleChangeData}
          placeholder="Order ID"
        />
      </FormGroup>
      <FormGroup>
        <Label for="Product ID">Product ID</Label>
        <Input
          type="text"
          name="product_id"
          value={postData.product_id}
          onChange={handleChangeData}
          placeholder="Product ID"
        />
      </FormGroup>    

      <FormGroup>
        <Label for="Quantity">Quantity</Label>
        <Input
          type="text"
          name="quantity"
          value={postData.quantity}
          onChange={handleChangeData}
          placeholder="Quantity"
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
