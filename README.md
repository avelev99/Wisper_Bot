This script transcribes audio files in the current directory and writes the transcriptions to a file named script.txt. The script uses the Whisper library for audio transcription and FFmpeg for converting audio files to the MP3 format.

The script has the following components:

The AudioTranscriber class that initializes the Whisper model, converts MP4 files to MP3 files, and transcribes audio files.
The convert_to_mp3 method that converts all MP4 files in the current directory to MP3 files.
The transcribe method that transcribes a given audio file and returns the transcription as a string.
The main function that writes the transcriptions of all MP3 files in the current directory to script.txt.

Note that the Whisper model used in this script is the "base" model, but you can use any other model available in the Whisper library.
