import CRUD from "services/crud";
import React from "react";
import TableContent from "./tableContent";
import FormInput from "suppliers/home/formInput";
import { Container, Row, Col } from "reactstrap";

function HomeSuppliers() {
  // Dùng duy nhất cho React Hooks FUNCTION COMPONENT. KHÔNG ĐƯỢC DÙNG REACT CLASS COMPONENT
  const [listSuppliers, setListSuppliers] = React.useState([]); //Create listSuppliers State
  const [checkUpdate, setCheckUpdate] = React.useState(false);

  // Nếu giá trị state cũ là A, sau khi mình update thành B => render lại, A set thành A => không render lại

  const RetrieveAllSuppliers = () => {
    // <=> function RetrieveAllSuppliers(){}
    console.log("Retrieve all suppliers");
    CRUD.getAllSuppliers().then((res) => {
      //console.log(res);
      setListSuppliers(res.data.data); //Set list Suppliers after get all result from server
      setCheckUpdate(false);
    });
  };

  const onUpdateSuccess = (status) => {
    setCheckUpdate(status);
  };

  // useEffect: 1 dạng reactr hooks
  React.useEffect(() => {
    RetrieveAllSuppliers(); //Retrieve data when component rendered
  }, [checkUpdate]); //Dependencies, checkUpdate thay đổi => chạy lại useEffect

  return (
    // Short hand React.Fragment
    <Container fluid={true}>
      <h2 className="text-center">Suppliers</h2>
      <Row>
        <Col xs="8">
          <TableContent
            items={listSuppliers}
            onDeleteSuccess={onUpdateSuccess}
          />
        </Col>
        <Col xs="4">
          <h3 className="text-center">Create Suppliers</h3>
          <FormInput onSubmitSuccess={onUpdateSuccess} type="create" />
        </Col>
      </Row>
    </Container>
  );
}
export default HomeSuppliers;
