import whisper
import os
import subprocess

class AudioTranscriber:
    def __init__(self):
        self.model = whisper.load_model("base")

    def convert_to_mp3(self):
        for filename in os.listdir():
            if filename.endswith('.mp4'):
                mp3_filename = filename[:-4] + ".mp3"
                subprocess.run(["ffmpeg", "-i", filename, mp3_filename])
    
    def transcribe(self, filename):
        result = self.model.transcribe(filename)
        return result["text"]

transcriber = AudioTranscriber()
transcriber.convert_to_mp3()

def main():
    with open("script.txt", "w") as f:
        for filename in os.listdir():
            if filename.endswith('.mp3'):
                transcription = transcriber.transcribe(filename)
                f.write(f"Transcription for {filename}: {transcription}\n")