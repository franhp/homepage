import React from "react";
import { Image, Row, Col, ListGroup, Jumbotron } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faLinkedin,
  faGoodreads,
  faLastfmSquare,
  faGithubSquare,
  faTwitterSquare,
  faDocker,
  faLinux,
  faPython,
  faJava,
  faAws,
  faHtml5,
  faCss3,
  faJenkins,
  faReact,
  faSass,
  faJs,
} from "@fortawesome/free-brands-svg-icons";
import {
  faPlaneDeparture,
  faGamepad,
  faHeart,
  faFilm,
  faMapMarkerAlt,
  faBook,
  faMusic,
  faCoffee,
  faThumbsUp,
} from "@fortawesome/free-solid-svg-icons";

import profile from "../images/profile.png";

class Home extends React.Component {
  render() {
    return (
      <Jumbotron className="Home pt-2">
        <Row>
          <Col sm={4} className="text-center">
            <Image src={profile} thumbnail width={300} />
          </Col>
          <Col sm={8}>
            <Col sm={12}>
              <h1>Fran Hermoso</h1>
            </Col>
            <Col sm={{ span: 9, offset: 3 }} className="text-right">
              I'm a GNU/Linux and Python enthusiast who is always willing to try
              new technologies. I am most often working as a DevOps but I also
              enjoy Developer oriented opportunities, specially backend.
            </Col>
          </Col>
        </Row>
        <Row>
          <Col sm={4} className="ProfileLinks text-center pt-2 pb-2">
            <a href="https://uk.linkedin.com/in/franhp">
              <FontAwesomeIcon icon={faLinkedin} size="4x" />
            </a>
            <a href="https://github.com/franhp">
              <FontAwesomeIcon icon={faGithubSquare} size="4x" />
            </a>
            <br className="d-none d-md-block" />
            <a href="https://twitter.com/franhp">
              <FontAwesomeIcon icon={faTwitterSquare} size="4x" />
            </a>
            <br className="d-block d-sm-none" />
            <a href="http://lastfm.es/user/franhp">
              <FontAwesomeIcon icon={faLastfmSquare} size="4x" />
            </a>
            <br className="d-none d-md-block" />
            <a href="https://www.goodreads.com/user/show/39044705-fran-hermoso">
              <FontAwesomeIcon icon={faGoodreads} size="4x" />
            </a>
          </Col>
          <Col sm={8}>
            <ListGroup variant="flush" className="ProfileBox">
              <ListGroup.Item>
                <Row>
                  <Col xs={2} className="vertical-line text-center">
                    <FontAwesomeIcon icon={faMapMarkerAlt} size="2x" />
                  </Col>
                  <Col xs={10} className="text-center">
                    Manresa (Barcelona)
                  </Col>
                </Row>
              </ListGroup.Item>
              <ListGroup.Item>
                <Row>
                  <Col xs={2} className="vertical-line text-center">
                    <FontAwesomeIcon icon={faThumbsUp} size="2x" />
                  </Col>
                  <Col xs={10} className="text-center">
                    <Row>
                      <Col xs={12} md={5}>
                        Systems:
                        <br />
                        <FontAwesomeIcon icon={faDocker} size="2x" />
                        <FontAwesomeIcon icon={faLinux} size="2x" />
                        <FontAwesomeIcon icon={faJenkins} size="2x" />
                        <FontAwesomeIcon icon={faAws} size="2x" />
                      </Col>

                      <Col xs={12} md={2}>
                        Backend:
                        <br />
                        <FontAwesomeIcon icon={faPython} size="2x" />
                        <FontAwesomeIcon icon={faJava} size="2x" />
                      </Col>

                      <Col xs={12} md={5}>
                        Frontend:
                        <br />
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
              <ListGroup.Item>
                <Row>
                  <Col xs={2} className="vertical-line text-center">
                    <FontAwesomeIcon icon={faHeart} size="2x" />
                  </Col>
                  <Col xs={10} className="text-center">
                    <FontAwesomeIcon icon={faMusic} size="2x" />
                    <FontAwesomeIcon icon={faBook} size="2x" />
                    <FontAwesomeIcon icon={faPlaneDeparture} size="2x" />
                    <FontAwesomeIcon icon={faGamepad} size="2x" />
                    <FontAwesomeIcon icon={faFilm} size="2x" />
                    <FontAwesomeIcon icon={faCoffee} size="2x" />
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
