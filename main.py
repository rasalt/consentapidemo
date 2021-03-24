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


# Reference link: https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Flask_Blog/02-Templates

import logging
import os

#import google.auth
from google.auth import app_engine
from google.auth.transport import requests

from flask import Flask, render_template, url_for, redirect, flash, session
from forms import LoginForm, ConsentForm, DataRequestForm
import flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '343sfre'
posts = [
    {
        'author': 'Mary Higgins',
        'title': 'The cradle will fall'
    },
    {
        'author': 'Agatha Christie',
        'title': 'And then there were none'
    }
]

useremail = ""

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Welcome back  {form.email.data} !', 'success')
        useremail = form.email.data
        session['user'] = useremail
        return redirect(url_for('consent'))
    return render_template('login.html', title='Login', form=form)



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
    "Allow medicalrecord  to be shared with your healthcare provider?", #9
    "Allow medicalrecord to be shared with your healthplan provider?", #10
    "Allow medicalrecord to be shared with partners", #11

    "Allow anonymized data to be shared for research?", #12
    "Allow identifiable data to be shared for discount programs?", #13
    "Allow identifiable data to be shared for coaching recommendations?" #14
   ]

@app.route("/consent", methods=['GET','POST'])
def consent():
    userconsentdata = ({})
    userconsentdata["activity"] = {}
    userconsentdata["vitals"] = {}
    userconsentdata["medicalrecord"] = {}
    userconsentdata["mentalhealth"] = {}
    userconsentdata["de-identified"] = {}
    userconsentdata["identifiable"] = {}
    form = ConsentForm()
#    if form.validate_on_submit():
#        flash(f'Your consent has been noted and we will send you a copy of this information for your records', 'success')
    if (flask.request.method =='POST'):
        print("POST")
        textToDisplay = "Your Consent Summary - "+ "<br/>"+ "<br/>"+ "<br/>"
        textToDisplay = textToDisplay + consentList[0] + "-" + form.consent0.data  + "<br/>"
        textToDisplay = textToDisplay + consentList[1] + "-" + form.consent1.data  + "<br/>"
        textToDisplay = textToDisplay + consentList[2] + "-" + form.consent2.data  + "<br/>"
        textToDisplay = textToDisplay + consentList[3] + "-" + form.consent3.data  + "<br/>"
        textToDisplay = textToDisplay + consentList[4] + "-" + form.consent4.data  + "<br/>"
        textToDisplay = textToDisplay + consentList[5] + "-" + form.consent5.data  + "<br/>"
        textToDisplay = textToDisplay + consentList[6] + "-" + form.consent6.data  + "<br/>"
        textToDisplay = textToDisplay + consentList[7] + "-" + form.consent7.data  + "<br/>"
        textToDisplay = textToDisplay + consentList[8] + "-" + form.consent8.data  + "<br/>"
        textToDisplay = textToDisplay + consentList[9] + "-" + form.consent9.data  + "<br/>"
        textToDisplay = textToDisplay + consentList[10] + "-" + form.consent10.data  + "<br/>"
        textToDisplay = textToDisplay + consentList[11] + "-" + form.consent11.data  + "<br/>"
        textToDisplay = textToDisplay + consentList[12] + "-" + form.consent12.data  + "<br/>"
        textToDisplay = textToDisplay + consentList[13] + "-" + form.consent13.data  + "<br/>"
        textToDisplay = textToDisplay + consentList[14] + "-" + form.consent14.data  + "<br/>"
        textToDisplay = textToDisplay + "<br/>" + "<br/>"+ "<br/>"
        textToDisplay = textToDisplay + "A copy of your consent is sent to your email address for your future reference" + "<br/>"
        textToDisplay = textToDisplay + "Please remember you can change your consent at any time" + "<br/>"
        textToDisplay = textToDisplay + "Goodbye for now" + "<br/>"

        if (form.consent0.data == "Yes"): userconsentdata["activity"]["provider"] = True
        else: userconsentdata["activity"]["provider"] = False

        if (form.consent1.data == "Yes"): userconsentdata["activity"]["healthplan"] = True
        else: userconsentdata["activity"]["healthplan"] = False

        if (form.consent2.data == "Yes"): userconsentdata["activity"]["partners"] = True
        else: userconsentdata["activity"]["partners"] = False
#
        if (form.consent3.data == "Yes"):
            userconsentdata["vitals"]["provider"] = True
        else:
            userconsentdata["vitals"]["provider"] = False

        if (form.consent4.data == "Yes"):
            userconsentdata["vitals"]["healthplan"] = True
        else:
            userconsentdata["vitals"]["healthplan"] = False

        if (form.consent5.data == "Yes"):
            userconsentdata["vitals"]["partners"] = True
        else:
            userconsentdata["vitals"]["partners"] = False

#
        if (form.consent6.data == "Yes"):
            userconsentdata["mentalhealth"]["provider"] = True
        else:
            userconsentdata["mentalhealth"]["provider"] = False

        if (form.consent7.data == "Yes"):
            userconsentdata["mentalhealth"]["healthplan"] = True
        else:
            userconsentdata["mentalhealth"]["healthplan"] = False

        if (form.consent8.data == "Yes"):
            userconsentdata["mentalhealth"]["partners"] = True
        else:
            userconsentdata["mentalhealth"]["partners"] = False
    #
        if (form.consent6.data == "Yes"):
             userconsentdata["medicalrecord"]["provider"] = True
        else:
            userconsentdata["medicalrecord"]["provider"] = False

        if (form.consent7.data == "Yes"):
            userconsentdata["medicalrecord"]["healthplan"] = True
        else:
            userconsentdata["medicalrecord"]["healthplan"] = False

        if (form.consent8.data == "Yes"):
            userconsentdata["medicalrecord"]["partners"] = True
        else:
            userconsentdata["medicalrecord"]["partners"] = False

        if (form.consent12.data == "Yes"):
            userconsentdata["de-identified"]["research"] = True
        else:
            userconsentdata["de-identified"]["research"] = False

        if (form.consent13.data == "Yes"):
            userconsentdata["identifiable"]["discount"] = True
        else:
            userconsentdata["identifiable"]["discount"] = False

        if (form.consent14.data == "Yes"):
            userconsentdata["identifiable"]["coaching"] = True
        else:
            userconsentdata["identifiable"]["coaching"] = False

        print(userconsentdata)
        updateConsentData(session['user'], userconsentdata)

        return(textToDisplay)
#        return redirect(url_for('consentAck'))
    return render_template('consent.html', title='consent', form=form)

@app.route("/datarequestAll", methods=['GET','POST'])
def datarequestAll():

    form = DataRequestForm()
    print("fsfndfsk")
    if (flask.request.method =='POST'):
        print("POST")
        print("45464")

        textToDisplay = "Request for data by a " + form.who.data + ". For the purpose of " + form.whatid.data + ". Requesting Organization is " + form.requestingName.data + "<br/>"+ "<br/>"+ "<br/> "

        # Lets get all the data that this user can access
        mappingarray = []
        data = {}

        data['gcs_destination'] = {}
        data['gcs_destination']['uri_prefix'] = 'gs://smede-sandbox/consent/xyz'
        data['resource_attributes'] = {}

        if (form.whatid.data != "any"):
            data['resource_attributes']['data_identifiable'] = form.whatid.data
        if (form.whattype.data != "any"):
            data['resource_attributes']['data_type'] = form.whattype.data

        data['request_attributes'] = {}

        if (form.who.data != "any"):
            data['request_attributes']['requester_type'] = form.who.data
        if (form.purpose.data != "any"):
            data['request_attributes']['requester_identity'] = form.purpose.data


        print(data)
        request = svc.projects().locations().datasets().consentStores().queryAccessibleData(
            consentStore = consent_parent, body=data)
        response = request.execute()
        print (response)
        print ("------------------------------------------")
        # Read the destination output file
        session['mappingarray'] = getMapping()
        print(session)
        print("REDIRECTING NOW")
        #return(mappingarray)
      #  return redirect(url_for('resultall'))
        print(session['mappingarray'])
        #session["mappingarray"]= [{"value": "A", "phys": "PHYS"}, {"value": "B", "phys": "PHYS"}]
        return render_template('dataresult.html', data=session['mappingarray'])
    #        return redirect(url_for('consentAck'))
    return render_template('datarequestAll.html', title='datarequest', form=form)


def download_blob(bucket_name, source_blob_name, destination_file_name):
     """Downloads a blob from the bucket."""
     # bucket_name = "your-bucket-name"
     # source_blob_name = "storage-object-name"
     # destination_file_name = "local/path/to/file"
     import google.cloud.storage as storage
     storage_client = storage.Client()
     bucket = storage_client.bucket(bucket_name)

     # Construct a client side representation of a blob.
     # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
     # any content from Google Cloud Storage. As we don't need additional data,
     # using `Bucket.blob` is preferred here.
     blob = bucket.blob(source_blob_name)
     blob.download_to_filename(destination_file_name)

     print(
         "Blob {} downloaded to {}.".format(
          source_blob_name, destination_file_name)
      )

def getMapping():
    from google.cloud import storage

    # Read GCS file
    storage_client = storage.Client.from_service_account_json("/Users/rkharwar/sandbox/uhg/smede-276406-764778147a0d.json")

    # get bucket with name
    bucket = storage_client.get_bucket('smede-sandbox')
    # get bucket data as blob
    blob = bucket.get_blob("consent/xyz/consent_xyz_query-accessible-data-result-11744410558303043585.txt")
    # convert to string
    blob.download_to_filename('consentdata.txt')

    file1 = open('consentdata.txt', 'r')
    lines = file1.readlines()
    file1.close()

    # Read firestore
    from google.cloud import firestore
    db = firestore.Client.from_service_account_json("/Users/rkharwar/sandbox/uhg/smede-276406-764778147a0d.json")

    count = 0
    mappinginfo = []
    print(lines)
    # Strips the newline character
    data = {}
    for line in lines:
        count += 1
        logicalid = line.strip()
        data['logicalid'] = logicalid
        print("getMapping, logicalid is {}".format(logicalid))
        dataphys = {}
        doc_ref = db.collection(u'consentdatamapping').document(logicalid)
        doc = doc_ref.get()
        if doc.exists:
            print(f'Document data: {doc.to_dict()}')
        else:
            print(u'No such document!')
        data['physicalmapping'] =   doc.to_dict()
        data['physicalmapping'] =   json.dumps(data['physicalmapping'])

        mappinginfo.append(data)


    print(mappinginfo)

    return mappinginfo

    print("Line{}: {}".format(count, line.strip()))
#url     = 'http://example.tld'
#payload = { 'key' : 'val' }
#headers = {}
#res = requests.post(url, data=payload, headers=headers)

#    "activity",
#    "vitals",
#    "mentalhealth",
#    "medicalrecord"

#    "provider",
#    "healthplan",
#    "partners"

PROJECT_ID="smede-276406"
LOCATION="us-central1"
DATASET="consentdemo"
CONSENTSTORE="consent"
CONSENT_BASE_URL='https://healthcare.googleapis.com/v1'

def get_session():
    """Creates an authorized Requests Session."""

    # Pass in the credentials and project ID. If none supplied, get them
    # from the environment.
    from google.oauth2 import service_account

    SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
    SERVICE_ACCOUNT_FILE = "/Users/rkharwar/sandbox/uhg/smede-276406-764778147a0d.json"

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    import googleapiclient.discovery

    service = googleapiclient.discovery.build('healthcare', 'v1beta1', credentials=credentials)
    consent_parent = "projects/{}/locations/{}/datasets/{}/consentStores/{}".format(
        PROJECT_ID, LOCATION, DATASET,CONSENTSTORE
    )
    return service, consent_parent

def setup_consentservice():
   global svc
   global consent_parent
   svc, consent_parent = get_session()

def destroy_consentservice():
    print("will close")
    return

def list_consentAttributes():
    print("Listing Consent Attributes")
    request = svc.projects().locations().datasets().consentStores().attributeDefinitions().list(
        parent=consent_parent)

    response = request.execute()
    print(json.dumps(
      response,
      sort_keys=True,
      indent=2
    ))
    print("------------------------------------------------------------------------------------------------")

def list_consents():
    print("Listing Consents")
    request = svc.projects().locations().datasets().consentStores().consents().list(
        parent=consent_parent)

    response = request.execute()
    print(json.dumps(
      response,
      sort_keys=True,
      indent=2
    ))
    print("------------------------------------------------------------------------------------------------")

# Variables

resource_attr = {
    "data_identifiable": ["identifiable", "de-identified"],
    "data_type": ["activity", "vitals", "mentalhealth", "medicalrecord"]
}
request_attr = {
    "requester_type": ["provider", "healthplan", "partners"],
    "purpose": ["coaching", "research", "discount"]
}

def createDataMapping(logicalid):
    from google.cloud import firestore
    import random
    print("logical id is {}".format(logicalid))
    resource="gs://"
    comment="this is crazy"
    # Add a new document
    db = firestore.Client.from_service_account_json("/Users/rkharwar/sandbox/uhg/smede-276406-764778147a0d.json")
    id = random.randint(1,10000)
    if ("activity" in logicalid):
        if (",id" in logicalid):
            resource = "bt.activitydata"
            comment = "Identifiable Activity data in BigTable"
        else:
            resource = "btdeid.activitydata"
            comment = "De-Identifiable Activity data in BigTable"

    if ("vitals" in logicalid):
        if (",id" in logicalid):
            resource = "bt.vitalsdata"
            comment = "Identifiable Vitals data in BigTable"
        else:
            resource = "btdeid.vitalsdata"
            comment = "De-Identifiable Vitals data in BigTable"

    if ("medicalrecord" in logicalid):
        if (",id" in logicalid):
            resource = "BASE_URL/projects/demo/us-central1/datasets/demodataset/fhirStores/FHIRR4/Patient"
            comment = "Identifiable claims data in FHIR Store"
        else:
            resource = "BASE_URL/projects/demo/us-central1/datasets/deiddemodataset/fhirStores/FHIRR4/Patient"
            comment = "De-Identifiable claims data in FHIR Store"

    if ("mentalhealth" in logicalid):
        if (",id" in logicalid):
            resource = "PROJECT_ID.bigquerymentalhealth"
            comment = "Identifiable mental health data in BigQuery"
        else:
            resource = "PROJECT_ID.deidbigquerymentalhealth"
            comment = "De-Identifiable mental health data in BigQuery"

    data = {}

    data['resource'] = resource
    data['id'] = id
    data['comment'] = comment
    #activity data in BigTable
    #claims data in FHIR store
    #mentalhealth in BQ
    #vitals in BigTable


    # Add a new doc in collection 'cities' with ID 'LA'
    db.collection(u'consentdatamapping').document(logicalid).set(data)



import json
#@app.route("/")
def updateConsentData(useremail, userconsentdata):

    # Make an authenticated API request
    # #headers = {"Content-Type": "application/consent+json;charset=utf-8"}

    print("Creating Consent Artifact")
    #useremail = "test_user_1"

    #Create consent artifact payload
    data = {}
    data['user_id'] = useremail
    data['user_signature'] = {} 
    data['user_signature']['user_id'] = useremail
    data['consent_content_version'] = 'v1'
    data['metadata'] = {} 
    data['metadata']['client'] = 'mobile' 
    # Documentation
    #https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1beta1.projects.locations.datasets.consentStores.consentArtifacts.html#create

    print(json.dumps(data, indent = 4))
    
    request = svc.projects().locations().datasets().consentStores().consentArtifacts().create(
        parent=consent_parent,body=data)

    print("Consent Artifact for {}".format(useremail))
    response = request.execute()
    print(json.dumps(
      response,
      sort_keys=True,
      indent=2
    ))
    artifact = response["name"]
    print("------------------------")

    print("Create Consent  for patient data type {}".format(useremail))
    print("Creating consents - userdata mapping as well as the consent itself")
    print("User {}, consent data is {}".format(useremail,userconsentdata))
    # Check if the user exists in the system. If the user exists in the system, then leave the data mappings in tact but
    # update the consent artifact and consent itself
    print("Checking if the user exists in the system")
    filtertext = "user_id="+"\"" + session["user"]+ "\""
    # filtertext = "user_id="+"\"test_user_100\""


    print(filtertext)
    request = svc.projects().locations().datasets().consentStores().consents().list(parent=consent_parent,filter=filtertext)    #, )
    response = request.execute()


    if (len(response) == 0): # This is a new user.
        print("New User ")

        # userDataMapping
        for a in ["activity", "vitals", "mentalhealth", "medicalrecord"]:

            # Create the userDataMapping
            # Use opaque id and expect another application to take care of transalting the opaqueid to physical resource location
            # the format of the opaque id is "useremail,"noun(activity/Vitals),physresource(bq/csv/fhir),id(table/csv
            # Create the payload
            # Create 2 version per data type
            ## Deidentified Data ID
            data = {}
            attr = {}
            data["user_id"] = useremail
            data["data_id"] = useremail +  "," + a + "," + "deid"
            data["resource_attributes"] = []
            attr["attribute_definition_id"] = "data_identifiable"
            attr["values"] = ["de-identified"]
            data["resource_attributes"].append(attr)
            print("Creating user data mapping for user {} datatype {} and de-id".format(useremail,a))
            print(json.dumps(data, indent=4))
            request = svc.projects().locations().datasets().consentStores().userDataMappings().create(
                parent=consent_parent,body=data)

            response = request.execute()
            print(json.dumps(
              response,
              sort_keys=True,
              indent=2
            ))
            createDataMapping(data["data_id"])

            ## Identifiable Data ID
            data = {}
            attr = {}
            data["user_id"] = useremail
            data["data_id"] = useremail +  "," + a + "," + "id"
            data["resource_attributes"] = []
            attr["attribute_definition_id"] = "data_identifiable"
            attr["values"] = ["identifiable"]
            data["resource_attributes"].append(attr)
            print("Creating user data mapping for datatype {} and id".format(a))
            print(json.dumps(data, indent=4))
            request = svc.projects().locations().datasets().consentStores().userDataMappings().create(
                parent=consent_parent,body=data)

            response = request.execute()
            print(json.dumps(
              response,
              sort_keys=True,
              indent=2
            ))
            createDataMapping(data["data_id"])

    # Existing user
    #Consent Creating
    print("Existing User ")

    for a in ["activity", "vitals", "mentalhealth", "medicalrecord"]:

        data = {}
        activityBy = []
        for b in ["provider", "healthplan", "partners"]:
            if userconsentdata[a][b] == True:
                activityBy.append(b)

        data["user_id"] = useremail
        data["policies"] = []
        obj0 = {}
        obj0["resource_attributes"] = []
        obj = {}
        obj["attribute_definition_id"] = "data_type"
        obj["values"] = []
        obj["values"].append(a)
        obj0["resource_attributes"].append(obj)
        obj0["authorization_rule"] = {}
        obj0["authorization_rule"]["expression"] = "requester_type in {}".format(str(activityBy))
        data["policies"].append(obj0)

        data["consent_artifact"]= artifact

        print(json.dumps(data, indent=4))
        request = svc.projects().locations().datasets().consentStores().consents().create(
            parent=consent_parent,body=data)

        response = request.execute()
        print(json.dumps(
          response,
          sort_keys=True,
          indent=2
         ))
        print("------------------------")

        print("Create Consent  for idenitifable  data  {}".format(useremail))

        data = {}
        #Create the payload
        accessBy = []
        if (userconsentdata["identifiable"]["discount"] == True):
            accessBy.append("discount")
        if (userconsentdata["identifiable"]["coaching"] == True):
            accessBy.append("coaching")
        data['user_id'] = useremail
        data['policies'] = []
        obj0 = {}
        obj0['resource_attributes'] = []
        obj = {}
        obj['attribute_definition_id'] = 'data_identifiable'
        obj['values'] = []
        obj['values'].append('identifiable')
        obj0['resource_attributes'].append(obj)
        obj0['authorization_rule'] = {}
        obj0['authorization_rule']['expression'] = 'requester_identity in {}'.format(str(accessBy))
        data['policies'].append(obj0)

        data['consent_artifact']= artifact

        print(json.dumps(data, indent=4))
        request = svc.projects().locations().datasets().consentStores().consents().create(
            parent=consent_parent,body=data)

        response = request.execute()
        print(json.dumps(
          response,
          sort_keys=True,
          indent=2
        ))
        print("------------------------")

        print("Create Consent  for de-identified  data  {}".format(useremail))

        data = {}
        #Create the payload
        accessBy = []
        if (userconsentdata["de-identified"]["research"] == True):
            accessBy.append("research")

        data['user_id'] = useremail
        data['policies'] = []
        obj0 = {}
        obj0['resource_attributes'] = []
        obj = {}
        obj['attribute_definition_id'] = 'data_identifiable'
        obj['values'] = []
        obj['values'].append('de-identified')
        obj0['resource_attributes'].append(obj)
        obj0['authorization_rule'] = {}
        obj0['authorization_rule']['expression'] = 'requester_identity in {}'.format(str(accessBy))
        data['policies'].append(obj0)

        data['consent_artifact']= artifact

        print(json.dumps(data, indent=4))
        request = svc.projects().locations().datasets().consentStores().consents().create(
            parent=consent_parent,body=data)

        response = request.execute()
        print(json.dumps(
          response,
          sort_keys=True,
          indent=2
        ))
        print("------------------------")
    return  



if __name__ == '__main__':
    setup_consentservice()
    list_consentAttributes()
    list_consents()
    app.run(debug=True)


