import React from "react";
import { Image, Row, Col, ListGroup, Container } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faLinkedin,
  faLastfmSquare,
  faGithubSquare,
  faDocker,
  faLinux,
  faPython,
  faJava,
  faAws,
  faHtml5,
  faCss3,
  faJenkins,
  faReact,
  faGitlab,
  faNodeJs,
  faJs,
  faPlaystation,
  faWizardsOfTheCoast,
  faUbuntu,
  faReddit,
  faImdb,
  faGolang,
  faBitcoin,
  faEthereum,
  faDebian,
  // faJs,
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
      <Container className="Home pt-2 mt-4 p-5 bg-primary rounded">
        <Row className="mb-4">
          <Col sm={4} className="text-center">
            <Image src={profile} thumbnail width={300} />
          </Col>
          <Col sm={8}>
            <Col sm={12}>
              <h1>Fran Hermoso</h1>
            </Col>
            <Col sm={{ span: 9 }} className="ProfileLinks text-right">
              I'm a GNU/Linux and Python enthusiast who is always willing to try
              new technologies. I am most often working as a DevOps but I also
              enjoy Developer oriented opportunities, specially backend.
              <hr />
              <a href="https://uk.linkedin.com/in/franhp">
                <FontAwesomeIcon icon={faLinkedin} size="4x" />
              </a>
              <a href="https://github.com/franhp">
                <FontAwesomeIcon icon={faGithubSquare} size="4x" />
              </a>
              <a href="http://lastfm.es/user/franhp">
                <FontAwesomeIcon icon={faLastfmSquare} size="4x" />
              </a>
            </Col>
          </Col>
        </Row>
        <Row>
          <Col sm={6}>
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
              <ListGroup.Item>
                <Row>
                  <Col xs={2} className="vertical-line text-center">
                    <FontAwesomeIcon icon={faThumbsUp} size="2x" />
                  </Col>
                  <Col xs={10} className="text-center">
                    <FontAwesomeIcon icon={faPlaystation} size="2x" />
                    <FontAwesomeIcon icon={faWizardsOfTheCoast} size="2x" />
                    <FontAwesomeIcon icon={faBitcoin} size="2x" />
                    <FontAwesomeIcon icon={faEthereum} size="2x" />
                    <FontAwesomeIcon icon={faReddit} size="2x" />
                    <FontAwesomeIcon icon={faImdb} size="2x" />
                  </Col>
                </Row>
              </ListGroup.Item>
            </ListGroup>
          </Col>
          <Col sm={6}>
            <ListGroup variant="flush" className="ProfileBox">
              <ListGroup.Item>
                <Row>
                  <Col xs={3} className="vertical-line text-center">
                    Backend
                  </Col>
                  <Col xs={9} className="text-center">
                    <FontAwesomeIcon icon={faPython} size="2x" />
                    <FontAwesomeIcon icon={faJava} size="2x" />
                    <FontAwesomeIcon icon={faGolang} size="2x" />
                    <FontAwesomeIcon icon={faNodeJs} size="2x" />
                  </Col>
                </Row>
              </ListGroup.Item>
              <ListGroup.Item>
                <Row>
                  <Col xs={3} className="vertical-line text-center">
                    Systems
                  </Col>
                  <Col xs={9} className="text-center">
                    <FontAwesomeIcon icon={faLinux} size="2x" />
                    <FontAwesomeIcon icon={faDebian} size="2x" />
                    <FontAwesomeIcon icon={faUbuntu} size="2x" />
                    <FontAwesomeIcon icon={faDocker} size="2x" />
                    <FontAwesomeIcon icon={faJenkins} size="2x" />
                    <FontAwesomeIcon icon={faAws} size="2x" />
                    <FontAwesomeIcon icon={faGitlab} size="2x" />
                  </Col>
                </Row>
              </ListGroup.Item>
              <ListGroup.Item>
                <Row>
                  <Col xs={3} className="vertical-line text-center">
                    Frontend
                  </Col>
                  <Col xs={9} className="text-center">
                    <FontAwesomeIcon icon={faReact} size="2x" />
                    <FontAwesomeIcon icon={faHtml5} size="2x" />
                    <FontAwesomeIcon icon={faCss3} size="2x" />
                    {/* <FontAwesomeIcon icon={faSass} size="2x" /> */}
                    <FontAwesomeIcon icon={faJs} size="2x" />
                  </Col>
                </Row>
              </ListGroup.Item>
            </ListGroup>
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;
