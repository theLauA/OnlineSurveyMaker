# OnlineSurveyMaker

# User Cases
1. The user create a new survey
2. Add multiple choice questions to the survey 
3. Save the surveys

# Approach 1
* A home page to choose between MAKE view or View view
* MAKE view:
..* Create Survey with custom name
..* Create Multiple Choice Question and Add to survey
..* Specify Number of Choices First, then use django form to generate textfields for input
..* Preview Created Questions
* View view:
..* View Created Surveys

# Porgress
1. Go through DJango turtorial
..* Went through 2 parts of DJango turtorial which is a polling app. Will build on the turtorial app instead of using additional open source packages.
..* Finished turtorial except
2. Create new app, surveymaker
..* Pass userId between views using session 

# Requirement
Python 3

# Commands
Install Django
`pip install Django`
Start Web-App when in folder
`python manager.py runserver`
Create Django project
`django-admin startproject mysite`
Create Django applicaton
`python manager.py startapp appname` 