# OnlineSurveyMaker

# Requirement
Python 3 and Django Installed \
run `python manage.py runserver` at root to start the application \
By Default, the website is hosted on `http://127.0.0.1:8000/` and the Survey Maker Appliction is hosted on `http://127.0.0.1:8000/smaker/`

# User Cases
1. The user create a new survey
2. Add multiple choice questions to the survey 
3. Save the surveys

# Approach
* A home page to choose between MAKE view or View view
* MAKE view:
    * Create Survey with custom name
    * Create Multiple Choice Question and Add to survey
    * Specify Number of Choices First, then use django form to generate textfields for input
    * Preview Created Questions
* View view:
    * View Created Surveys

# Models
* `MCUser` model contains username and date_joined fields. Hardcoded in the application as it is not the focus.
* `Survey` model contains creater field reference to `MCUser`, survey_name field to store the survey title and pud field to store the date of the survey created.
* `MCQuestion` model extends `Question` model from Django's turtorial(`polls` app); with foreign key reference to `Survey` models, question_txt to store the text of the question and pub_date to store the date of the question created.
* `MCChoice` model contains a reference to `MCQuestion` model, choice_text to sotre teh text of the choice of a multiple choice question.
* HighLevel Overview: 1 user -> N Surveys, 1 Survey -> N MCQuestion, 1 MCQuestion -> N MCChoice

# Views
* `index` view landing page of the app, contains two buttons `View Survey` and `Create New Survey`, and they will bring user to `ssview` view and `create` view coresspondingly.
* `Surveysview` shows a list of surveys created by the user as list of links when the user has created at least one survey. Links will bring user to the `Surveyview` view to display detail of the survey.
* `Surveyview` render survey as form without submit button.
* `create` view contains one text input field for user to enter the new survey's name. Submit will take the user to `initQ` view.
* `initQ` view contains one Integer input field for user to define how many multiple choices will the new question have. It also display a preview of the survey, showing survey's current added multiple choice question(s) if any.
* `buildQ` view contains one text input field for question text, and X text input fields as defined in `initQ` view for choices. Zero choice is prohibited. Valid submission will take user back to `initQ` view. A link to go back to `index` view.

# Not Implemented
* Create Question other than Multiple Choice
* Edit question
* Delete survey
* Delete question
* Dynamic field
* Active Form and Store Result 
* Choice or More for Multiple Choice Question

# Models to support other user filling out survey
* Create an `Answer` Model with a reference to `MCQuestion` model, a reference to `MCChoice` model PK, a reference to MCUser model PK
* Create an `User` Model with more fields than `MCUser` Model(maybe extend `MCUser` Model). Tihs includes a password field, and a email field for identification, to support other users(instead of hardcoding) to auhtenticate and log on. 



# Commands
Install Django \
`pip install Django` \
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