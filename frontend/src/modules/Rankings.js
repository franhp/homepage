import React from 'react'
import books from '../api/books.json';
import movies from '../api/movies.json';
import tvseries from '../api/tvseries.json'
import watched from '../api/watched.json';

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

class RankingStats extends React.Component {
    render() {
        return (
            <div className="RankingStats">
                <ul>
                    <li>Last Update: {this.props.content.last_update}</li>
                    <li>Count TV Series: {this.props.content.count_tvseries}</li>
                    <li>Count Movies: {this.props.content.count_movies}</li>
                    <li>Count Books: {this.props.content.count_books}</li>
                </ul>
            </div>
        );
    }
}

class Rankings extends React.Component {
    render() {
        return (
            <div className="Rankings">
                <RankingStats content={watched} />
                <Ranking title="Books" content={books} />
                <Ranking title="Movies" content={movies} />
                <Ranking title="TV Shows" content={tvseries} />
            </div>
        );
    }
}

export default Rankings;