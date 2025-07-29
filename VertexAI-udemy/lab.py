from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
api_key_path = "ai-doc-processing-463120-13d2e83f8b73.json"
project_id = "ai-doc-processing-463120"
import os
base_dir = os.path.dirname(__file__)
api_key_path = os.path.join(base_dir, 'ai-doc-processing-463120-13d2e83f8b73.json')
credentials = Credentials.from_service_account_file(api_key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"])

region="us-central1"
import vertexai
vertexai.init(credentials=credentials, project=project_id, location=region)
modelname="gemini-2.0-flash-001"
from vertexai.generative_models import GenerativeModel
model=GenerativeModel(modelname)
response = model.generate_content("capital city of china")
print(response.text)
from vertexai.generative_models import GenerationConfig
generation_config = GenerationConfig(
    temperature=0.7,
    top_p=0.9,
    candidate_count=1,
    max_output_tokens=1024,
    stop_sequences=["\n"],
)