import React, { useState } from "react";
import axios from "axios";
import { Alert, Form, Button, Container, Row, Col } from "react-bootstrap";

function PinReset() {
  const [formData, setFormData] = useState({ phone: "", newPin: "", confirmNewPin: "" });
  const [message, setMessage] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage(null);
    setError(null);
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/pin-reset/", formData);
      setMessage(response.data.message);
    } catch (err) {
      setError("Error resetting PIN. Please try again.");
    }
  };

  return (
    <Container className="mt-5">
      <Row className="justify-content-md-center">
        <Col md={6}>
          <h2>Reset PIN</h2>
          {message && <Alert variant="success">{message}</Alert>}
          {error && <Alert variant="danger">{error}</Alert>}
          <Form onSubmit={handleSubmit}>
            <Form.Group className="mb-3">
              <Form.Label>Phone Number</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter phone number"
                value={formData.phone}
                onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
                required
              />
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label>New PIN</Form.Label>
              <Form.Control
                type="password"
                placeholder="Enter new PIN"
                value={formData.newPin}
                onChange={(e) => setFormData({ ...formData, newPin: e.target.value })}
                required
              />
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label>Confirm New PIN</Form.Label>
              <Form.Control
                type="password"
                placeholder="Confirm new PIN"
                value={formData.confirmNewPin}
                onChange={(e) => setFormData({ ...formData, confirmNewPin: e.target.value })}
                required
              />
            </Form.Group>
            <Button variant="primary" type="submit">
              Reset PIN
            </Button>
          </Form>
        </Col>
      </Row>
    </Container>
  );
}

export default PinReset;
