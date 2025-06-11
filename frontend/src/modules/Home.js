import React from "react";
import { Image, Row, Col, ListGroup, Container } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

// Brand icons
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
  faReddit,
  faImdb,
  faSteam,
  faGolang,
  faBitcoin,
  faEthereum,
  faDebian,
} from "@fortawesome/free-brands-svg-icons";

// Solid icons
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
  faTv,
} from "@fortawesome/free-solid-svg-icons";

// Assets
import profile from "../images/profile.jpg";

// Icon groups for better organization
const socialIcons = [
  {
    icon: faLinkedin,
    url: "https://uk.linkedin.com/in/franhp",
    label: "LinkedIn",
  },
  { icon: faGithubSquare, url: "https://github.com/franhp", label: "GitHub" },
  {
    icon: faLastfmSquare,
    url: "http://lastfm.es/user/franhp",
    label: "Last.fm",
  },
  { icon: faTv, url: "https://trakt.tv/users/franhp", label: "Trakt.tv" },
];

const interestIcons = [
  { icon: faMusic, label: "Music" },
  { icon: faBook, label: "Reading" },
  { icon: faPlaneDeparture, label: "Travel" },
  { icon: faGamepad, label: "Gaming" },
  { icon: faFilm, label: "Movies" },
  { icon: faCoffee, label: "Coffee" },
];

const likeIcons = [
  { icon: faPlaystation, label: "PlayStation" },
  { icon: faSteam, label: "Steam" },
  { icon: faBitcoin, label: "Bitcoin" },
  { icon: faEthereum, label: "Ethereum" },
  { icon: faReddit, label: "Reddit" },
  { icon: faImdb, label: "IMDB" },
];

const skillGroups = [
  {
    category: "Backend",
    icons: [
      { icon: faPython, label: "Python" },
      { icon: faJava, label: "Java" },
      { icon: faGolang, label: "Go" },
      { icon: faNodeJs, label: "Node.js" },
    ],
  },
  {
    category: "Systems",
    icons: [
      { icon: faLinux, label: "Linux" },
      { icon: faDebian, label: "Debian" },
      { icon: faDocker, label: "Docker" },
      { icon: faJenkins, label: "Jenkins" },
      { icon: faAws, label: "AWS" },
      { icon: faGitlab, label: "GitLab" },
    ],
  },
  {
    category: "Frontend",
    icons: [
      { icon: faReact, label: "React" },
      { icon: faHtml5, label: "HTML5" },
      { icon: faCss3, label: "CSS3" },
      { icon: faJs, label: "JavaScript" },
    ],
  },
];

const Home = () => {
  return (
    <Container className="Home pt-3 mt-5 p-5 rounded shadow">
      {/* Profile Header Section */}
      <Row className="mb-5 align-items-center">
        <Col md={4} className="text-center mb-4 mb-md-0">
          <Image
            src={profile}
            thumbnail
            width={280}
            className="profile-image shadow"
            alt="Fran Hermoso profile"
            style={{ borderColor: "#F39C12", padding: "4px" }}
          />
        </Col>
        <Col md={8}>
          <h1 className="display-4 mb-3">Fran Hermoso</h1>
          <p className="lead mb-4">
            GNU/Linux and Python enthusiast with a strong DevOps background,
            passionate about backend development and exploring new technologies.
          </p>
          <hr className="my-4" />
          <div className="social-links d-flex justify-content-start gap-3">
            {socialIcons.map((item, index) => (
              <a
                key={index}
                href={item.url}
                className="social-icon"
                aria-label={item.label}
                target="_blank"
                rel="noopener noreferrer"
              >
                <FontAwesomeIcon icon={item.icon} size="3x" />
              </a>
            ))}
          </div>
        </Col>
      </Row>

      {/* Profile Details Section */}
      <Row className="mt-4 d-flex equal-height-row">
        {/* Personal Info */}
        <Col lg={6} className="mb-4 mb-lg-0 d-flex">
          <ListGroup
            variant="flush"
            className="ProfileBox shadow-sm rounded w-100"
          >
            <ListGroup.Item className="bg-light py-3">
              <Row className="align-items-center">
                <Col xs={2} className="vertical-line text-center">
                  <FontAwesomeIcon icon={faMapMarkerAlt} size="2x" />
                </Col>
                <Col xs={10} className="text-center">
                  <span className="fs-5">Manresa (Barcelona)</span>
                </Col>
              </Row>
            </ListGroup.Item>

            <ListGroup.Item className="py-3">
              <Row className="align-items-center">
                <Col xs={2} className="vertical-line text-center">
                  <FontAwesomeIcon icon={faHeart} size="2x" />
                </Col>
                <Col xs={10}>
                  <div className="d-flex flex-wrap justify-content-center gap-3">
                    {interestIcons.map((item, index) => (
                      <div key={index} className="text-center icon-with-label">
                        <FontAwesomeIcon icon={item.icon} size="2x" />
                        <div className="small mt-1">{item.label}</div>
                      </div>
                    ))}
                  </div>
                </Col>
              </Row>
            </ListGroup.Item>

            <ListGroup.Item className="bg-light py-3">
              <Row className="align-items-center">
                <Col xs={2} className="vertical-line text-center">
                  <FontAwesomeIcon icon={faThumbsUp} size="2x" />
                </Col>
                <Col xs={10}>
                  <div className="d-flex flex-wrap justify-content-center gap-3">
                    {likeIcons.map((item, index) => (
                      <div key={index} className="text-center icon-with-label">
                        <FontAwesomeIcon icon={item.icon} size="2x" />
                        <div className="small mt-1">{item.label}</div>
                      </div>
                    ))}
                  </div>
                </Col>
              </Row>
            </ListGroup.Item>
          </ListGroup>
        </Col>

        {/* Skills */}
        <Col lg={6} className="d-flex">
          <ListGroup
            variant="flush"
            className="ProfileBox shadow-sm rounded w-100"
          >
            {skillGroups.map((group, groupIndex) => (
              <ListGroup.Item
                key={groupIndex}
                className={`py-3 ${groupIndex % 2 === 0 ? "bg-light" : ""}`}
              >
                <Row className="align-items-center">
                  <Col xs={3} className="vertical-line text-center">
                    <span className="fw-bold">{group.category}</span>
                  </Col>
                  <Col xs={9}>
                    <div className="d-flex flex-wrap justify-content-center gap-3">
                      {group.icons.map((item, index) => (
                        <div
                          key={index}
                          className="text-center icon-with-label"
                        >
                          <FontAwesomeIcon icon={item.icon} size="2x" />
                          <div className="small mt-1">{item.label}</div>
                        </div>
                      ))}
                    </div>
                  </Col>
                </Row>
              </ListGroup.Item>
            ))}
          </ListGroup>
        </Col>
      </Row>
    </Container>
  );
};

export default Home;
