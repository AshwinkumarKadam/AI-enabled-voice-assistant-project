# AI Voice Assistant (Jarvis)

A Python-based voice assistant that listens for the "Jarvis" wake word, responds to commands, and uses Google's Gemini AI for conversational answers.

## Features

* **Wake Word Activation**: Listens for "Jarvis" before processing commands.
* **Web Browsing**: Opens Google, YouTube, and Facebook.
* **Music Player**: Plays songs from a local library (e.g., "play imagine").
* **News Reader**: Fetches and speaks the latest top headlines from NewsAPI.
* **AI Integration**: Uses Google's Gemini AI to answer any unrecognized questions.
* **Exit Command**: Shuts down with the "sleep jarvis" command.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-project-name.git](https://github.com/your-username/your-project-name.git)
    cd your-project-name
    ```

2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    # On macOS/Linux
    python3 -m venv env
    source env/bin/activate

    # On Windows
    python -m venv env
    .\env\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install speechrecognition pyttsx3 requests google-generativeai
    ```

4.  **Install PyAudio:**
    `speechrecognition` requires PyAudio for microphone access.
    ```bash
    pip install PyAudio
    ```

## Configuration

Before running the assistant, you must configure API keys and set up your music library.

### 1. API Keys

Open the main `.py` script and add your API keys in the designated spots:

* **Google Gemini AI Key:**
    Get your key from [Google AI Studio](https://aistudio.google.com/) and add it here:
    ```python
    def aiProcess(command):
        client = genai.Client(api_key="put you api key here") 
        # ...
    ```

* **NewsAPI Key:**
    Get your key from [NewsAPI.org](https://newsapi.org/) and add it here:
    ```python
    newsapi ="put you news api key here"
    ```

### 2. Music Library

This assistant plays music by looking up a song in a local file.

1.  In the same directory as your main script, create a new file named `musiclibrary.py`.
2.  Inside this file, create a Python dictionary named `music`. This dictionary should map the song name (the command you will say) to its full URL (e.g., a YouTube link).

**Example `musiclibrary.py`:**
```python
music = {
    'imagine': '[https://www.youtube.com/watch?v=YkgkThdzX-8](https://www.youtube.com/watch?v=YkgkThdzX-8)',
    'bohemian': '[https://www.youtube.com/watch?v=fJ9rUzIMcZQ](https://www.youtube.com/watch?v=fJ9rUzIMcZQ)',
    'never': '[https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ)'
}
