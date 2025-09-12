# exemplo de chamada usando parâmetros da open ai

from openai import OpenAI

client = OpenAI(
    api_key = 'api_key'
)

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages= [
        {"role": 'system', 'content': 'Você é um assistente...'},
        {"role": 'user', 'content': 'O conteúdo a ser perguntado'},
    ],
    #usando parametros 
    max_tokens=150,
    temperature=0.3, #quanto mais alto, mais criativo,quanto menor, uma resposta mais técnica. 
) 

print(response) # para ver todo o conteúdo 
print(response.choices[0].messages.content) # para pegar apenas o message