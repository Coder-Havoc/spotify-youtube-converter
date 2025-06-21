# youtube_playlist.py

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
import pickle

SCOPES = ["https://www.googleapis.com/auth/youtube"]

class YouTubeClient:
    def __init__(self):
        self.service = self.authenticate()

    def authenticate(self):
        creds = None
        token_path = "credentials/token.json"
        secrets_path = "credentials/client_secrets.json"

        if os.path.exists(token_path):
            with open(token_path, "rb") as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(secrets_path, SCOPES)
                creds = flow.run_local_server(port=0)

            with open(token_path, "wb") as token:
                pickle.dump(creds, token)

        return build("youtube", "v3", credentials=creds)

    def create_playlist(self, title, description=""):
        try:
            request = self.service.playlists().insert(
                part="snippet,status",
                body={
                    "snippet": {
                        "title": title,
                        "description": description
                    },
                    "status": {
                        "privacyStatus": "private"
                    }
                }
            )
            response = request.execute()
            print(f"✅ Created playlist: {title}")
            return response["id"]
        except HttpError as e:
            print(f"❌ An HTTP error occurred: {e}")
            return None

    def add_video_to_playlist(self, playlist_id, video_id):
        try:
            request = self.service.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": playlist_id,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": video_id
                        }
                    }
                }
            )
            request.execute()
            print(f"  ➕ Added video: {video_id}")
        except HttpError as e:
            print(f"❌ Failed to add video {video_id}: {e}")
