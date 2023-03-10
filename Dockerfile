FROM python:3.8-slim

LABEL "com.github.actions.name"="Delete Kubeflow Pipeline from GitHub"
LABEL "com.github.actions.icon"="upload-cloud"
LABEL "com.github.actions.color"="blue"

WORKDIR /app
COPY . . 

RUN  pip install -r requirements.txt

RUN chmod +x entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
