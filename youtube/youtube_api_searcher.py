# youtube/youtube_api_searcher.py

import yt_dlp

def search_youtube_video(query):
    try:
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
            'format': 'bestaudio/best',
            'default_search': 'ytsearch1',
            'noplaylist': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            if 'entries' in info and len(info['entries']) > 0:
                return info['entries'][0]['id']
            return None
    except Exception as e:
        print(f"❌ YouTube search failed for '{query}': {e}")
        return None
