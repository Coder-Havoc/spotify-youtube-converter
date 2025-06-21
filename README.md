# Spotify-to-YouTube Playlist Converter

Easily convert your Spotify playlist into a private YouTube playlist in just a few steps!

## 🚀 Features

* Fetches all track names from a Spotify playlist
* Searches YouTube for the best matching video for each track
* Automatically creates a YouTube playlist
* Adds matched videos to the playlist
* Outputs a shareable YouTube playlist link

## 🔧 Setup

### 1. Clone the Repository

```bash
$ git clone https://github.com/your-username/spotify-youtube-converter.git
$ cd spotify-youtube-converter
```

### 2. Install Dependencies

```bash
$ pip install -r requirements.txt
```

### 3. Add Spotify API Credentials

Create a `.env` file in the root directory:

```
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
```

### 4. Add YouTube API Credentials

Place your `client_secrets.json` (from Google Cloud Console) in the `credentials/` directory.
It should look like this:

```json
{
  "installed": {
    "client_id": "...",
    "client_secret": "...",
    "redirect_uris": ["http://localhost"]
  }
}
```

## ▶️ Running the Project

```bash
$ python main.py
```

Follow the prompts:

* Paste your Spotify playlist URL
* Enter a name for the YouTube playlist
* Authenticate Google account (first time only)

## 📁 Project Structure

```
spotify-youtube-converter/
├── main.py
├── spotify/
│   └── spotify_client.py
├── youtube/
│   ├── youtube_playlist.py
│   └── youtube_searcher.py
├── utils/
│   └── clean_title.py
├── credentials/
│   └── client_secrets.json
│   └── token.json (auto-generated)
└── .env
```

## ✅ Output

A working YouTube playlist link is shown at the end:

```
🔗 View your playlist: https://www.youtube.com/playlist?list=...
```

## 🧠 Notes

* Only public Spotify playlists are supported.
* The YouTube playlist is created as **private**.
* You can manually make the playlist public from your YouTube account.

## 📜 License

MIT License

---

Built with ❤️ by Bhavya Shrivastava
