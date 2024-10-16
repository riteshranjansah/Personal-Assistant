# Jarvis - Personal Assistant

This repository contains a voice-activated personal assistant named Jarvis, built using Python. Jarvis can perform a variety of tasks such as searching Wikipedia, sending emails, and controlling web browsers, all through voice commands.

## Features

- **Voice Recognition**: Understands user commands using speech recognition.
- **Text-to-Speech**: Responds to the user with spoken words.
- **Time & Date**: Provides current time and greetings based on the time of day.
- **Web Browsing**: Opens websites like Google, YouTube, and Stack Overflow.
- **Music Player**: Plays random songs from a specified directory.
- **Email Sending**: Sends emails using Gmail.

## Getting Started

### Prerequisites

- Python 3.x
- Libraries:
  - `pyttsx3`
  - `speech_recognition`
  - `wikipedia`
  - `webbrowser`
  - `smtplib`
  - `random`
  - `pyautogui`

You can install the required libraries using pip:

```bash
pip install pyttsx3 SpeechRecognition wikipedia-api
```

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/riteshranjansah/personal-assistant.git
   cd personal-assistant
   ```

2. Replace the email and password in the `sendEmail` function with your Gmail credentials (ensure you handle security appropriately).

### Running the Application

1. Start the Jarvis application:
   ```bash
   python Personal-Assistant/jarvis.py
   ```

2. Follow the spoken prompts to interact with Jarvis.

## How It Works

- **Speech Recognition**: The `takeCommand` function captures audio input from the microphone and converts it to text using Google’s speech recognition.
- **Text-to-Speech**: The `speak` function uses the `pyttsx3` library to read out responses.
- **Task Execution**: Based on the recognized command, the program executes corresponding actions like opening websites, playing music, or sending emails.

## Customization

- Modify the music directory in the `play music` section to point to your preferred music folder.
- Adjust the email address in the `sendEmail` function to the recipient’s email.

## Acknowledgments

- [pyttsx3](https://pypi.org/project/pyttsx3/): Text-to-speech conversion library.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): Library for recognizing speech.
- [Wikipedia API](https://pypi.org/project/wikipedia/): For fetching Wikipedia summaries.

## Contact

For any questions or feedback, feel free to reach out via GitHub issues.
