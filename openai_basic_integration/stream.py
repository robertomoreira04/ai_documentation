# exemplo de chamada em "stream" (recebendo por chunks, pequenos pedaços) 

from openai import OpenAI

client = OpenAI(
    api_key = 'api_key'
)

stream = client.chat.completions.create(
    model='gpt-4o-mini',
    messages= [
        {"role": 'user', 
         'content': 'O conteúdo a ser perguntado'},
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
