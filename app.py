import streamlit as st 
from audio_recorder_streamlit import audio_recorder 
import openai
import base64



def setup_openai_client(api_key):

    return openai.OpenAI(api_key=api_key)

def transcript_audio(client, audio_path):

    with open(audio_path,  "rb") as audio_file:
        transcript= client.audio.transcriptions.create(model='whisper-1', file=audio_file)
        return transcript.text

def fetch_ai_response(client, input_text):
    messages = [{"role": "user", "content": input_text}]
    response = client.chat.compeletion.create(model="gpt-3.5-turbo-1106", messages=messages)
    return response.choices[0].message.content

def text_to_audio(client, text, audio_path) :
    response = client.audio.speech.create(model="tts-1", voice="echo", input=text)
    response.steam_to_file(audio_path)

def create_text_card(text, title="Response"):
    card_html = f"""
            ‹style>
            .card {{
                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
                transition: 0.3s;
                border-radius: 5px;
                padding: 15px;
            }}
            .card:hover {{
                box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
            }}
            .container {{
                padding: 2px 16px;
            }}
        </style>
        <div class="card">
            <h4><b>{title}</b></h4>
            <p>{text}</p>
        </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)


def auto_play_audio(audio_file):
    with  open(audio_file, "rb") as audio_file:
        audio_bytes=audio_file.read()
    base64_audio=base64.b64encode(audio_bytes).decode("utf-8" )
    audio_html = f'<audio src="data:audio/mp3;base64,{base64_audio}" controls autoplay>'
    st.markdown(audio_html, unsafe_allow_html=True)
        


def main():

    st.sidebar.title("API KEY CONFIGURATION")
    api_key = st.sidebar.text_input("Enter you OpenAI Api Key", type="password")


    st.title(" 🧠 Just a Rather Very Intelligent Assistance 🤖 ")
    st.write("This is a simple Voice chatbot built with Streamlit and OpenAI API")
    st.write("Hey there👋🏻!!, How can i Assit you today!!")

    if api_key:
        client = setup_openai_client(api_key)
    
        recorded_audio = audio_recorder()

        if recorded_audio:
            audio_path = "audio.mp3"
            with open(audio_path, "wb") as f:
                f.write(recorded_audio)

            transcribed_text = transcript_audio(client, audio_path)
            #st.write("transcribed Text: " + transcribed_text)
            create_text_card(transcribed_text, "Transcribed Text")

            ai_response = fetch_ai_response(client, transcribed_text)
           
            audio_file_path = "  ai_audio_response.mp3"

            text_to_audio(client, ai_response, response_audio_file)
            #st.audio(response_audo_file, format="audio/mp3")
            auto_pay_audio(response_audio_file)

            create_text_card(ai_response, "AI Response")
            #st.write("AI Response: " + ai_response)


if __name__ == "__main__":
    main()