
"""from huggingface_hub import InferenceClient

client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",  #  mistralai/Mistral-7B-Instruct-v0.2
    token="YOUR_HUGGINGFACE_TOKEN"  
)

def generate_answer(prompt):
    response = client.chat_completion(
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )
    return response.choices[0].message.content"""
    
    
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables
load_dotenv()

# Read token from .env
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

client = InferenceClient(
    model="Qwen/Qwen2.5-72B-Instruct",
    token=HF_TOKEN
)

def generate_answer(prompt):

    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )

    return response.choices[0].message.content
    
    
