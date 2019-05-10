# OnlineSurveyMaker

# Requirement
PipEnv, Python 3 and Django Installed \
To start backend:
make sure packages are install `pipenv install djangorestframework django-cors-headers` \
start vitual environment `cd bacckend`, `pipenv shell` \
run `python manage.py runserver` at root to start the backend server \
By Default, the website is hosted on `http://localhost:8000/` and this is what the REACT front end is configured to \
To start frontend:
go to root and `cd frontend`\
install packages `yarn install`\
start client `yarn start`

# User Cases
1. The user create a new survey
2. Add multiple choice questions to the survey 
3. Save the survey

# Approach
* A home page to choose between creating a new survey, viewing an existing survey, and adding new question to an existing survey
* View an existing survey
    * A Modal is poped up rendering the survey
    * No submit button
* Edit an existing survey
    * A Modal is poped up
        * A Textfield to define how many choices with the new question has
        * A preview for created questions in the survey
    * share Modal with View
* Create a new Survey
    * A Text Field in Home Page to ask for new Survey's Name
    * A Modal with pop allowing user to add new Question
        * Same Modal as Edit
* Use Modal to keep the one page design, and reduce routing

# Models
* `MCUser` model contains username and date_joined fields. Hardcoded in the application as it is not the focus.
* `Survey` model contains creater field reference to `MCUser`, survey_name field to store the survey title and pud field to store the date of the survey created.
* `MCQuestion` model extends `Question` model from Django's turtorial(`polls` app); with foreign key reference to `Survey` models, question_txt to store the text of the question and pub_date to store the date of the question created.
* `MCChoice` model contains a reference to `MCQuestion` model, choice_text to sotre teh text of the choice of a multiple choice question.
* HighLevel Overview: 1 user -> N Surveys, 1 Survey -> N MCQuestion, 1 MCQuestion -> N MCChoice

# React Component
* App
    * A landing page to display username and surveys
    * Surveys are display as list
        * Name
        * Three buttons (DELETE is not working)
    * Click on EDIT or VIEW will open the Modal Component
    * A TEXT INPUT field to enter survey name
        * Create a survey and Open Modal in Edit Mode upon submit
* Modal
    * Two Mode
        * View mode will just render the survey
        * Edit mode will allow user to add question

# Test
* A simple Test against url and placeholder text is createer
* run `python manager.py test surveymaker`

# Not Implemented
* Create Question other than Multiple Choice
* Edit question
* Delete question
* Dynamic field
* Active Form and Store Result 
* Choice or More for Multiple Choice Question
* Scheduled publication of survey
* Grouping Surveys

# To support other user filling out survey
* If we want other user to execute the survey, we would want the result of the survey to be saved. Currently, my view to display survey doesn't allow user to submit their answer. I would have a new view rendering the survey provided with user and survey as context, and allow user to submit their result.
* Create an `Answer` Model with a reference to `MCQuestion` model, a reference to `MCChoice` model PK, a reference to MCUser model PK
* Create an `User` Model with more fields than `MCUser` Model(maybe extend `MCUser` Model). Tihs includes a password field, and a email field for identification, to support other users(instead of hardcoding) to auhtenticate and log on. If permission is also a concern, additional models for group and membership will also be needed.



# Commands
Start Web-App when in folder \
`python manager.py runserver` \
Create Django project \
`django-admin startproject mysite` \
Create Django applicaton \
`python manager.py startapp appname` \
Reset database migration define by app \
`python manager.py --fake surveymaker zero` 

# Porgress
1. Go through DJango turtorial
..* Went through 2 parts of DJango turtorial which is a polling app. Will build on the turtorial app instead of using additional open source packages.
..* Finished turtorial except
2. Create new app, surveymaker
..* Pass userId between views using session
3. Added Features: ability to create a new survey and add mc questions to the survey; view created survey
4. Added: ability to add multiple choice question to a created survey.
5. REACT UI inspired by: https://scotch.io/tutorials/build-a-to-do-application-using-django-and-react
6. Added: REACT UI added. Ditched Django html views, and use it as REST server.
7. Use pipenv to set up backend environment