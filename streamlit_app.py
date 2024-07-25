import streamlit as st

st.title("Youtube downloader")
st.write(
    "Copy and paste your URL here"
)

#import streamlit as st
from pytube import YouTube
import os

def download_video(url, resolution):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4', res=resolution).first()
        if not stream:
            st.error(f"No video found with resolution {resolution}.")
            return None
        stream.download(output_path="downloads")
        return os.path.join("downloads", stream.default_filename)
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

st.title("YouTube Video Downloader")

# URL input
url = st.text_input("Enter YouTube video URL")

# Resolution selection
resolution = st.selectbox("Select Resolution", ["360p", "720p", "1080p"])

if st.button("Download"):
    if url:
        st.info("Downloading...")
        filepath = download_video(url, resolution)
        if filepath:
            st.success("Download completed!")
            with open(filepath, "rb") as file:
                btn = st.download_button(
                    label="Download Video",
                    data=file,
                    file_name=os.path.basename(filepath),
                    mime="video/mp4"
                )
            os.remove(filepath)
    else:
        st.error("Please enter a valid URL.")
