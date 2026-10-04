import React from "react";
import { ListGroup, ListGroupItem } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowUpRightFromSquare } from "@fortawesome/free-solid-svg-icons";
import bookmarks from "../api/bookmarks.json";
import categories from "../api/bookmark_categories.json";

class Bookmarks extends React.Component {
  renderLinks(items) {
    return items.map((bookmark) => {
      return (
        <ListGroupItem className="bookmark-item" key={bookmark.pk}>
          <div className="bookmark-copy">
            <div className="bookmark-heading">
              <a className="bookmark-link" href={bookmark.fields.url}>
                {bookmark.fields.name}
                <FontAwesomeIcon
                  className="bookmark-link-icon"
                  icon={faArrowUpRightFromSquare}
                />
              </a>
              {bookmark.fields.year != null && (
                <span className="bookmark-year">{bookmark.fields.year}</span>
              )}
            </div>
            <p className="bookmark-description">
              {bookmark.fields.description}
            </p>
          </div>
        </ListGroupItem>
      );
    });
  }

  render() {
    return (
      <div className="Bookmarks">
        {categories.map((category) => {
          const items = bookmarks.filter(
            (bookmark) => bookmark.fields.link_type === category.pk
          );
          return (
            <section key={category.pk}>
              <div className="bookmark-section-heading">
                <h2 className="bookmark-category">{category.fields.name}</h2>
                <span className="bookmark-count">{items.length}</span>
              </div>
              <ListGroup className="bookmark-list">
                {this.renderLinks(items)}
              </ListGroup>
            </section>
          );
        })}
      </div>
    );
  }
}

export default Bookmarks;
