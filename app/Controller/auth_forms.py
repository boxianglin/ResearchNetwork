from datetime import date, datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,BooleanField
from wtforms.fields.core import  RadioField
from wtforms.fields.html5 import DateField
from wtforms.fields.simple import TextAreaField 
from wtforms.validators import DataRequired, Email, Length, ValidationError, equal_to
from app.Model.models import ProgrammingLanguages, ResearchTopics, User, TechnicalElectives
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput

'''
User login form component
''' 
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

'''
Faculty registration form component
'''
class FacultyRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    wsuid = StringField('WSU ID', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Paswword', validators=[DataRequired(), equal_to('password')]) 
    submit = SubmitField('Register As Faculty')

    def validate_username(self, username):
        faculty = User.query.filter_by(username = username.data).first()
        if faculty is not None:
            raise ValidationError('The username already existed! Please use a different username.')

    # Check for the uniqueness for email
    def validate_email(self, email):
        faculty = User.query.filter_by(email = email.data).first()
        if faculty is not None:
            raise ValidationError('The email already existed! Please use a different email address.')

    def validate_WSUID(self, wsuid):
        user = User.query.filter_by(wsuid = wsuid.data).first()
        if user is not None:
            raise ValidationError('The WSUID already existed! Please use a differen WSUID!')


def get_programming():
    return ProgrammingLanguages.query.all()

def get_researchtopic():
    return ResearchTopics.query.all()

def get_TechnicalElectives():
    return TechnicalElectives.query.all()

def get_programmingLable(theProgramming):
    return theProgramming.name

def get_researchtopicLabel(research):
    return research.title

def get_TechnicalElectivesLabel(theElectives):
    return theElectives.title

'''
Student registration form component
'''
class StudentRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    wsuid = StringField('WSU ID', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Paswword', validators=[DataRequired(), equal_to('password')]) 
    major = StringField('Major', validators=[DataRequired()])
    GPA = StringField('GPA', validators=[DataRequired()])
    gradulation = DateField('Gradulation Date', format='%Y-%m-%d') #%H:%M:%S'
    elective = QuerySelectMultipleField('Technical Electives', query_factory = get_TechnicalElectives, get_label = get_TechnicalElectivesLabel, allow_blank=False)
    researchtopic = QuerySelectMultipleField('Research Topics', query_factory = get_researchtopic, get_label = get_researchtopicLabel, allow_blank=False)
    programming =  QuerySelectMultipleField('Programming Languages', query_factory = get_programming, get_label = get_programmingLable, allow_blank=False)
    experience = TextAreaField('Experience: ',validators=[DataRequired()])
    submit = SubmitField('Register As Student')

    def validate_username(self, username):
        student = User.query.filter_by(username = username.data).first()
        if student is not None:
            raise ValidationError('The username already existed! Please use a different username.')

    # Check for the uniqueness for email
    def validate_email(self, email):
        student = User.query.filter_by(email = email.data).first()
        if student is not None:
            raise ValidationError('The email already existed! Please use a different email address.')

    def validate_WSUID(self, wsuid):
        user = User.query.filter_by(wsuid = wsuid.data).first()
        if user is not None:
            raise ValidationError('The WSUID already existed! Please use a differen WSUID!')

    def validate_gradulation(self, gradulation):

        if gradulation.data is not None:
            if gradulation.data < date.today():
                raise ValidationError("Graduation date must later than today!")