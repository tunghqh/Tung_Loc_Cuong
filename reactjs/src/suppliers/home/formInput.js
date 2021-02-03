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
    supplier_name: "",
    contact_name: "",
    address: "",
    city: "",
    postal_code: "",
    country: "",
    phone: "",
  });
 
  useEffect(() => {
    console.log("Update Item: " + JSON.stringify(updateItem));
    if (updateItem) {
      setPostData({
        supplier_name: updateItem.supplier_name,
        contact_name: updateItem.contact_name,
        address: updateItem.address,
        city: updateItem.city,
        postal_code: updateItem.postal_code,
        country: updateItem.country,
        phone: updateItem.phone,
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
        ? CRUD.updateOneSuppliers(updateID, postData)
        : CRUD.createSuppliers(postData);

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
    console.log("Supplier Name : " + JSON.stringify(postData));
  }

  function handleOnSubmit(e) {
    e.preventDefault(); // prevent reload page if submit
  }

  return (
    <Form onSubmit={handleOnSubmit}>
      <FormGroup>
        <Label for="Supplier Name">Supplier Name</Label>
        <Input
          type="text"
          name="supplier_name"
          value={postData.supplier_name}
          onChange={handleChangeData}
          placeholder="Supplier Name"
        />
      </FormGroup>
      <FormGroup>
        <Label for="contactName">Contact Name</Label>
        <Input
          type="text"
          name="contact_name"
          value={postData.contact_name}
          onChange={handleChangeData}
          placeholder="Contact Name"
        />
      </FormGroup>
      <FormGroup>
        <Label for="_address">Address</Label>
        <Input
          type="text"
          name="address"
          value={postData.address}
          onChange={handleChangeData}
          placeholder="Address"
          id=""
        />
      </FormGroup>

      <FormGroup>
        <Label for="city">City</Label>
        <Input
          type="text"
          name="city"
          value={postData.city}
          onChange={handleChangeData}
          placeholder="City"
          id=""
        />
      </FormGroup>

      <FormGroup>
        <Label for="postalCode">Postal Code</Label>
        <Input
          type="text"
          name="postal_code"
          value={postData.postal_code}
          onChange={handleChangeData}
          placeholder="Postal Code"
        />
      </FormGroup>

      <FormGroup>
        <Label for="Country">Country</Label>
        <Input
          type="text"
          name="country"
          value={postData.country}
          onChange={handleChangeData}
          placeholder="Country"
        />
      </FormGroup>

      <FormGroup>
        <Label for="Phone">Phone</Label>
        <Input
          type="text"
          name="phone"
          value={postData.phone}
          onChange={handleChangeData}
          placeholder="Phone"
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
