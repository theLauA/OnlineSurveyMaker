import React, { Component } from 'react';
import './App.css';
import axios from "axios";
import CustomModal from "./components/Modal";

class App extends Component {
  constructor(props){
    super(props);
    this.state={
      user:{
        name:"",
        id:1,
        surveys:[]
      },
      activeSurvey: null,
      modal:false,
      edit:false
    }
  }
  componentDidMount(){
    this.refreshUserInfo();
  }
  refreshUserInfo = () =>{
    axios
      .get("/api/users/"+this.state.user.id)
      .then(res => this.renderUserInfo(res.data))
      .catch(err => console.log(err));
  };
  renderUserInfo = (data) =>{
    if(data.id===this.state.user.id){
      
      this.setState({
        user:{
          ...this.state.user,
          name : data.username,
          surveys : data.surveys
        }
      });
    }
  };
  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };
  viewSurvey = (survey) => {
    this.setState({activeSurvey:survey,modal:!this.state.modal,edit:false});
    
  };
  editSurvey = (survey) => {
    if (survey.id) {
      axios
        .get("/api/surveys/"+survey.id)
        .then(res => {this.setState({activeSurvey:res.data, modal:!this.state.modal,edit:true});})
        .catch(err => console.log(err));
    }
  }
  
  renderSurveyList = () => {
    const surveys = this.state.user.surveys;
    return surveys.map(survey => (
      <li 
        key={survey.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className="mr-2">
            {survey.survey_name}
        </span>
        <span>
        <button
            onClick={() => this.viewSurvey(survey)}
            className="btn btn-success mr-2"
          >
            View{" "}
          </button>
          <button
          onClick={() => this.editSurvey(survey)}
            className="btn btn-secondary mr-2"
          >
            Edit{" "}
          </button>
          <button
            className="btn btn-danger"
          >
            Delete{" "}
          </button>
        </span>
      </li>
    ));

  };

  render() {
    return (
      <main className="content">
        <h1 className="text-white text-center my-4">Welcome {this.state.user.name}!</h1>
        <div className="row ">
          <div className="col-md-6 col-sm-10 mx-auto p-0 rounded bg-light">  
            <div className="card p-3">
              <div className="">
                <button className="btn btn-primary">
                    Create New Survey
                </button>
              </div>
              <h2>You have created {this.state.user.surveys.length} survey{this.state.user.surveys.length > 0 ?"s":""}</h2>
              <ul className="list-group list-group-flush">
                {this.renderSurveyList()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.modal ? (
          <CustomModal
          toggle={this.toggle}
          survey={this.state.activeSurvey}
          edit={this.state.edit}
        />
        ) : null}
      </main>
    );
  }
}

export default App;
