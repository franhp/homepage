import React, { useState } from 'react';
import { ListGroup, Tab, Accordion, Card } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowRight, faArrowDown } from '@fortawesome/free-solid-svg-icons'
import ReactMarkDown from 'react-markdown';
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { coy } from "react-syntax-highlighter/dist/esm/styles/prism";
import categories from '../api/wiki_categories.json';
import documents from '../api/wiki.json';

import './Wiki.css'

class CodeBlock extends React.PureComponent {
    static defaultProps = {
        language: null
    };

    render() {
        const { language, value } = this.props;
        return (
            <SyntaxHighlighter language={language} style={coy}>
                {value}
            </SyntaxHighlighter>
        );
    }
}

function CollapsibleCard(document) {
    const [open, setOpen] = useState(false);

    return (
        <Card>
            <Accordion.Toggle as={Card.Header} eventKey={document.fields.slug} onClick={() => setOpen(!open)}>
                {document.fields.title} {open ? <FontAwesomeIcon icon={faArrowDown} /> : <FontAwesomeIcon icon={faArrowRight} />}
            </Accordion.Toggle>
            <Accordion.Collapse eventKey={document.fields.slug}>
                <Card.Body>
                    <ReactMarkDown source={document.fields.content} renderers={{ code: CodeBlock }} />
                    <div className="text-right">Last Update: <i>{document.fields.date.split('T')[0]}</i></div>
                </Card.Body>
            </Accordion.Collapse>
        </Card>
    );
}

class Wiki extends React.Component {
    render() {
        return (
            <Tab.Container>
                <ListGroup horizontal className="text-center mb-3">
                    {categories.map(category => {
                        return (
                            <ListGroup.Item action href={"#" + category.fields.slug}>
                                {category.fields.name}&nbsp;
                                <div className="badge badge-secondary badge-pill">
                                    {documents.map(document => { return (document.fields.category === category.pk) ? 1 : 0 }).reduce((a, b) => a + b, 0)}
                                </div>
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
                                            return <CollapsibleCard {...document} />
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