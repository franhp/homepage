import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  NavLink,
} from "react-router-dom";
import { Navbar, Nav, Container, Image } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faLocationArrow,
  faBookmark,
  faTrophy,
} from "@fortawesome/free-solid-svg-icons";
import {
  faCreativeCommons,
  faCreativeCommonsBy,
  faCreativeCommonsNcEu,
  faCreativeCommonsSa,
} from "@fortawesome/free-brands-svg-icons";

import "./custom.scss";
import logo from "./images/logo.png";

import Home from "./modules/Home";
import Rankings from "./modules/Rankings";
import Places from "./modules/Places";
import Bookmarks from "./modules/Bookmarks";
// import Wiki from "./modules/Wiki";

class App extends React.Component {
  renderTopButton(href, icon, name) {
    return (
      <NavLink to={href} className="nav-link">
        <FontAwesomeIcon icon={icon} />
        &nbsp;
        <span className="d-md-none d-lg-inline d-xl-inline">{name}</span>
      </NavLink>
    );
  }

  render() {
    return (
      <Router>
        <Navbar sticky="top" expand="md" variant="light" bg="light">
          <Navbar.Brand href="/" className="ms-5">
            <Image src={logo} width={25} />
            &nbsp;
            <span className="d-md-none d-lg-inline d-xl-inline">franhp</span>
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="responsive-navbar-nav" />
          <Navbar.Collapse
            id="responsive-navbar-nav"
            className="justify-content-center"
          >
            <Nav>
              {this.renderTopButton("/rankings", faTrophy, "Rankings")}
              {this.renderTopButton("/places", faLocationArrow, "Places")}
              {this.renderTopButton("/bookmarks", faBookmark, "Bookmarks")}
              {/* {this.renderTopButton("/wiki", faFolderOpen, "Wiki")} */}
              {/* {this.renderTopButton("/unknown", faTrophy, "Unknown")} */}
            </Nav>
          </Navbar.Collapse>
        </Navbar>

        <Container className="p-3 pb-5">
          <Routes>
            <Route exact path="/" element={<Home />} />
            <Route path="/rankings" element={<Rankings />} />
            <Route path="/places" element={<Places />} />
            <Route path="/bookmarks" element={<Bookmarks />} />
            {/* <Route path="/wiki" element={<Wiki />} /> */}
          </Routes>
        </Container>

        <Navbar
          fixed="bottom"
          variant="light"
          bg="light"
          className="justify-content-center"
        >
          <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
            <FontAwesomeIcon icon={faCreativeCommons} size="sm" />
            <FontAwesomeIcon icon={faCreativeCommonsBy} size="sm" />
            <FontAwesomeIcon icon={faCreativeCommonsNcEu} size="sm" />
            <FontAwesomeIcon icon={faCreativeCommonsSa} size="sm" />
          </a>
        </Navbar>
      </Router>
    );
  }
}

export default App;
