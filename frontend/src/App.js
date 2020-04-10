import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { Navbar, Nav, Container, Image } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser, faBook, faLocationArrow, faLink, faFilm } from '@fortawesome/free-solid-svg-icons'

import cc from './images/by-nc-sa.eu.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import Home from './modules/Home';
import Rankings from './modules/Rankings';



function App() {
  return (
    <Router>
      <Navbar sticky="top" expand="lg" variant="dark" bg="dark">
        <Navbar.Brand href="/">
          <FontAwesomeIcon icon={faUser} />
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse>
          <Nav>
            <Nav.Link href="/wiki">
              Wiki <FontAwesomeIcon icon={faBook} />
            </Nav.Link>
            <Nav.Link href="/bookmarks">
              Bookmarks <FontAwesomeIcon icon={faLink} />
            </Nav.Link>
            <Nav.Link href="/places">
              Places <FontAwesomeIcon icon={faLocationArrow} />
            </Nav.Link>
            <Nav.Link href="/rankings">
              Rankings <FontAwesomeIcon icon={faFilm} />
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
      <Container>
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
        <Image src={cc} className="p-3" />
      </Navbar>
    </Router >
  );
}

export default App;
