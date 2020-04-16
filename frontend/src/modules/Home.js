import React from 'react';
import { Image, Row, Col, Container } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faLinkedin, faGoodreads, faLastfmSquare, faGithubSquare, faTwitterSquare, faDocker, faLinux, faPython, faJava, faAws, faHtml5, faCss3, faJenkins, faReact, faSass, faJs, faLess } from '@fortawesome/free-brands-svg-icons';
import { faHeadphones, faPlaneDeparture, faTerminal, faGamepad, faHeart, faFilm, faMapMarkerAlt, faBook, faMusic, faBriefcase } from '@fortawesome/free-solid-svg-icons';

import logo from '../images/logo.svg';


class Home extends React.Component {
    render() {
        return (
            <Container>
                <Row>
                    <Col sm={6} className="text-center">
                        <Image src={logo} width="350" thumbnail />
                    </Col>
                    <Col sm={6}>
                        <h2>Other</h2>
                        <FontAwesomeIcon icon={faMapMarkerAlt} />
                        <FontAwesomeIcon icon={faBriefcase} />
                        <h2>Profiles</h2>
                        <FontAwesomeIcon icon={faLastfmSquare} />
                        <FontAwesomeIcon icon={faGoodreads} />
                        <FontAwesomeIcon icon={faLinkedin} />
                        <FontAwesomeIcon icon={faGithubSquare} />
                        <FontAwesomeIcon icon={faTwitterSquare} />

                        <h2>Hobbies</h2><FontAwesomeIcon icon={faHeart} />
                        <FontAwesomeIcon icon={faHeadphones} />
                        <FontAwesomeIcon icon={faMusic} />
                        <FontAwesomeIcon icon={faBook} />
                        <FontAwesomeIcon icon={faPlaneDeparture} />
                        <FontAwesomeIcon icon={faGamepad} />
                        <FontAwesomeIcon icon={faFilm} />

                        <h2>Technologies</h2>
                        <FontAwesomeIcon icon={faDocker} />
                        <FontAwesomeIcon icon={faLinux} />
                        <FontAwesomeIcon icon={faTerminal} />
                        <FontAwesomeIcon icon={faPython} />
                        <FontAwesomeIcon icon={faJenkins} />
                        <FontAwesomeIcon icon={faJava} />
                        <FontAwesomeIcon icon={faJs} />
                        <FontAwesomeIcon icon={faAws} />
                        <FontAwesomeIcon icon={faReact} />
                        <FontAwesomeIcon icon={faHtml5} />
                        <FontAwesomeIcon icon={faCss3} />
                        <FontAwesomeIcon icon={faSass} />
                        <FontAwesomeIcon icon={faLess} />

                    </Col>
                </Row>
            </Container>

        );
    }
}

export default Home;