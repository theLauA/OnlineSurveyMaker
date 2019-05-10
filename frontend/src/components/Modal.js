import React, { Component } from "react";
import {
    Button,
    Modal,
    ModalHeader,
    ModalBody,
    ModalFooter,
    Col,
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
            activeQuestion: {
                question_text:"",
                choices:{}
            },
            newQuestionsChoices: 0,
            editQuestion: false
        }
    }
    
    componentDidMount(){
        this.refreshSurvey();
    }

    //Initialize and Populate Survey
    refreshSurvey = () => {
        const survey = this.props.survey;
        if (survey.id) {
          axios
            .get("/api/surveys/"+survey.id)
            .then(res => {this.setState({survey:res.data})})
            .catch(err => console.log(err));
        }
    }
    //Helper Function to Populate Survey
    //Populate Questions
    renderQuestions = () =>{

        if(this.state.survey){
            
            const questions = this.state.survey.questions;
            if(questions){
                return questions.map(question => (
                    <FormGroup tag="fieldset" key={"question_"+question.id}>
                        <legend>{question.question_text}</legend>
                        {this.renderChoices(question.choices)}
                    </FormGroup>
                ));
            } 
        }
    };

    //Helper Function Populate Questions
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

    //Render View for creating new Multiple Choice
    renderNewChoices = (num_of_choices) =>{
        const mcquestion = [];
        for(let i = 0; i < num_of_choices; i ++){
            mcquestion.push(
                <FormGroup row key={"newchoice_"+i}>
                    <Label for={"newchoice"+i} sm={2}>{"Choice"+(i+1)}</Label>
                    <Col sm={10}>
                    <Input type="text" name={"newchoice"+i} id={"newchoice"+i} placeholder={"Choice"+(i+1)} onChange={this.handleChange}/>
                    </Col>
                </FormGroup>
            );
        }
        return mcquestion;
    }

    //Handle Form for creating new Multiple Choice Question
    handleChange = e => {
        let { name, value } = e.target;
        var activeQuestion = {};
        if(name==="question_text"){
            activeQuestion = { ...this.state.activeQuestion, [name]: value };
        }
        else{
            activeQuestion = { ...this.state.activeQuestion, choices:{...this.state.activeQuestion.choices,[name]: value} };
        }
        this.setState({ activeQuestion });
    };
    handleCreate = e =>{
        console.log(this.state.activeQuestion)
        if(this.state.activeQuestion.question_text !== "" && Object.keys(this.state.activeQuestion.choices).length === this.state.newQuestionsChoices){
            
            //Formate Data
            var question = this.state.activeQuestion;
            var choices = question.choices;
            var choices_list = []
            for (var choice in choices){
                
                choices_list.push({choice_text:choices[choice]})
            };
            question.choices = choices_list;
            axios
                .put("/api/surveys/"+this.state.survey.id+"/",question)
                .then(res => this.reset());
        }
        this.reset();
    }

    //Specify How Many Choices will the new Multiple Choice Question Has
    handleNumberChange = e => {
        const value = parseInt(e.target.value)
        if(value > 0){
            this.setState({newQuestionsChoices:value})
        }
    };
    handleSubmit = e=>{
        
        if(this.state.newQuestionsChoices > 0){
            this.setState({editQuestion:true});
        }
    };


    //Reset After Creating a New Question
    reset = () => {
        this.setState({activeQuestion: {
            question_text:"",
            choices:{}
        },
        newQuestionsChoices: 0,
        editQuestion: false});
        this.refreshSurvey();
    };
    render(){
        const {toggle, onSave} = this.props;
        return(
            <Modal isOpen={true} toggle={toggle}>
                <ModalHeader toggle={toggle}>{this.state.survey?this.state.survey.survey_name:""}</ModalHeader>
                <ModalBody>
                    {this.props.edit&&!this.state.editQuestion?(
                        <Form>
                            <FormGroup>
                                <Label for="noc">Number of Choices with Your New Multiple Choice Question Have</Label>
                                <Input type="text" name="numberOfChoices" id="noc" pattern="[0-9]*" onChange={this.handleNumberChange}/>
                            </FormGroup>
                            <Button onClick={this.handleSubmit}>Create New Question</Button>
                        </Form>
                    ):null}
                    {this.props.edit&&this.state.editQuestion?(
                        <Form>
                            <FormGroup>
                                <Label>New Question</Label>
                                <Input type="text" name="question_text" placeholder="New Question" id="newQuestion" onChange={this.handleChange}/>
                            </FormGroup>
                            {this.renderNewChoices(this.state.newQuestionsChoices)}
                            <Button onClick={()=>this.handleCreate()}>Add Question</Button>
                        </Form>
                    ):null}
                    {this.props.edit?(<h3>Survey Preview</h3>):null}
                    <Form>
                        {this.renderQuestions()}
                    </Form>
                </ModalBody>
            </Modal>
        )
    }
}

