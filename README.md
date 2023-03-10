# Kubeflow Pipelines Delete action

GitHub Actions for deleting pipelines on GCP/GKE's Kubeflow instances.

This action works in combination of: https://github.com/albert-cintas-pot/kubeflow-compile-deploy

## Workflow Configuration
### Parameters

The action has been set up with only two input parameters:

| key                       | required | description                                                                                                                  | 
| :------------------------ | -------- | ---------------------------------------------------------------------------------------------------------------------------- | 
| PULL_REQUEST_NUMBER       | True     | The number of the Pull Request associated to the pipelines that should be deleted. |

Default pipeline name will be the same as the filename of the pipeline. IMPORTANT: Pipeline function should also have the same name.


### Authentication secrets and parameters

We use the Kubeflow SDK to authenticate to the Kubeflow instance as stated in the official docs: https://www.kubeflow.org/docs/distributions/gke/pipelines/authentication-sdk/#connecting-to-kubeflow-pipelines-in-a-full-kubeflow-deployment

Note that OTHER_CLIENT_ID credentials should be initialized locally before using them in the action, to get the KFP credentials JSON.

The following secrets are mandatory for proper auth:

| key                       | description                                                                                                                                                                      | 
| :------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | 
| KUBEFLOW_URL              | The url endpoint where your Kubeflow UI is running.                                                                                                                              | 
| CLIENT_ID                 | The client ID used by Identity-Aware Proxy at the time of deploying Kubeflow.                                                                                                    | 
| OTHER_CLIENT_ID           | The client ID used to obtain the auth codes and refresh tokens (https://cloud.google.com/iap/docs/authentication-howto#authenticating_from_a_desktop_app).                       | 
| OTHER_CLIENT_SECRET       | The client secret used to obtain the auth codes and refresh tokens.                                                                                                              |
| KFP_CREDENTIALS_JSON      | The JSON file containing the credentials generated the first time you init the SDK client using above credentials (stored at: $HOME/.config/kfp/credentials.json.                |

### Usage

#### Define Workflow for single pipeline

```yaml
name: Delete Kubeflow pipeline
on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout files in repo
      uses: actions/checkout@v2

    - name: Delete a pipeline
      uses: albert-cintas-pot/kubeflow-delete-pipeline@main
      env:
        KUBEFLOW_URL: ${{ secrets.KUBEFLOW_URL }} # Required for AUTH
        KFP_CREDENTIALS_JSON: ${{ secrets.KFP_CREDENTIALS_JSON }} # Required for AUTH
        CLIENT_ID: ${{ secrets.CLIENT_ID }} # Required for AUTH
        OTHER_CLIENT_ID: ${{ secrets.OTHER_CLIENT_ID }} # Required for AUTH
        OTHER_CLIENT_SECRET: ${{ secrets.OTHER_CLIENT_SECRET }} # Required for AUTH
        PULL_REQUEST_NUMBER: ${{ github.event.number }} # Required

```

### Docker image creation

A github action has been setup in this repository to create a Docker image with KFP SDK installed for use in this action. This shaves 30 seconds of time each time a Kubeflow pipeline is deleted.
