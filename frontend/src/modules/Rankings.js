import React from "react";
import { Tab, Row, Col, Nav, ListGroup, Container } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faImdb, faGoodreads } from "@fortawesome/free-brands-svg-icons";
import { faStar } from "@fortawesome/free-solid-svg-icons";
import books from "../api/books.json";
import movies from "../api/movies.json";
import tvseries from "../api/tvseries.json";
import watched from "../api/watched.json";

import "./Rankings.css";

class Ranking extends React.Component {
  renderItem(index, value, item_type) {
    return (
      <ListGroup.Item
        key={index}
        className="d-flex justify-content-between align-items-center"
        action
        href={value.fields.reference}
      >
        {index + 1}. {value.fields.name}
        <span className="badge badge-secondary">
          <i className="fa-2x">
            <span className="fa-layers fa-fw">
              <FontAwesomeIcon icon={faStar} />
              <span className="fa-layers-text star">
                {value.fields.site_rating.toFixed(1)}
              </span>
            </span>
          </i>
          {item_type === "Books" ? (
            <FontAwesomeIcon size="2x" icon={faGoodreads} />
          ) : (
            <FontAwesomeIcon size="2x" icon={faImdb} />
          )}
        </span>
      </ListGroup.Item>
    );
  }

  render() {
    return (
      <ListGroup>
        {this.props.content.map((item, i) => {
          return this.renderItem(i, item, this.props.title);
        })}
      </ListGroup>
    );
  }
}

class Rankings extends React.Component {
  renderPill(keyname, name, count) {
    return (
      <Nav.Item>
        <Nav.Link eventKey={keyname}>
          <strong className="text-secondary">{name}</strong>
          <span className="badge badge-secondary badge-pill float-right">
            {count}
          </span>
        </Nav.Link>
      </Nav.Item>
    );
  }

  render() {
    return (
      <div className="Rankings">
        <Tab.Container defaultActiveKey="first">
          <Row>
            <Col sm={3}>
              <Nav variant="pills" className="flex-column">
                {this.renderPill("first", "Movies", watched.count_movies)}
                {this.renderPill("second", "TV Shows", watched.count_tvseries)}
                {this.renderPill("third", "Books", watched.count_books)}
              </Nav>
            </Col>
            <Col sm={9}>
              <Tab.Content>
                <Tab.Pane eventKey="first">
                  <Ranking title="Movies" content={movies} />
                </Tab.Pane>
                <Tab.Pane eventKey="second">
                  <Ranking title="TV Shows" content={tvseries} />
                </Tab.Pane>
                <Tab.Pane eventKey="third">
                  <Ranking title="Books" content={books} />
                </Tab.Pane>
              </Tab.Content>
            </Col>
          </Row>
        </Tab.Container>
        <Container className="text-right">
          Last updated: <small>{watched.last_update}</small>
        </Container>
      </div>
    );
  }
}

export default Rankings;
