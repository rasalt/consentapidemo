# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_storage_app]
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email
#import email_validator

class LoginForm(FlaskForm):
    email = StringField('Email',
                             validators=[DataRequired()])
                           # validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                             validators=[DataRequired()]) 

    submit = SubmitField('Submit')

consentList = [
    "Allow activity data to be shared with your healthcare provider?", #0
    "Allow activity data to be shared with your healthplan provider?", #1
    "Allow activity data to be shared with partners", #2
    "Allow vitals to be shared with your healthcare provider?", #3
    "Allow vitals to be shared with your healthplan provider?", #4
    "Allow vitals to be shared with partners", #5
    "Allow mentalhealth data  to be shared with your healthcare provider?", #6
    "Allow mentalhealth data to be shared with your healthplan provider?", #7
    "Allow mentalhealth data to be shared with partners", #8
    "Allow medicalrecords  to be shared with your healthcare provider?", #9
    "Allow medicalrecords to be shared with your healthplan provider?", #10
    "Allow medicalrecords to be shared with partners", #11

    "Allow anonymized data to be shared for research?", #12
    "Allow identifiable data to be shared for discount programs?", #13
    "Allow identifiable data to be shared for coaching recommendations?" #14
   ]

class ConsentForm(FlaskForm):
    choices = ['No','Yes']
    consent0 = SelectField(consentList[0],choices=choices)
    consent1 = SelectField(consentList[1],choices=choices)
    consent2 = SelectField(consentList[2],choices=choices)
    consent3 = SelectField(consentList[3],choices=choices)
    consent4 = SelectField(consentList[4],choices=choices)
    consent5 = SelectField(consentList[5],choices=choices)
    consent6 = SelectField(consentList[6],choices=choices)
    consent7 = SelectField(consentList[7],choices=choices)
    consent8 = SelectField(consentList[8],choices=choices)
    consent9 = SelectField(consentList[9],choices=choices)
    consent10 = SelectField(consentList[10],choices=choices)
    consent11 = SelectField(consentList[11],choices=choices)
    consent12 = SelectField(consentList[12],choices=choices)
    consent13 = SelectField(consentList[13],choices=choices)
    consent14 = SelectField(consentList[14],choices=choices)

    submit = SubmitField('Submit')


class DataRequestForm(FlaskForm):

    choices_who = ["provider", "healthplan", "partners", "any"]
    choices_purpose = ["coaching", "research", "discount", "any"]
    choices_whatid = ["identifiable", "de-identified", "any"]
    choices_whattype = ["activity", "vitals", "mentalhealth", "medicalrecord", "any"]

    who = SelectField("Are you a provider (eg. a Dr or a Hospital) or a Healthplan (eg. a Aetna or BCBS etc) or a Third Party (eg. a Research Institute etc.)",choices=choices_who)
    purpose = SelectField("what is the purpose of the data access?",choices=choices_purpose)

    whattype = SelectField("What data type do you want to access?",choices=choices_whattype)
    whatid = SelectField("Is the data identifiable or de-identified?",choices=choices_whatid)
    requestingName = StringField('Requesting Organization name')


    submit = SubmitField('Submit')


