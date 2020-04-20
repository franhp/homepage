import React, { useState } from 'react';
import { Container, Row, Media, Col, Collapse } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlus, faMinus } from '@fortawesome/free-solid-svg-icons';
import GoogleMapReact from 'google-map-react';
import points from '../api/places.json';

import './Places.css';


function CollapsibleCityList(params) {
    const [open, setOpen] = useState(false);

    return (
        <div className={params.country + "collapsible"}>
            <span
                onClick={() => setOpen(!open)}
                aria-controls={params.country + "unfold"}
                aria-expanded={open}
            >{open ? <FontAwesomeIcon icon={faMinus} size="xs" /> : <FontAwesomeIcon icon={faPlus} size="xs" />}</span>
            <Collapse in={open}>
                <div id={params.country + "unfold"}>
                    {params.cities.map(city => {
                        return (
                            <li key={city}>
                                <small>{city[0]} <span className="badge badge-primary year">{city[1]}</span></small>
                            </li>
                        )
                    })}
                </div>
            </Collapse>
        </div>
    );
}

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

    renderCityList(country) {
        if (this.state.places[country].length > 3) {
            return (
                <>
                    {
                        this.state.places[country].slice(0, 3).map(city => {
                            return (
                                <li key={city}>
                                    <small>{city[0]} <span className="badge badge-primary year">{city[1]}</span></small>
                                </li>
                            )
                        })
                    }
                    < CollapsibleCityList country={country} cities={this.state.places[country].slice(3)} />
                </>
            )
        } else {
            return (
                this.state.places[country].map(city => {
                    return (
                        <li key={city}>
                            <small>{city[0]} <span className="badge badge-primary year">{city[1]}</span></small>
                        </li>

                    )
                })
            )
        }
    }

    renderMedia(country) {
        return (
            <Media key={country}>
                <img width={65} height={45} className="mr-3" src={this.state.flags[country]} alt={country} />
                <Media.Body>
                    <h5>{country}</h5>
                    <ul className="list-unstyled">
                        {this.renderCityList(country)}
                    </ul>
                </Media.Body>
            </Media >
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

const getInfoWindowString = place => `
    <div style="width: 100%; overflow: hidden; table; text-align: center;">
            <div style="width: 100px; float: left;">
                <img src="${place.getProperty('flag')}" width="75px"/>
            </div>
            <div style="margin-left: 100px; color: black;">
                <b>${place.getProperty('city')}</b><br>
                ${place.getProperty('country')} <br>
                <i>${place.getProperty('date').split('-')[0]}</i>
            </div>
    </div>`;

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

        map.data.addListener('click', function (event) {
            // Create nice infowindow
            var info = new maps.InfoWindow()
            info.setContent(getInfoWindowString(event.feature));
            info.setPosition(event.feature.getGeometry().get());
            info.setOptions({ pixelOffset: new maps.Size(0, -30) });
            info.open(map);

            // Center the face
            map.setZoom(6);
            map.setCenter(event.feature.getGeometry().get());
        });

    }

    render() {
        return (
            <div className="Places">
                <div style={{ height: '50vh', width: '100%' }}>
                    {
                        <GoogleMapReact
                            bootstrapURLKeys={{ key: process.env.REACT_APP_GOOGLE_API_KEY }}
                            defaultCenter={this.props.center}
                            defaultZoom={this.props.zoom}
                            yesIWantToUseGoogleMapApiInternals
                            onGoogleApiLoaded={({ map, maps }) => this.handleApiLoaded(map, maps)}
                        >
                        </GoogleMapReact>
                    }
                </div>
                <PlacesList />
            </div>

        );
    }
}

export default Places;