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
    shipper_name: "",
    phone: "",
  });

  useEffect(() => {
    console.log("Update Item: " + JSON.stringify(updateItem));
    if (updateItem) {
      setPostData({
        shipper_name: updateItem.shipper_name,
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
        ? CRUD.updateOneShippers(updateID, postData)
        : CRUD.createShippers(postData);

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
        <Label for="shipperName">Shipper Name</Label>
        <Input
          type="text"
          name="shipper_name"
          value={postData.shipper_name}
          onChange={handleChangeData}
          placeholder="Shipper Name"
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
