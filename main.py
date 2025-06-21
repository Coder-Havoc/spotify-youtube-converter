# main.py

from spotify.spotify_client import get_spotify_tracks
from youtube.youtube_api_searcher import search_youtube_video
from youtube.youtube_playlist import YouTubeClient
from utils.clean_title import clean_title

def main():
    print(">>")
    playlist_url = input("Enter the Spotify playlist URL: ").strip()
    playlist_name = input("Enter a name for your YouTube playlist: ").strip()

    print("\n🔍 Fetching songs from Spotify...")
    songs = get_spotify_tracks(playlist_url)

    cleaned_titles = [clean_title(song) for song in songs]

    print("\n🔍 Matching YouTube Links:")
    video_ids = []
    for i, title in enumerate(cleaned_titles, 1):
        video_id = search_youtube_video(title)
        if video_id:
            print(f"{i}. {title} → https://www.youtube.com/watch?v={video_id}")
            video_ids.append(video_id)
        else:
            print(f"{i}. {title} → ❌ Not found")

    print("\n🚀 Creating YouTube playlist...")
    yt_client = YouTubeClient()
    playlist_id = yt_client.create_playlist(playlist_name)

    if not playlist_id:
        print("❌ Could not create playlist. Exiting.")
        return

    print(f"\n📥 Adding videos to playlist '{playlist_name}'...")
    for vid in video_ids:
        yt_client.add_video_to_playlist(playlist_id, vid)

    print("\n✅ All done!")
    print(f"🔗 View your playlist: https://www.youtube.com/playlist?list={playlist_id}")

if __name__ == "__main__":
    main()
