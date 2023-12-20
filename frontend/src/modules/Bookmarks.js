import React from "react";
import { Row, ListGroup, ListGroupItem } from "react-bootstrap";
import bookmarks from "../api/bookmarks.json";
import categories from "../api/bookmark_categories.json";

class Bookmarks extends React.Component {
  renderLinks(category_id) {
    return bookmarks.map((bookmark) => {
      if (bookmark.fields.link_type === category_id) {
        return (
          <ListGroupItem>
            <h5>
              <a href={bookmark.fields.url}>
                {bookmark.fields.name}{" "}
                <small>
                  {bookmark.fields.year == null
                    ? ""
                    : "(" + bookmark.fields.year + ")"}
                </small>
              </a>
            </h5>
            <p>{bookmark.fields.description}</p>
          </ListGroupItem>
        );
      } else {
        return <></>;
      }
    });
  }

  render() {
    return categories.map((category) => {
      return (
        <Row>
          <ListGroup>
            <h2>{category.fields.name}</h2>
            {this.renderLinks(category.pk)}
          </ListGroup>
        </Row>
      );
    });
  }
}

export default Bookmarks;
