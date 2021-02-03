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
    lastname: "",
    firstname: "",
    birthdate: "",
    photo: "",
    notes: "",
  });
 
  useEffect(() => {
    console.log("Update Item: " + JSON.stringify(updateItem));
    if (updateItem) {
      setPostData({
        lastname: updateItem.lastname,
        firstname: updateItem.firstname,
        birthdate: updateItem.birthdate,
        photo: updateItem.photo,
        notes: updateItem.notes,
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
        ? CRUD.updateOneEmployees(updateID, postData)
        : CRUD.createEmployees(postData);

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
        <Label for="Lastname">Lastname</Label>
        <Input
          type="text"
          name="lastname"
          value={postData.lastname}
          onChange={handleChangeData}
          placeholder="Lastname"
        />
      </FormGroup>
      <FormGroup>
        <Label for="Firstname">Firstname</Label>
        <Input
          type="text"
          name="firstname"
          value={postData.firstname}
          onChange={handleChangeData}
          placeholder="Firstname"
        />
      </FormGroup>
      <FormGroup>
        <Label for="Birthdate">Birthdate(vd : 2020-11-11)</Label>
        <Input
          type="text"
          name="birthdate"
          value={postData.birthdate}
          onChange={handleChangeData}
          placeholder="(vd : 2020-11-11)"
          id=""
        />
      </FormGroup>

      <FormGroup>
        <Label for="Photo">Photo</Label>
        <Input
          type="text"
          name="photo"
          value={postData.photo}
          onChange={handleChangeData}
          placeholder="Photo"
          id=""
        />
      </FormGroup>

      <FormGroup>
        <Label for="Notes">Notes</Label>
        <Input
          type="text"
          name="notes"
          value={postData.notes}
          onChange={handleChangeData}
          placeholder="Notes"
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
