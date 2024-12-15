import React, { useEffect, useState } from "react";
import axios from "axios";
import { Container, Row, Col, Alert } from "react-bootstrap";

function Home() {
  const [message, setMessage] = useState(null);

  useEffect(() => {
    const fetchMessage = async () => {
      const token = localStorage.getItem("access");
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/home/", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        setMessage(response.data.message);
      } catch (err) {
        setMessage("Error fetching message.");
      }
    };
    fetchMessage();
  }, []);

  return (
    <Container className="mt-5">
      <Row className="justify-content-md-center">
        <Col md={6}>
          <h2>Welcome</h2>
          {message && <Alert variant="info">{message}</Alert>}
        </Col>
      </Row>
    </Container>
  );
}

export default Home;
