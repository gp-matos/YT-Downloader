from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import os

def verify_youtube_link(url):
    try:
        yt = YouTube(url)
        # Additional checks can be added here if needed
        return yt  # Return the yt object if successful
    except Exception as e:
        print(e)
        return None

#format can be "mp4" or "mp3" or "wav"
def download_stream(url, path, name, format):
    # Verify the youtube link
    yt = verify_youtube_link(url)
    if yt is None:
        return "ERROR: Invalid youtube link"

    #check path exists
    if not os.path.exists(path):
        return "ERROR: Invalid path"

    if format == "mp4":
        # Get the highest quality video stream
        try:
            #get the highest resolution stream
            stream = yt.streams.get_highest_resolution()
            #download the stream to the specified path
            stream.download(output_path=path, filename=name + ".mp4")
            mp4_path = os.path.join(path, name + ".mp4")
            return mp4_path
        
        except Exception as e:
            return e
        
    elif format == "mp3":
        try:
            #get the highest quality audio stream
            stream = yt.streams.get_audio_only()
            #download the stream to the specified path
            stream.download(output_path=path, filename=name + ".mp4")
            #get the mp4 file path
            mp4_path = os.path.join(path, name + ".mp4")
            #get the mp3 file path
            mp3_path = os.path.join(path, name + ".mp3")
            #convert the mp4 file to mp3
            AudioFileClip(mp4_path).write_audiofile(mp3_path)
            #delete the mp4 file
            os.remove(mp4_path)
            return mp3_path
        except Exception as e:
            return e
        
    elif format == "wav":
        try:
            #get the highest quality audio stream
            stream = yt.streams.get_audio_only()
            #download the stream to the specified path
            stream.download(output_path=path, filename=name + ".mp4")
            #get the mp4 file path
            mp4_path = os.path.join(path, name + ".mp4")
            #get the mp3 file path
            wav_path = os.path.join(path, name + ".wav")
            #convert the mp4 file to wav
            AudioFileClip(mp4_path).write_audiofile(wav_path, 44100, 2, 2000,"pcm_s32le")
            #delete the mp4 file
            os.remove(mp4_path)
            return wav_path
        except Exception as e:
            return e
    else: # Invalid format
        return "ERROR: invalid format"
        
if __name__ == "__main__":
    #get url
    url = input("Enter the youtube link: ")
    #get the path to save the file
    path = input("Enter the path to save the file: ")
    #get the file name
    name = input("Enter the file name: ")
    #get the format
    format = input("Enter the format (mp4, mp3, wav): ")
    #download the stream
    download_stream(url, path, name, format)
        

        