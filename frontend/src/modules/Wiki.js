import React from 'react';
import { ListGroup, Container } from 'react-bootstrap';
import categories from '../api/wiki_categories.json';
import documents from '../api/wiki.json';



class Wiki extends React.Component {
    render() {
        return (
            <Container>
                <ListGroup>
                    {categories.map(category => {
                        return (
                            <ListGroup.Item action>
                                {category.fields.name}
                            </ListGroup.Item>
                        )
                    })}
                </ListGroup>
            </Container>

        );
    }
}

export default Wiki;