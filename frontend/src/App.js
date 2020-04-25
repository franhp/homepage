import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { Navbar, Nav, Container, Image } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faFileCode,
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

import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import logo from "./images/logo.png";

import Home from "./modules/Home";
import Rankings from "./modules/Rankings";
import Places from "./modules/Places";
import Bookmarks from "./modules/Bookmarks";
import Wiki from "./modules/Wiki";

class App extends React.Component {
  renderTopButton(href, icon, name) {
    return (
      <Nav.Link href={href} className="mr-5">
        <FontAwesomeIcon icon={icon} />
        &nbsp;
        <span className="d-md-none d-lg-inline d-xl-inline">{name}</span>
      </Nav.Link>
    );
  }

  render() {
    return (
      <Router>
        <Navbar sticky="top" expand="md" variant="light" bg="light">
          <Navbar.Brand>
            <a href="/">
              <Image src={logo} width={25} />
              &nbsp;
              <span className="d-md-none d-lg-inline d-xl-inline">franhp</span>
            </a>
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
              {this.renderTopButton("/wiki", faFileCode, "Wiki")}
              {/* {this.renderTopButton("/unknown", faTrophy, "Unknown")} */}
            </Nav>
          </Navbar.Collapse>
        </Navbar>

        <Container className="p-3">
          <Switch>
            <Route exact path="/">
              <Home />
            </Route>
            <Route path="/rankings">
              <Rankings />
            </Route>
            <Route path="/places">
              <Places />
            </Route>
            <Route path="/bookmarks">
              <Bookmarks />
            </Route>
            <Route path="/wiki">
              <Wiki />
            </Route>
          </Switch>
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
