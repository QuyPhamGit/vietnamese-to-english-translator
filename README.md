# Live Speech Translation: Vietnamese to English

**Author**: Quy Pham Ngo Thien

This simple project listens for Vietnamese speech using the `speech_recognition` library, transcribes it to text, and then translates the text from Vietnamese to English using the Hugging Face MarianMT model. The translated text is then printed to the console.

## Features:
- Real-time Vietnamese speech recognition.
- Automatic translation from Vietnamese to English.
- Continuously listens for speech until manually stopped.

## How It Works:
1. **Audio Capture**: The script captures audio input through the microphone.
2. **Speech Recognition**: Google's Speech-to-Text API is used to recognize the Vietnamese speech and convert it to text.
3. **Translation**: The recognized Vietnamese text is then translated to English using the MarianMTModel from Hugging Face.
4. **Output**: Both the original Vietnamese text and the translated English text are printed to the console.

## Requirements:
- Python 3.x
- **Libraries**:
  - `speech_recognition`: For speech-to-text conversion.
  - `transformers`: For translation using the MarianMTModel.
  - `torch`: For model inference.
  - `pyaudio`: For capturing microphone input.

You can install these dependencies with:
```bash
pip install speech_recognition transformers torch pyaudio
