import React from 'react';
import { Container, Row, Media, Col } from 'react-bootstrap';
import GoogleMapReact from 'google-map-react';
import points from '../api/places.json';

import './Places.css';

class PlacesList extends React.Component {
    constructor(props) {
        super(props);

        var flags = {}
        var places = {}

        points.features.forEach(feature => {

            flags[feature.properties.country] = feature.properties.flag;

            var city = [feature.properties.city, feature.properties.date.split("-")[0]]
            if (Array.isArray(places[feature.properties.country])) {
                places[feature.properties.country].push(city);
            } else {
                places[feature.properties.country] = [city];
            }

        });

        this.state = {
            places: places,
            flags: flags,
            countries: Object.keys(flags)
        }
    }

    split_array(keys) {
        return [keys.slice(0, keys.length / 2), keys.slice(keys.length / 2)];
    }

    renderMedia(country) {
        return (

            <Media key={country}>
                <img width={65} height={45} className="mr-3" src={this.state.flags[country]} alt={country} />
                <Media.Body>
                    <h5>{country}</h5>
                    <ul className="list-unstyled">{this.state.places[country].map(city => {
                        return (
                            <li key={city}>
                                <small>{city[0]} <span className="badge badge-primary year">{city[1]}</span></small>
                            </li>
                        )
                    })}
                    </ul>
                </Media.Body>
            </Media>
        );
    }

    renderMediaCol(slice) {
        return (
            <Col sm={6} key={slice}>
                {slice.map(country => {
                    return this.renderMedia(country);
                })}
            </Col>
        );
    }

    render() {
        return (
            <Container>
                <h1>{this.state.countries.length} countries visited</h1>
                <Row>
                    {this.split_array(this.state.countries).map(slice => {
                        return this.renderMediaCol(slice);
                    })}
                </Row>
            </Container >
        );
    }
}

class Places extends React.Component {
    static defaultProps = {
        center: {
            lat: 50.736455,
            lng: 13.007813
        },
        zoom: 3
    };

    handleApiLoaded(map, maps) {
        map.data.addGeoJson(points);

        map.data.setStyle(function (feature) {
            return ({ "icon": "./faces/" + feature.j.attendants + ".png" })
        });
    }

    render() {
        return (
            <div className="Places">
                <div style={{ height: '50vh', width: '100%' }}>
                    {<GoogleMapReact
                        bootstrapURLKeys={{ key: process.env.REACT_APP_GOOGLE_API_KEY }}
                        defaultCenter={this.props.center}
                        defaultZoom={this.props.zoom}
                        yesIWantToUseGoogleMapApiInternals
                        onGoogleApiLoaded={({ map, maps }) => this.handleApiLoaded(map, maps)}
                    >
                    </GoogleMapReact>}
                </div>
                <PlacesList />

            </div>

        );
    }
}

export default Places;