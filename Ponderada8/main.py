from deep_translator import GoogleTranslator
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os
import whisper

class STT:
    def __init__(self):
        self.model = whisper.load_model("small")

    def transcribe_audio(self, audio_path):
        model_result = self.model.transcribe(audio_path)
        transcription = model_result["text"]
        return transcription


class Translate:
    def __init__(self, source_language, target_language):
        self.trans = GoogleTranslator(source=source_language, target=target_language)

    def translate_text(self, text):
        translated_text = self.trans.translate(text)
        return translated_text


class TTS:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_audio(self, text, model_name, voice_name):
        speech_file_path = Path(__file__).parent / "translated_audio.mp3"
        audio_response = self.client.audio.speech.create(
            model=model_name,
            voice=voice_name,
            input=text
        )
        audio_response.stream_to_file(speech_file_path)
        return speech_file_path


if __name__ == "__main__":
    stt = STT()
    translate = Translate(source_language="pt", target_language="en")
    tts = TTS()

    audio_transcription = stt.transcribe_audio("audio.mp3")
    print(f"Áudio transcrito: {audio_transcription}")

    translated_text = translate.translate_text(audio_transcription)
    print(f"Tradução: {translated_text}")

    audio_file_path = tts.generate_audio(translated_text, "tts-1", "alloy")
    print(f"Áudio gerado: {audio_file_path}")
