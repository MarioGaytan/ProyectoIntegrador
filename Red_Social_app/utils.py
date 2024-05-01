import secrets
from .models import APICredential

def generate_api_key():
    return secrets.token_urlsafe(32)

def create_api_key():
    key = generate_api_key()
    api_credential = APICredential.objects.create(key=key)
    return api_credential