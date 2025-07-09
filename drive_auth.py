# drive_auth.py
from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

# Scope to read files
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Path to the JSON key you downloaded
# CORRECTED: Default path now points to the root directory
KEYFILE = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "credentialsdrive-sa.json")

def get_drive_service():
    """
    Returns an authorized Google Drive service client.
    """
    creds = service_account.Credentials.from_service_account_file(
        KEYFILE, scopes=SCOPES
    )
    service = build('drive', 'v3', credentials=creds)
    return service