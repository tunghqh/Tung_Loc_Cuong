import CRUD from "services/crud";
import React from "react";
import TableContent from "./tableContent";
import FormInput from "products/home/formInput";
import { Container, Row, Col } from "reactstrap";

function HomeProducts() {
  // Dùng duy nhất cho React Hooks FUNCTION COMPONENT. KHÔNG ĐƯỢC DÙNG REACT CLASS COMPONENT
  const [listProducts, setListProducts] = React.useState([]); //Create listProducts State
  const [checkUpdate, setCheckUpdate] = React.useState(false);

  // Nếu giá trị state cũ là A, sau khi mình update thành B => render lại, A set thành A => không render lại

  const RetrieveAllProducts = () => {
    // <=> function RetrieveAllProducts(){}
    console.log("Retrieve all Products");
    CRUD.getAllProducts().then((res) => {
      //console.log(res);
      setListProducts(res.data.data); //Set list Products after get all result from server
      setCheckUpdate(false);
    });
  };

  const onUpdateSuccess = (status) => {
    setCheckUpdate(status);
  };

  // useEffect: 1 dạng reactr hooks
  React.useEffect(() => {
    RetrieveAllProducts(); //Retrieve data when component rendered
  }, [checkUpdate]); //Dependencies, checkUpdate thay đổi => chạy lại useEffect

  return (
    // Short hand React.Fragment
    <Container fluid={true}>
      <h2 className="text-center">Products</h2>
      <Row>
        <Col xs="8">
          <TableContent
            items={listProducts}
            onDeleteSuccess={onUpdateSuccess}
          />
        </Col>
        <Col xs="4">
          <h3 className="text-center">Create Products</h3>
          <FormInput onSubmitSuccess={onUpdateSuccess} type="create" />
        </Col>
      </Row>
    </Container>
  );
}
export default HomeProducts;
