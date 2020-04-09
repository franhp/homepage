import React from 'react';
import logo from './logo.svg';
import './App.css';
import books from './api/books.json';


class Ranking extends React.Component {
  renderItem(value) {
    return (
      <li className="RankingItem">{value.fields.name}</li>
    );
  }

  render() {
    return (
      <div className="Ranking">
        <h1>{this.props.title} ranking</h1>
        <ol>
          {this.props.content.map(book => { return this.renderItem(book) })}
        </ol>
      </div>
    );
  }
}

function App() {
  return (
    <div className="App">

      <header className="App-header">
        <Ranking title="Books" content={books} />
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>

      </header>
    </div>
  );
}

export default App;
