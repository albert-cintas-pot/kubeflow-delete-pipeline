import kfp
import logging
import sys
import os
import re

# Setting logging level
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# Set vars
host = os.getenv("KUBEFLOW_URL")
client_id = os.getenv("CLIENT_ID")
other_client_id = os.getenv("OTHER_CLIENT_ID")
other_client_secret = os.getenv("OTHER_CLIENT_SECRET")
pull_request_number = os.getenv("PULL_REQUEST_NUMBER")

# Authenticate session client
client = kfp.Client(host=host, 
    client_id=client_id, 
    other_client_id=other_client_id, 
    other_client_secret=other_client_secret
)

# Get all pipelines in current environment
get_pipelines = client.list_pipelines().pipelines

# If pipeline contains Pull Request number, delete it
for pipeline in get_pipelines:
    name = pipeline.name
    if re.search(pull_request_number, name):
        pipeline_id = client.get_pipeline_id(name)
        client.delete_pipeline(pipeline_id)
        logging.info("Pipeline '" + name + "' has been deleted.")
