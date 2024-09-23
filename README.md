# Voice Chatbot with Streamlit and OpenAI

This project is a simple voice-based chatbot that uses **Streamlit** and **OpenAI**'s API to transcribe audio inputs, generate text-based responses, and convert those responses back into audio format.

## Features

- **Audio Recording:** The app allows users to record their voice directly.
- **Transcription:** It transcribes the recorded voice using OpenAI's Whisper model.
- **AI Response Generation:** Uses OpenAI's GPT-3.5 Turbo to generate text responses based on the transcribed text.
- **Text-to-Speech:** Converts the AI-generated text response back into audio using OpenAI's text-to-speech feature.
- **Interactive UI:** Displays the transcribed text and the AI's response in a card format. Automatically plays the AI-generated audio.

## Prerequisites

- Python 3.7+
- Streamlit
- OpenAI API Key
- The following Python packages must be installed:
  - `streamlit`
  - `audio_recorder_streamlit`
  - `openai`
  - `base64`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-repository-name/voice-chatbot.git
    cd voice-chatbot
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install streamlit openai audio_recorder_streamlit
    ```

4. Create a file named `api_key.py` in the project root directory to store your OpenAI API key:

    ```python
    api_key = "your_openai_api_key"
    ```

5. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Enter your OpenAI API key in the sidebar under "API KEY CONFIGURATION."
2. Click the **Record** button to start recording your voice.
3. After recording, the app will:
   - Transcribe your audio using OpenAI's Whisper model.
   - Generate a response using GPT-3.5 Turbo.
   - Convert the response text into speech using OpenAI's text-to-speech engine.
   - Display the transcribed text and the AI-generated response in cards.
   - Automatically play the AI-generated audio response.

## Code Explanation

The following functions are the core parts of the app:

- **`setup_openai_client(api_key)`**: Initializes the OpenAI client using the provided API key.
  
- **`transcript_audio(client, audio_path)`**: Transcribes audio using the Whisper model from OpenAI.

- **`fetch_ai_response(client, input_text)`**: Sends the transcribed text to OpenAI GPT-3.5 Turbo and receives a response.

- **`text_to_audio(client, text, audio_path)`**: Converts the AI response text into speech and saves it as an MP3 file.

- **`create_text_card(text, title)`**: Creates a card layout in Streamlit for displaying transcribed text and AI responses.

- **`auto_play_audio(audio_file)`**: Automatically plays an audio file directly in the Streamlit app.

## Example

When running the app, you will interact with the following UI elements:

- **API Key Configuration**: You enter your OpenAI API key here.
- **Audio Recording**: You record your voice.
- **Transcribed Text**: The app displays your transcribed audio.
- **AI Response**: The app shows the AI's response and automatically plays the audio.

## File Structure

```plaintext
voice-chatbot/
│
├── app.py              # Main Streamlit app code
├── api_key.py          # Stores the OpenAI API key
├── README.md           # Project documentation
├── venv/               # Virtual environment (optional)
└── requirements.txt    # Required Python packages

```

## Notes

- Make sure your OpenAI API key has access to the Whisper model and GPT-3.5 Turbo.
-	If you’re experiencing issues with audio recording or playback, ensure the correct file formats are used and supported by your system.

## License

This project is licensed under the MIT License.
