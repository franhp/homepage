import React from 'react'
import { Tab, Row, Col, Nav, ListGroup, Container } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faImdb, faGoodreads } from '@fortawesome/free-brands-svg-icons'
import books from '../api/books.json';
import movies from '../api/movies.json';
import tvseries from '../api/tvseries.json'
import watched from '../api/watched.json';


class Ranking extends React.Component {
    renderItem(index, value, item_type) {
        return (
            <ListGroup.Item className="d-flex justify-content-between align-items-center" action href={value.fields.reference}>
                {index + 1}. {value.fields.name}
                <span className="badge badge-primary badge-pill">
                    {(item_type === "Books") ? <FontAwesomeIcon icon={faGoodreads} /> : <FontAwesomeIcon icon={faImdb} />}
                    &nbsp;{value.fields.site_rating.toFixed(1)}
                </span>
            </ListGroup.Item>
        );
    }

    render() {
        return (
            <ListGroup>
                {this.props.content.map((item, i) => { return this.renderItem(i, item, this.props.title) })}
            </ListGroup>
        );
    }
}

class Rankings extends React.Component {
    render() {
        return (
            <div className="Rankings">
                <Tab.Container defaultActiveKey="first">
                    <Row>
                        <Col sm={3}>
                            <Nav variant="pills" className="flex-column">
                                <Nav.Item>
                                    <Nav.Link eventKey="first">Movies <span>{watched.count_movies}</span></Nav.Link>
                                </Nav.Item>
                                <Nav.Item>
                                    <Nav.Link eventKey="second">TV Series <span>{watched.count_tvseries}</span></Nav.Link>
                                </Nav.Item>
                                <Nav.Item>
                                    <Nav.Link eventKey="third">Books <span>{watched.count_books}</span></Nav.Link>
                                </Nav.Item>
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
                    Last updated: {watched.last_update}
                </Container>
            </div>
        );
    }
}

export default Rankings;