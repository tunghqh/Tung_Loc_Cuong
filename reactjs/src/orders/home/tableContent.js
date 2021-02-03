import React from "react";
import CRUD from "services/crud";
import { useHistory } from "react-router-dom";
import { Table, Button } from "reactstrap";

function TableContent({ items, onDeleteSuccess }) {
  let history = useHistory();

  // === props.checkUpdateSuccess
  function handleOnDelete(id) {
    //Handle when click button Delete
    CRUD.deleteOneOrders(id).then((res) => {
      // Call CURD from services
      // check response message
      onDeleteSuccess(true);
    });
  }

  function handleOnEdit(item) {
    // Route sang UpdatePage
    history.push(`/orders/update/${item.order_id}`, { updateItem: item });
  }

  return (
    <Table striped>
      <thead>
        <tr>
          <th>ID</th>
          <th>Customer ID</th>
          <th>Employee ID</th>
          <th>Orderdate</th>
          <th>Shipper ID</th>
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
            <td>{item.order_id}</td>
            <td>{item.customer_id}</td>
            <td>{item.employee_id}</td>
            <td>{item.orderdate}</td>
            <td>{item.shipper_id}</td>
            <td>
              <Button
                color="danger"
                onClick={() => handleOnDelete(item.order_id)}
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
