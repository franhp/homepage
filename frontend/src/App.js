import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { Navbar, Nav, Container, Image } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser, faBook, faLocationArrow, faLink, faFilm, faExclamation } from '@fortawesome/free-solid-svg-icons'

import cc from './images/by-nc-sa.eu.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import Home from './modules/Home';
import Rankings from './modules/Rankings';
import Places from './modules/Places';


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
              {this.renderTopButton("/wiki", faBook, "Wiki")}
              {this.renderTopButton("/bookmarks", faLink, "Bookmarks")}
              {this.renderTopButton("/places", faLocationArrow, "Places")}
              {this.renderTopButton("/rankings", faFilm, "Rankings")}
              {this.renderTopButton("/unknown", faExclamation, "Unknown")}
            </Nav>
          </Navbar.Collapse>
        </Navbar>

        <Container className="p-3 min">
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
          </Switch>
        </Container>

        <Navbar fixed="bottom" variant="light" bg="light" className="justify-content-center">
          <Image src={cc} id="footer-logo" />
        </Navbar>
      </Router >
    );
  }
}


export default App;
