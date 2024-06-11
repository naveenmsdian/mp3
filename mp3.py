import streamlit as st
from moviepy.editor import VideoFileClip
import tempfile
import os

def convert_to_mp3(video_file_path):
    with st.spinner('Converting video to MP3...'):
        video_clip = VideoFileClip(video_file_path)
        audio_clip = video_clip.audio
        mp3_file_path = os.path.join(tempfile.gettempdir(), "output.mp3")
        audio_clip.write_audiofile(mp3_file_path)
        audio_clip.close()
        video_clip.close()
        return mp3_file_path

st.title("Video to MP3 Converter")

# File uploader
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi", "mkv"])

if uploaded_file is not None:
    st.video(uploaded_file)
    
    if st.button('Convert to MP3'):
        # Create a temporary file to save the uploaded video
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video_file:
            temp_video_file.write(uploaded_file.read())
            temp_video_file_path = temp_video_file.name
        
        # Convert video to MP3
        mp3_file_path = convert_to_mp3(temp_video_file_path)
        
        st.success("Conversion completed!")
        
        # Provide download link
        with open(mp3_file_path, "rb") as f:
            st.download_button(
                label="Download MP3",
                data=f,
                file_name="converted_audio.mp3",
                mime="audio/mpeg"
            )
        
        # Clean up temporary files
        os.remove(temp_video_file_path)
        os.remove(mp3_file_path)

# Footer
st.write("Developed by Naveen Kumar.")
