import CRUD from "services/crud";
import React from "react";
import TableContent from "./tableContent";
import FormInput from "employees/home/formInput";
import { Container, Row, Col } from "reactstrap";

function HomeEmployees() {
  // Dùng duy nhất cho React Hooks FUNCTION COMPONENT. KHÔNG ĐƯỢC DÙNG REACT CLASS COMPONENT
  const [listEmployees, setListEmployees] = React.useState([]); //Create listEmployees State
  const [checkUpdate, setCheckUpdate] = React.useState(false);

  // Nếu giá trị state cũ là A, sau khi mình update thành B => render lại, A set thành A => không render lại

  const RetrieveAllEmployees = () => {
    // <=> function RetrieveAllEmployees(){}
    console.log("Retrieve all Employees");
    CRUD.getAllEmployees().then((res) => {
      //console.log(res);
      setListEmployees(res.data.data); //Set list Employees after get all result from server
      setCheckUpdate(false);
    });
  };

  const onUpdateSuccess = (status) => {
    setCheckUpdate(status);
  };

  // useEffect: 1 dạng reactr hooks
  React.useEffect(() => {
    RetrieveAllEmployees(); //Retrieve data when component rendered
  }, [checkUpdate]); //Dependencies, checkUpdate thay đổi => chạy lại useEffect

  return (
    // Short hand React.Fragment
    <Container fluid={true}>
      <h2 className="text-center">Employees</h2>
      <Row>
        <Col xs="8">
          <TableContent
            items={listEmployees}
            onDeleteSuccess={onUpdateSuccess}
          />
        </Col>
        <Col xs="4">
          <h3 className="text-center">Create Employees</h3>
          <FormInput onSubmitSuccess={onUpdateSuccess} type="create" />
        </Col>
      </Row>
    </Container>
  );
}
export default HomeEmployees;
