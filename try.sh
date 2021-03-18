curl -X POST \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    -H "Content-Type: application/consent+json; charset=utf-8" \
    --data "{
       'user_id': 'abc@gmail.com',
       'user_signature' : {
         'user_id': 'abc@gmail.com',
       },      
       'consent_content_version': 'v1',
       'metadata': {'client': 'mobile'}
    }" \
"https://healthcare.googleapis.com/v1beta1/projects/smede-276406/locations/us-central1/datasets/consentdemo/consentStores/consent/consentArtifacts"
