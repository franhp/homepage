import React from "react";
import { Tab, Row, Col, Nav, ListGroup } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faImdb } from "@fortawesome/free-brands-svg-icons";
import {
  faBook,
  faFilm,
  faStar,
  faTv,
} from "@fortawesome/free-solid-svg-icons";
import books from "../api/books.json";
import movies from "../api/movies.json";
import tvseries from "../api/tvseries.json";
import watched from "../api/watched.json";

class Ranking extends React.Component {
  renderItem(index, value, item_type) {
    const rating = value.fields.site_rating;

    return (
      <ListGroup.Item
        key={value.pk}
        className="ranking-item d-flex justify-content-between align-items-center"
        action
        href={value.fields.reference}
      >
        <span className="ranking-item-left">
          <span className="ranking-number">
            {String(index + 1).padStart(2, "0")}
          </span>
          <span className="ranking-title">{value.fields.name}</span>
        </span>
        <span className="ranking-item-meta">
          <span className="rating-badge">
            <FontAwesomeIcon icon={faStar} />
            {rating == null ? "—" : rating.toFixed(1)}
          </span>
          <FontAwesomeIcon
            className={`source-icon ${
              item_type === "Books" ? "source-icon--book" : "source-icon--imdb"
            }`}
            icon={item_type === "Books" ? faBook : faImdb}
            size="2x"
          />
        </span>
      </ListGroup.Item>
    );
  }

  render() {
    return (
      <ListGroup className="ranking-list">
        {this.props.content.map((item, i) => {
          return this.renderItem(i, item, this.props.title);
        })}
      </ListGroup>
    );
  }
}

class Rankings extends React.Component {
  renderPill(keyname, name, count, icon) {
    return (
      <Nav.Item>
        <Nav.Link
          eventKey={keyname}
          className="ranking-nav-link d-flex justify-content-between align-items-center"
        >
          <span className="ranking-nav-label">
            <FontAwesomeIcon icon={icon} />
            <strong>{name}</strong>
          </span>
          <span className="ranking-count">{count}</span>
        </Nav.Link>
      </Nav.Item>
    );
  }

  render() {
    return (
      <div className="Rankings">
        <Tab.Container defaultActiveKey="first">
          <Row className="g-4">
            <Col md={4} lg={3}>
              <Nav variant="pills" className="rankings-nav flex-md-column">
                {this.renderPill(
                  "first",
                  "Movies",
                  watched.count_movies,
                  faFilm
                )}
                {this.renderPill(
                  "second",
                  "TV Shows",
                  watched.count_tvseries,
                  faTv
                )}
                {this.renderPill("third", "Books", watched.count_books, faBook)}
              </Nav>
            </Col>
            <Col md={8} lg={9}>
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
        <footer className="rankings-updated">
          Last updated <time>{watched.last_update}</time>
        </footer>
      </div>
    );
  }
}

export default Rankings;
