"""
Quy Pham Ngo Thien

This simple project listens for Vietnamese speech using the speech_recognition library, 
transcribes it to text, and then translates the text from Vietnamese to English 
using the Hugging Face MarianMT model. The translated text is then printed to the console.

Steps:
1. Capture audio input using the microphone.
2. Use Google's Speech-to-Text API to recognize Vietnamese speech.
3. Translate the recognized text from Vietnamese to English using the MarianMTModel.
4. Print the original Vietnamese text and the translated English text.

Requirements:
- speech_recognition
- transformers
- torch
- pyaudio

Note:
- This script runs in a loop and continuously listens for speech until manually stopped (Ctrl-C in terminal).
"""


import speech_recognition as sr
from transformers import MarianMTModel, MarianTokenizer

# Load the translation model
model_name = "Helsinki-NLP/opus-mt-vi-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_vietnamese_to_english(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    return tokenizer.batch_decode(translated, skip_special_tokens=True)[0]

def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening for Vietnamese speech...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            vietnamese_text = recognizer.recognize_google(audio, language="vi-VN")
            print(f"Recognized (Vietnamese): {vietnamese_text}")

            english_translation = translate_vietnamese_to_english(vietnamese_text)
            print(f"Translation (English): {english_translation}")
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError:
            print("Error with the speech recognition service.")

# Run live translation
while True:
    recognize_speech()
