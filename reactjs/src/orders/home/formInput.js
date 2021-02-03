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
    customer_id: "",
    employee_id: "",
    orderdate: "",
    shipper_id: "",
  });
 
  useEffect(() => {
    console.log("Update Item: " + JSON.stringify(updateItem));
    if (updateItem) {
      setPostData({
        customer_id: updateItem.customer_id,
        employee_id: updateItem.employee_id,
        orderdate: updateItem.orderdate,
        shipper_id: updateItem.shipper_id,
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
        ? CRUD.updateOneOrders(updateID, postData)
        : CRUD.createOrders(postData);

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
    console.log("Employees : " + JSON.stringify(postData));
  }

  function handleOnSubmit(e) {
    e.preventDefault(); // prevent reload page if submit
  }

  return (
    <Form onSubmit={handleOnSubmit}>
      <FormGroup>
        <Label for="Customer ID">Customer ID</Label>
        <Input
          type="text"
          name="customer_id"
          value={postData.customer_id}
          onChange={handleChangeData}
          placeholder="Customer ID"
        />
      </FormGroup>
      <FormGroup>
        <Label for="Employee ID">Employee ID</Label>
        <Input
          type="text"
          name="employee_id"
          value={postData.employee_id}
          onChange={handleChangeData}
          placeholder="Employee ID"
        />
      </FormGroup>
      <FormGroup>
        <Label for="Orderdate">Orderdate(vd : 2020-11-11)</Label>
        <Input
          type="text"
          name="orderdate"
          value={postData.orderdate}
          onChange={handleChangeData}
          placeholder="(vd : 2020-11-11)"
          id=""
        />
      </FormGroup>

      <FormGroup>
        <Label for="Shipper ID">Shipper ID</Label>
        <Input
          type="text"
          name="shipper_id"
          value={postData.shipper_id}
          onChange={handleChangeData}
          placeholder="Shipper ID"
          id=""
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
