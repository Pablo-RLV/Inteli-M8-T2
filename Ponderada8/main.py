import whisper
from googletrans import Translator
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os


model = whisper.load_model("small")
modelResult = model.transcribe("audio.mp3")
transcription = modelResult["text"]
print(f"Áudio transcrito: {transcription}")

trans = Translator()
traduzido = trans.translate(transcription, dest="en").text
print(f"Tradução: {traduzido}")

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
speech_file_path = Path(__file__).parent / "traduzido.mp3"
audio_response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=traduzido
)
audio_response.stream_to_file(speech_file_path)
print(f"Áudio gerado: {speech_file_path}")