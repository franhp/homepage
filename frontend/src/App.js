import React from 'react';
import { Link, BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import Rankings from './modules/Rankings';
import Home from './modules/Home';


function App() {
  return (
    <Router>
      <div>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/rankings">Rankings</Link>
          </li>
        </ul>

        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/rankings">
            <Rankings />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
