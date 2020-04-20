import React from 'react';
import { Row, Media, Image } from 'react-bootstrap';
import bookmarks from '../api/bookmarks.json';
import categories from '../api/bookmark_categories.json';

class Bookmarks extends React.Component {
    renderLinks(category_id) {
        return (
            bookmarks.map(bookmark => {
                if (bookmark.fields.link_type === category_id) {
                    return (
                        <Media as="li">
                            <a href={bookmark.fields.url}>
                                <Image
                                    width={120}
                                    className="mr-5 mb-2"
                                    alt={bookmark.fields.slug}
                                    src={"./thumbnails/" + bookmark.fields.slug + ".png"}
                                    thumbnail
                                />
                            </a>
                            <Media.Body>
                                <h5><a href={bookmark.fields.url}>{bookmark.fields.name}</a></h5>
                                <p>{bookmark.fields.description}</p>
                            </Media.Body>
                        </Media>
                    )
                } else {
                    return (<></>);
                }

            })
        )
    }


    render() {
        return (
            categories.map(category => {
                return (
                    <Row>
                        <ul className="list-unstyled">
                            <h2>{category.fields.name}</h2>
                            {this.renderLinks(category.pk)}
                        </ul>
                    </Row>
                )
            })


        );
    }
}

export default Bookmarks;