import CRUD from "services/crud";
import React from "react";
import TableContent from "./tableContent";
import FormInput from "orderdetails/home/formInput";
import { Container, Row, Col } from "reactstrap";

function HomeOrderDetails() {
  // Dùng duy nhất cho React Hooks FUNCTION COMPONENT. KHÔNG ĐƯỢC DÙNG REACT CLASS COMPONENT
  const [listOrderDetails, setListOrderDetails] = React.useState([]); 
  const [checkUpdate, setCheckUpdate] = React.useState(false);

  // Nếu giá trị state cũ là A, sau khi mình update thành B => render lại, A set thành A => không render lại

  const RetrieveAllOrderDetails = () => {
    console.log("Retrieve all OrderDetails");
    CRUD.getAllOrderDetails().then((res) => {
      //console.log(res);
      setListOrderDetails(res.data.data); 
      setCheckUpdate(false);
    });
  };

  const onUpdateSuccess = (status) => {
    setCheckUpdate(status);
  };

  // useEffect: 1 dạng reactr hooks
  React.useEffect(() => {
    RetrieveAllOrderDetails(); //Retrieve data when component rendered
  }, [checkUpdate]); //Dependencies, checkUpdate thay đổi => chạy lại useEffect

  return (
    // Short hand React.Fragment
    <Container fluid={true}>
      <h2 className="text-center">OrderDetails</h2>
      <Row>
        <Col xs="8">
          <TableContent
            items={listOrderDetails}
            onDeleteSuccess={onUpdateSuccess}
          />
        </Col>
        <Col xs="4">
          <h3 className="text-center">Create OrderDetails</h3>
          <FormInput onSubmitSuccess={onUpdateSuccess} type="create" />
        </Col>
      </Row>
    </Container>
  );
}
export default HomeOrderDetails;
