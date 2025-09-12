# exemplo de chamada usando geração de áudio

from openai import OpenAI

client = OpenAI(
    api_key = '',
)

# ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer']

response = client.audio.speech.create(
    model='tts-1',
    voice='echo',
    input='Eu sou um áudio gerado por IA',
) 

response.write_to_file('meu_audio.mp3')

