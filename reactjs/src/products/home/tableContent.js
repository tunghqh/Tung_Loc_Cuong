import React from "react";
import CRUD from "services/crud";
import { useHistory } from "react-router-dom";
import { Table, Button } from "reactstrap";

function TableContent({ items, onDeleteSuccess }) {
  let history = useHistory();

  // === props.checkUpdateSuccess
  function handleOnDelete(id) {
    //Handle when click button Delete
    CRUD.deleteOneProducts(id).then((res) => {
      // Call CURD from services
      // check response message
      onDeleteSuccess(true);
    });
  }

  function handleOnEdit(item) {
    // Route sang UpdatePage
    history.push(`/products/update/${item.product_id}`, { updateItem: item });
  }

  return (
    <Table striped>
      <thead>
        <tr>
          <th>ID</th>
          <th>Product name</th>
          <th>Supplier ID</th>
          <th>Category ID</th>
          <th>Unit</th>
          <th>Price</th>
          <th>Delete</th>
          <th>Edit</th>
        </tr>
      </thead>
      <tbody>
        {items.map((
          item,
          index //Map responses list data to table row
        ) => (
          <tr>
            <td>{item.product_id}</td>
            <td>{item.product_name}</td>
            <td>{item.supplier_id}</td>
            <td>{item.category_id}</td>
            <td>{item.unit}</td>
            <td>{item.price }</td>
            <td>
              <Button
                color="danger"
                onClick={() => handleOnDelete(item.product_id)}
              >
                Delete
              </Button>
            </td>
            <td>
              <Button color="warning" onClick={() => handleOnEdit(item)}>
                Edit
              </Button>
            </td>
          </tr>
        ))}
      </tbody>
    </Table>
  );
}
export default TableContent;
