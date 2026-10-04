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
  faHtml5,
  faCss3,
  faKubernetes,
  faTypescript,
  faBrave,
  faWaze,
  faClaude,
  faGithub,
  faTelegram,
  faGitlab,
  faNodeJs,
  faJs,
  faPlaystation,
  faReddit,
  faGolang,
  faBitcoin,
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
  faCoffee,
  faThumbsUp,
  faDumbbell,
  faPersonHiking,
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
];

const interestIcons = [
  { icon: faBook, label: "Reading" },
  { icon: faPlaneDeparture, label: "Travel" },
  { icon: faGamepad, label: "Gaming" },
  { icon: faFilm, label: "Movies" },
  { icon: faCoffee, label: "Coffee" },
  { icon: faDumbbell, label: "Gym" },
  { icon: faPersonHiking, label: "Hiking" },
];

const likeIcons = [
  { icon: faPlaystation, label: "PlayStation" },
  { icon: faBitcoin, label: "Bitcoin" },
  { icon: faReddit, label: "Reddit" },
  { icon: faTelegram, label: "Telegram" },
  { icon: faWaze, label: "Waze" },
  { icon: faClaude, label: "Claude" },
  { icon: faBrave, label: "Brave" },
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
      { icon: faGitlab, label: "GitLab" },
      { icon: faGithub, label: "GitHub" },
      { icon: faKubernetes, label: "Kubernetes" },
    ],
  },
  {
    category: "Frontend",
    icons: [
      { icon: faTypescript, label: "TypeScript" },
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
            className="shadow"
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
      <Row className="mt-4 d-flex">
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
                      <div key={index} className="text-center">
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
                      <div key={index} className="text-center">
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
                        <div key={index} className="text-center">
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
