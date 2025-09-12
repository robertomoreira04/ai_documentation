# exemplo de chamada usando transcrição de áudio

from openai import OpenAI

client = OpenAI(
    api_key = '',
)

audio_file = open('caminhodoaudio', 'rb') # rb = read byte, lê o áudiow

transcription = client.audio.transcriptions.create(
    model='whisper-1',
    file=audio_file,
) 

print(transcription.text)