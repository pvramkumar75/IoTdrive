# drive_utils.py
import io
import pandas as pd
from googleapiclient.http import MediaIoBaseDownload
from drive_auth import get_drive_service

def list_csv_files_in_folder(folder_id: str):
    """
    Returns a list of dicts {'id': ..., 'name': ...} for each CSV in the folder.
    """
    service = get_drive_service()
    query = f"'{folder_id}' in parents and mimeType='text/csv'"
    resp = service.files().list(q=query, fields="files(id,name)").execute()
    return resp.get('files', [])

def download_csv_to_df(file_id: str) -> pd.DataFrame:
    """
    Downloads the CSV file by its Drive file ID and returns a pandas DataFrame.
    """
    service = get_drive_service()
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    fh.seek(0)
    return pd.read_csv(fh)
