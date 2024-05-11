import base64
import requests
import streamlit as st
from PIL import Image

from audiorecorder import audiorecorder

def process_audio(audio):
    url = "http://34.168.116.94:8000/docs"
    files = {'audio_file': open(audio, 'rb')}
    try:
        response = requests.post(url, files=files)
        if response.status_code == 200:
            generated_audio = response.content
            return generated_audio
        else:
            print("Error:", response.text)
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None
    


def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

def main():
    title = "Verbify AI"
    st.title(title)
    image = Image.open('images/VERBIFYAI.jpg')
    st.image(image, use_column_width=True)

    audio = audiorecorder("Record", "Click to stop recording")
    if len(audio) > 0:
        # To play audio in frontend:
        st.audio(audio.export().read())  

        # To save audio to a file, use pydub export method:
        audio.export("audio/recording.mp3", format="mp3")
        st.success("Recording completed")

        st.spinner("Generating audio...")
        generated_audio = process_audio('audio/recording.mp3')
        if generated_audio:
            st.success("Audio generated successfully. Playing...")
            autoplay_audio(generated_audio)
        else:
            st.error("Failed to generate audio.")



if __name__ == '__main__':
    main()
