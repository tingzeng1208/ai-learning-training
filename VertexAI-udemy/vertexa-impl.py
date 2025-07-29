from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
api_key_path = "ai-doc-processing-463120-13d2e83f8b73.json"
project_id = "ai-doc-processing-463120"
import os
import vertexai
credentials = Credentials.from_service_account_file(api_key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"])
vertexai.init(credentials=credentials, project=project_id, location=region)
modelname="gemini-2.0-flash-001"
from vertexai.generative_models import GenerativeModel

model=GenerativeModel(modelname)
response = model.generate_content("capital city of china")
print(response.text)

generation_config = {
    "temperature": 0.2,
    "max_output_tokens": 1024,
    "top_p": 0.8,
    "top_k": 40,
    "stop_sequences": ["\n"],
    "candidate_count": 1, # Number of candidate responses to generate
    "safety_settings": [
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": 0.5
        }
    ]
}