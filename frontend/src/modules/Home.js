import React from 'react';
import Image from 'react-bootstrap/Image';
import logo from '../images/logo.svg';


class Home extends React.Component {
    render() {
        return (
            <div className="App">

                <Image src={logo} width="200" height="400" thumbnail />



            </div >
        );
    }
}

export default Home;