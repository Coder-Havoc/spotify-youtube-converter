# 🎵 Spotify → YouTube Playlist Converter

[![MIT License](https://img.shields.io/github/license/Coder-Havoc/spotify-youtube-converter)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/Coder-Havoc/spotify-youtube-converter)](https://github.com/Coder-Havoc/spotify-youtube-converter/commits/main)
[![Stars](https://img.shields.io/github/stars/Coder-Havoc/spotify-youtube-converter?style=social)](https://github.com/Coder-Havoc/spotify-youtube-converter/stargazers)

Convert your favorite Spotify playlists into YouTube playlists effortlessly using the YouTube Data API and Spotipy.  
This tool allows you to transfer songs while maintaining titles, creates a new YouTube playlist, and adds the best-matching videos automatically.

---

## 🚀 Features

- ✅ Convert any public Spotify playlist to a YouTube playlist 
- 🔄 Convert YouTube → Spotify playlists (coming soon) 
- 🔍 Matches song titles intelligently via YouTube search  
- 🧠 Cleans song names to improve search accuracy  
- 📧 Uses OAuth to securely authenticate your Google account  
- 📦 CLI-based, lightweight, and fully open-source  

---

## 🧰 Requirements

- Python 3.8+
- Google YouTube Data API OAuth credentials (`client_secrets.json`)
- Spotify API credentials (via [Spotipy](https://spotipy.readthedocs.io))

---

## 🛠️ Installation

```bash
git clone https://github.com/Coder-Havoc/spotify-youtube-converter.git
cd spotify-youtube-converter
pip install -r requirements.txt
```

👉 Place your `client_secrets.json` file inside the `credentials/` folder.

---

## 📌 Usage

▶️ Spotify → YouTube (Working)

  python main.py

Follow the prompts to:
- Paste a Spotify playlist link
- Name your new YouTube playlist
- Authenticate your Google account (browser popup)
- Let the tool do the rest 🎉

🔄 YouTube → Spotify (Coming Soon)

This feature will:
- Parse a YouTube playlist URL
- Extract and clean video titles
- Search for matching tracks on Spotify
- Create and populate a Spotify playlist via API

Stay tuned!


## 🗂️ Folder Structure

```
spotify-youtube-converter/
│
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
├── credentials/
│   └── (place your client_secrets.json here)
├── utils/
│   └── clean_title.py
├── youtube/
│   └── youtube_searcher.py
```

---

## 🛡 License

This project is licensed under the [MIT License](LICENSE).

---

## ✨ Author

**Bhavya Shrivastava**  
📍 Vidisha, MP  
📧 bhavya9755@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/bhavya-shrivastava0107/)  
🔗 [GitHub](https://github.com/Coder-Havoc)