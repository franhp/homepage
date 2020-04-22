import React from 'react';
import { Image, Row, Col, Container, ListGroup, Jumbotron } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faLinkedin, faGoodreads, faLastfmSquare, faGithubSquare, faTwitterSquare, faDocker, faLinux, faPython, faJava, faAws, faHtml5, faCss3, faJenkins, faReact, faSass, faJs } from '@fortawesome/free-brands-svg-icons';
import { faHeadphones, faPlaneDeparture, faGamepad, faHeart, faFilm, faMapMarkerAlt, faBook, faMusic, faBriefcase, faCoffee, faThumbsUp } from '@fortawesome/free-solid-svg-icons';

import profile from '../images/profile.png';

import './Home.css';

class Home extends React.Component {
    render() {
        return (
            <Jumbotron className="Home pt-2">
                <Row>
                    <Col sm={4} className="text-center">
                        <Image src={profile} thumbnail width={200} />
                    </Col>
                    <Col sm={8}>
                        <Container>
                            <h1>Fran Hermoso</h1>
                        </Container>
                        <Container className="ProfileLinks text-right mt-4">
                            <a href="https://uk.linkedin.com/in/franhp">
                                <FontAwesomeIcon icon={faLinkedin} size="4x" />
                            </a>
                            <a href="https://github.com/franhp">
                                <FontAwesomeIcon icon={faGithubSquare} size="4x" />
                            </a>
                            <a href="https://twitter.com/franhp">
                                <FontAwesomeIcon icon={faTwitterSquare} size="4x" />
                            </a>
                            <a href="http://lastfm.es/user/franhp">
                                <FontAwesomeIcon icon={faLastfmSquare} size="4x" />
                            </a>
                            <a href="https://www.goodreads.com/user/show/39044705-fran-hermoso">
                                <FontAwesomeIcon icon={faGoodreads} size="4x" />
                            </a>

                        </Container>
                    </Col>
                </Row>
                <Row>
                    <Col sm={12} className="m-2">
                        <ListGroup variant="flush" className="ProfileBox">

                            <ListGroup.Item>
                                <Row>
                                    <Col xs={2} sm={2} md={3} className="vertical-line text-center">
                                        <FontAwesomeIcon icon={faBriefcase} size="2x" />
                                    </Col>
                                    <Col xs={6} sm={8} md={7} className="text-center">
                                        DevOps, Developer, SysAdmin
                                    </Col>
                                </Row>
                            </ListGroup.Item>
                            <ListGroup.Item>
                                <Row>
                                    <Col xs={2} sm={2} md={3} className="vertical-line text-center">
                                        <FontAwesomeIcon icon={faMapMarkerAlt} size="2x" />
                                    </Col>
                                    <Col xs={6} sm={8} md={7} className="text-center">
                                        Manresa, Barcelona
                                    </Col>
                                </Row>
                            </ListGroup.Item>
                            <ListGroup.Item>
                                <Row>
                                    <Col xs={2} sm={2} md={3} className="vertical-line text-center">
                                        <FontAwesomeIcon icon={faHeart} size="2x" />
                                    </Col>
                                    <Col xs={6} sm={7} md={7} className="text-center">
                                        <FontAwesomeIcon icon={faHeadphones} size="2x" />
                                        <FontAwesomeIcon icon={faMusic} size="2x" />
                                        <FontAwesomeIcon icon={faBook} size="2x" />
                                        <FontAwesomeIcon icon={faPlaneDeparture} size="2x" />
                                        <FontAwesomeIcon icon={faGamepad} size="2x" />
                                        <FontAwesomeIcon icon={faFilm} size="2x" />
                                        <FontAwesomeIcon icon={faCoffee} size="2x" />
                                    </Col>
                                </Row>
                            </ListGroup.Item>
                            <ListGroup.Item>
                                <Row>
                                    <Col xs={2} sm={2} md={3} className="vertical-line text-center">
                                        <FontAwesomeIcon icon={faThumbsUp} size="2x" />
                                    </Col>
                                    <Col xs={6} sm={8} md={7} className="text-center">
                                        <Row>
                                            <Col sm={4}>
                                                Systems:<br />
                                                <FontAwesomeIcon icon={faDocker} size="2x" />
                                                <FontAwesomeIcon icon={faLinux} size="2x" />
                                                <FontAwesomeIcon icon={faJenkins} size="2x" />
                                                <FontAwesomeIcon icon={faAws} size="2x" />
                                            </Col>

                                            <Col sm={2}>
                                                Backend:<br />
                                                <FontAwesomeIcon icon={faPython} size="2x" />
                                                <FontAwesomeIcon icon={faJava} size="2x" />
                                            </Col>

                                            <Col sm={5}>
                                                Frontend:<br />
                                                <FontAwesomeIcon icon={faReact} size="2x" />
                                                <FontAwesomeIcon icon={faHtml5} size="2x" />
                                                <FontAwesomeIcon icon={faCss3} size="2x" />
                                                <FontAwesomeIcon icon={faSass} size="2x" />
                                                <FontAwesomeIcon icon={faJs} size="2x" />
                                            </Col>
                                        </Row>
                                    </Col>
                                </Row>
                            </ListGroup.Item>
                        </ListGroup>

                    </Col>
                </Row>
            </Jumbotron>


        );
    }
}

export default Home;