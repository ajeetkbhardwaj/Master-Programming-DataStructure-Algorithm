# First, you need to install the required libraries.
# If you haven't already, run:
# pip install langchain-community youtube-transcript-api

import os
import sys
from langchain_community.document_loaders import YoutubeLoader
from youtube_transcript_api._errors import NoTranscriptFound, VideoUnavailable
from urllib.error import HTTPError

def process_urls_from_file(input_file_path, output_folder):
    """
    Reads a list of YouTube video URLs from a file, extracts their
    transcripts, and saves each transcript to a separate file.

    Args:
        input_file_path (str): The path to the file containing the URLs.
        output_folder (str): The name of the folder to save the transcripts.
    """
    # Create the output folder if it doesn't exist.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created folder: {output_folder}")

    # Read the URLs from the input file.
    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            video_urls = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.", file=sys.stderr)
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}", file=sys.stderr)
        return

    # Loop through each URL and process it.
    for i, url in enumerate(video_urls, 1):
        try:
            print(f"[{i}/{len(video_urls)}] Processing URL: {url}")
            
            # Initialize the YoutubeLoader. We add video info to get the title.
            loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
            
            # Load the transcript as a Document object.
            docs = loader.load()

            if docs:
                transcript_text = docs[0].page_content
                # Use a simple numerical filename for simplicity.
                output_filename = f"video_{i}.txt"
                output_filepath = os.path.join(output_folder, output_filename)

                # Save the transcript to the new file.
                with open(output_filepath, 'w', encoding='utf-8') as outfile:
                    outfile.write(transcript_text)
                
                print(f"Successfully saved transcript to: {output_filepath}")
            else:
                print(f"No transcript found for URL: {url}")
        
        # Catch specific errors for more informative feedback
        except (NoTranscriptFound, VideoUnavailable):
            print(f"Skipping: No transcript found or video unavailable for '{url}'")
        except HTTPError as e:
            # Handle the 400 Bad Request error specifically
            print(f"An HTTP error occurred for URL '{url}': {e}. The video might be private or have no transcript.")
        except Exception as e:
            # Fallback for any other unexpected errors
            print(f"An unexpected error occurred for URL '{url}': {e}", file=sys.stderr)


if __name__ == "__main__":
    # Get the input file name from command-line arguments.
    # The first argument (sys.argv[0]) is the script name itself.
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file_path>", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_directory = "transcripts/mlops"
    
    process_urls_from_file(input_file, output_directory)

