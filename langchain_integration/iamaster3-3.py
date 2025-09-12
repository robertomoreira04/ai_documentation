# pip install langchain_openai (realizar isso no terminal antes de começar a usar o langchain)

import os 
from langchain_openai import OpenAI, ChatOpenAI

os.environ['OPENAI_API_KEY'] = 'sk...'

# model = OpenAI()

# response = model.invoke(
 #   input='A pergunta',
 #   temperature=1,
  #  max_tokens=500,
#)

#print(response)

model = ChatOpenAI(
    model='gpt-4o-mini',
)

messages = [
    {'role': 'system', 'content': 'Vocẽ é....'}
    {'role': 'user', 'content': 'Quem foi....'}
]

response = model.invoke(messages)

print(response)
print(response.content)

