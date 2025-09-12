# exemplo de chamada básica da open ai

from openai import OpenAI

client = OpenAI(
    api_key = 'api_key'
)

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages= [
        {"role": 'user', 
         'content': 'O conteúdo a ser perguntado'},
    ],
)

print(response) # para ver todo o conteúdo 
print(response.choices[0].messages.content) # para pegar apenas o message

