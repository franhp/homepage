import React from 'react'
import logo from '../images/logo.svg';

class Home extends React.Component {
    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo" />
                    <div className="Home">
                        <h1>Home</h1>
                    </div>
                </header>
            </div >
        );
    }
}

export default Home;