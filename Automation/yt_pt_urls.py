from pytube import Playlist
import os
import sys
import pathlib

# extracted urls from a YouTube playlist to be saved into a txt file the path url with name of palylist

def get_playlist_videos_urls(playlist_url):
    playlist = Playlist(playlist_url)
    return [video.watch_url for video in playlist.videos]

def save_playlist_urls_to_txt(playlist_url, output_file):
    urls = get_playlist_videos_urls(playlist_url)
    with open(output_file, 'w') as f:
        for url in urls:
            f.write(url + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <playlist_url> <output_file>")
        sys.exit(1)

    playlist_url = sys.argv[1]
    output_file = sys.argv[2]

    save_playlist_urls_to_txt(playlist_url, output_file)
    print(f"Playlist URLs saved to {output_file}")
