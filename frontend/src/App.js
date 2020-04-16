import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { Navbar, Nav, Container } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser, faFileCode, faLocationArrow, faExclamation, faBookmark, faTrophy } from '@fortawesome/free-solid-svg-icons'
import { faCreativeCommons, faCreativeCommonsBy, faCreativeCommonsNcEu, faCreativeCommonsSa } from '@fortawesome/free-brands-svg-icons'

import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import Home from './modules/Home';
import Rankings from './modules/Rankings';
import Places from './modules/Places';
import Bookmarks from './modules/Bookmarks';


class App extends React.Component {
  renderTopButton(href, icon, name) {
    return (
      <Nav.Link href={href} className="mr-5">
        <FontAwesomeIcon icon={icon} />&nbsp;
        <span className="d-md-none d-lg-inline d-xl-inline">{name}</span>
      </Nav.Link>
    )
  }

  render() {
    return (
      <Router>
        <Navbar sticky="top" expand="md" variant="light" bg="light">
          <Navbar.Brand>
            <a href="/">
              <FontAwesomeIcon icon={faUser} />&nbsp;
              <span className="d-md-none d-lg-inline d-xl-inline">franhp</span>
            </a>
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="responsive-navbar-nav" />
          <Navbar.Collapse id="responsive-navbar-nav" className="justify-content-center">
            <Nav>
              {this.renderTopButton("/rankings", faTrophy, "Rankings")}
              {this.renderTopButton("/places", faLocationArrow, "Places")}
              {this.renderTopButton("/bookmarks", faBookmark, "Bookmarks")}
              {this.renderTopButton("/wiki", faFileCode, "Wiki")}
              {this.renderTopButton("/unknown", faExclamation, "Unknown")}
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
          </Switch>
        </Container>

        <Navbar sticky="bottom" variant="light" bg="light" className="justify-content-center">
          <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
            <FontAwesomeIcon icon={faCreativeCommons} />
            <FontAwesomeIcon icon={faCreativeCommonsBy} />
            <FontAwesomeIcon icon={faCreativeCommonsNcEu} />
            <FontAwesomeIcon icon={faCreativeCommonsSa} />
          </a>
        </Navbar>
      </Router >
    );
  }
}


export default App;
