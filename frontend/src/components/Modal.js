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
import axios from "axios";

export default class CustomModal extends Component{
    constructor(props){
        super(props);
        this.state = {
            survey: null,
            questions: [],
            edit: this.props.edit,
            activeQuestion: null,
            newQuestionsChoices: 0
        }
    }
    componentDidMount(){
        this.refreshSurvey();
    }
    refreshSurvey = () => {
        const survey = this.props.survey;
        if (survey.id) {
          axios
            .get("/api/surveys/"+survey.id)
            .then(res => {this.setState({survey:res.data})})
            .catch(err => console.log(err));
        }
    }
    renderQuestions = () =>{

        if(this.state.survey){
            const questions = this.state.survey.questions;
        
            return questions.map(question => (
                <FormGroup tag="fieldset" key={"question_"+question.id}>
                    <legend>{question.question_text}</legend>
                    {this.renderChoices(question.choices)}
                </FormGroup>
            ));
        }
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

    handleChange = e => {
        if(e.target.value > 0){
            this.setState({newQuestionsChoices:e.target.value})
        }
    }
    handleSubmit = e=>{
        if(this.state.newQuestionsChoices > 0){
            console.log(this.state.newQuestionsChoices);
        }
    }

    render(){
        const {toggle, onSave} = this.props;
        return(
            <Modal isOpen={true} toggle={toggle}>
                <ModalHeader toggle={toggle}>{this.state.survey?this.state.survey.survey_name:""}</ModalHeader>
                <ModalBody>
                    {this.props.edit?(
                        <Form>
                            <FormGroup>
                                <Label for="noc">Number of Choices with Your New Multiple Choice Question Have</Label>
                                <Input type="text" name="numberOfChoices" id="noc" pattern="[0-9]*" onChange={this.handleChange}/>
                            </FormGroup>
                            <Button onClick={this.handleSubmit}>Create New Question</Button>
                        </Form>
                    ):null}
                    {this.props.edit?(<h3>survey Preview</h3>):null}
                    <Form>
                        {this.renderQuestions()}
                    </Form>
                </ModalBody>
            </Modal>
        )
    }
}

