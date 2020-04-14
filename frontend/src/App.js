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



function App() {
  return (
    <Router>
      <Navbar sticky="top" expand="md" variant="dark" bg="dark">
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav" className="justify-content-center">
          <Nav>
            <Nav.Link href="/" className="mr-5">
              <span className="d-md-none d-lg-inline d-xl-inline">Home</span>&nbsp;
              <FontAwesomeIcon icon={faUser} />
            </Nav.Link>
            <Nav.Link href="/wiki" className="mr-5">
              <span className="d-md-none d-lg-inline d-xl-inline">Wiki</span>&nbsp;
              <FontAwesomeIcon icon={faBook} />
            </Nav.Link>
            <Nav.Link href="/bookmarks" className="mr-5">
              <span className="d-md-none d-lg-inline d-xl-inline">Bookmarks</span>&nbsp;
              <FontAwesomeIcon icon={faLink} />
            </Nav.Link>
            <Nav.Link href="/places" className="mr-5">
              <span className="d-md-none d-lg-inline d-xl-inline">Places</span>&nbsp;
              <FontAwesomeIcon icon={faLocationArrow} />
            </Nav.Link>
            <Nav.Link href="/rankings" className="mr-5">
              <span className="d-md-none d-lg-inline d-xl-inline">Rankings</span>&nbsp;
              <FontAwesomeIcon icon={faFilm} />
            </Nav.Link>
            <Nav.Link href="/unknown" className="mr-5">
              <span className="d-md-none d-lg-inline d-xl-inline">Unknown</span>&nbsp;
              <FontAwesomeIcon icon={faExclamation} />
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
      <Container className="content">
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/rankings">
            <Rankings />
          </Route>
        </Switch>
      </Container>
      <Navbar sticky="bottom" variant="dark" bg="dark" className="justify-content-center">
        <Image src={cc} id="footer-logo" />
      </Navbar>
    </Router >
  );
}

export default App;
