import React from 'react';
import { ListGroup, Tab, Accordion, Card } from 'react-bootstrap';
import ReactMarkDown from 'react-markdown';
import categories from '../api/wiki_categories.json';
import documents from '../api/wiki.json';



class Wiki extends React.Component {
    render() {
        return (
            <Tab.Container>
                <ListGroup horizontal>
                    {categories.map(category => {
                        return (
                            <ListGroup.Item action href={"#" + category.fields.slug}>
                                {category.fields.name}
                            </ListGroup.Item>
                        )
                    })}
                </ListGroup>


                <Tab.Content>
                    {categories.map(category => {
                        return (
                            <Tab.Pane eventKey={"#" + category.fields.slug}>
                                <Accordion>
                                    {documents.map(document => {
                                        if (document.fields.category === category.pk) {
                                            return (
                                                <Card>
                                                    <Accordion.Toggle as={Card.Header} eventKey={document.fields.slug}>
                                                        {document.fields.title}
                                                    </Accordion.Toggle>
                                                    <Accordion.Collapse eventKey={document.fields.slug}>
                                                        <Card.Body>
                                                            <ReactMarkDown source={document.fields.content} />
                                                        </Card.Body>
                                                    </Accordion.Collapse>
                                                </Card>
                                            )
                                        } else {
                                            return <></>
                                        }
                                    })}
                                </Accordion>
                            </Tab.Pane>
                        )
                    })}
                </Tab.Content>

            </Tab.Container>

        );
    }
}

export default Wiki;