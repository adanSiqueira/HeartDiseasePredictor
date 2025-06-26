#only for manual deploys in google cloud
# #!/bin/bash

# # Stop on errors
# set -e

# # Define variables
# PROJECT_ID="heartdiseasepredictor-464116"
# REGION="us-central1"
# SERVICE_NAME="heart-disease-app"

# # Authenticate (only needed once per session)
# #gcloud auth login
# #gcloud config set project $PROJECT_ID

# # Enable necessary services
# gcloud services enable run.googleapis.com
# gcloud services enable artifactregistry.googleapis.com

# # Deploy to Cloud Run from source
# gcloud run deploy $SERVICE_NAME \
#   --source . \
#   --region $REGION \
#   --platform managed \
#   --allow-unauthenticated \
#   --port 8050
