import React, { Component } from "react";
import {
    Button,
    Modal,
    ModalHeader,
    ModalBody,
    ModalFooter,
    Form,
    FormGroup,
    Input,
    Label
  } from "reactstrap";

export default class ViewModal extends Component{
    constructor(props){
        super(props);
        this.state = {
            survey: this.props.survey,
            questions: []
        }
    }
    componentDidMount(){
        
    }
    renderQuestions = () =>{
        const questions = this.state.survey.questions;
        
        return questions.map(question => (
            <FormGroup tag="fieldset" key={"question_"+question.id}>
                <legend>{question.question_text}</legend>
                {this.renderChoices(question.choices)}
            </FormGroup>
        ));

    };

    renderChoices = (choices) => {
        return choices.map(choice =>(
            <FormGroup check key={"choice_"+choice.id}>
                <Label check>
                    <Input type="radio" name="radio1"/>{' '}
                    {choice.choice_text}
                </Label>
            </FormGroup>
        ));
    }

    render(){
        const {toggle, onSave} = this.props;
        return(
            <Modal isOpen={true} toggle={toggle}>
                <ModalHeader toggle={toggle}>{this.state.survey.survey_name}</ModalHeader>
                <ModalBody>
                    <Form>
                        {this.renderQuestions()}
                    </Form>
                </ModalBody>
            </Modal>
        )
    }
}