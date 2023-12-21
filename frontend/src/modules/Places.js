import React from "react";
import { Container, Row, ListGroup, ListGroupItem } from "react-bootstrap";
import points from "../api/geoplaces.json";
import countries from "../api/countries.json";
import { MapContainer, Marker, TileLayer } from "react-leaflet";

import "leaflet/dist/leaflet.css";
import { Icon } from "leaflet";
import markerFranPng from "./../images/faces/fran.png";
import markerSaraPng from "./../images/faces/sara.png";
import markerHomePng from "./../images/faces/home.png";
import markerTogetherPng from "./../images/faces/together.png";

class PlacesList extends React.Component {
  renderMedia(country) {
    return (
      <ListGroupItem className="d-flex justify-content-between align-items-start">
        <div className="ms-2 me-auto">
          <h5 className="fw-bold">{country.fields.name}</h5>
          {country.fields.cities.join(", ")}
        </div>
        <span className="fs-1">{country.fields.flag}</span>
      </ListGroupItem>
    );
  }

  render() {
    return (
      <Container>
        <h1>{countries.length} countries visited</h1>
        <ListGroup>
          {countries.map((country) => this.renderMedia(country))}
        </ListGroup>
      </Container>
    );
  }
}

class Places extends React.Component {
  render() {
    return (
      <Container className="Places">
        <MapContainer
          center={[51.0, 19.0]}
          zoom={3}
          scrollWheelZoom={false}
          className="MapContainer"
        >
          <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          {points.map((point) => {
            let icon;
            switch (point.icon) {
              case "together":
                icon = markerTogetherPng;
                break;
              case "sara":
                icon = markerSaraPng;
                break;
              case "fran":
                icon = markerFranPng;
                break;
              case "home":
                icon = markerHomePng;
                break;
              default:
                icon = markerFranPng;
            }
            return (
              <Marker
                position={point.position}
                icon={new Icon({ iconUrl: icon })}
              />
            );
          })}
        </MapContainer>
        <Row>
          <PlacesList />
        </Row>
      </Container>
    );
  }
}

export default Places;
