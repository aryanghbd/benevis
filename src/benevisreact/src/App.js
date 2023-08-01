import React, { useState } from 'react';
import { Button, Form, Container, Row, Col } from 'react-bootstrap';
import axios from 'axios';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { solarizedlight } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { Link } from 'react-router-dom';

function App() {
  const [code, setCode] = useState('');
  const [result, setResult] = useState('');

  const handleChange = event => {
    setCode(event.target.value);
  };

  const handleSubmit = event => {
    event.preventDefault();
    axios.post('http://localhost:5000/interpret', { code })
      .then(response => setResult(response.data))
      .catch(err => console.error(err));
  };

  return (

    <Container className="mt-5">

      <Row>
        <Col md={{ span: 6, offset: 3 }}>
          <Form onSubmit={handleSubmit}>
            <Form.Group>
              <Form.Label><h3>Enter your Benevis code</h3></Form.Label>
              <Form.Control as="textarea" rows="10" value={code} onChange={handleChange} />
            </Form.Group>
            <Button variant="primary" type="submit">
              Run
            </Button>
          </Form>

          {result && (
            <div className="mt-5">
              <h3>Output</h3>
                <SyntaxHighlighter className="codeBox" language="javascript" style={solarizedlight}>
                  {result}
                </SyntaxHighlighter>
            </div>
          )}
        </Col>
      </Row>

      <Row className="mt-5">
        <Col>
          <h3>Syntax Guide</h3>
            <p>
              The following list gives an overview of Benevis syntax with its equivalents in Pinglish and Farsi:
            </p>
            <ul>
              <li><strong>chiye(expression)</strong>: Print a value to the console. Equivalent to "print" in many languages. (بیا دیدن، چیه)</li>
              <li><strong>agar(expression) statement</strong>: "If" conditional. (اگه)</li>
              <li><strong>dar gheyre in soorat statement</strong>: "Else" conditional. (در غیر این صورت)</li>
              <li><strong>ta(expression) statement</strong>: While loop. (تا)</li>
              <li><strong>be alaveye, be alaveye la, be alaveye fa</strong>: Plus operator (+). (به علاوه)</li>
              <li><strong>menhaye, menhaye la, menhaye fa</strong>: Minus operator (-). (منهای)</li>
              <li><strong>zarbdar, zarbdar la, zarbdar fa</strong>: Multiply operator (*). (ضربدر)</li>
              <li><strong>taghsim bar, taghsim bar la, taghsim bar fa</strong>: Division operator (/). (تقسیم بر)</li>
              <li><strong>mosaviye, mosaviye la, mosaviye fa</strong>: Equal operator (==). (مساوی)</li>
              <li><strong>mosavi nist ba</strong>: Not equal operator (!=). (مساوی نیست با)</li>
            </ul>

        </Col>
      </Row>

      <Row className="mt-5">
        <Col>
          <h3>About Me</h3>
          <p> I am Aryan Ghobadi, a Computer Engineering (ECE) graduate from Imperial College London. I am passionate about delivering software with performance and meaning. You can check out my other projects on <a href="https://github.com/aryanghbd">GitHub</a> or connect with me on <a href="https://www.linkedin.com/in/aryan-ghobadi/">LinkedIn</a>.</p>
        </Col>
      </Row>
    </Container>
  );
}

export default App;
