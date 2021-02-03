import React from "react";
import { useParams, useLocation } from "react-router-dom";
import FormInput from "suppliers/home/formInput";
import { Container, Row, Col } from "reactstrap";

export default function UpdatePageSuppliers() {
  const { id } = useParams();
  const location = useLocation();

  return (
    <Container>
      <h3 className="text-center">Update Suppliers at ID: {id} </h3>
      <Row>
        <Col sm="12" md={{ size: 6, offset: 3 }}>
          <FormInput
            type="update"
            updateID={id}
            updateItem={location.state?.updateItem}
          />
        </Col>
      </Row>
    </Container>
  );
}
