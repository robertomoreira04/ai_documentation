import os 
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

os.environ['OPENAI_API_KEY'] = 'sk...'

model = ChatOpenAI(model = 'gpt-3.5-turbo')

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content='Você deve responder baseado em dados geográficos...'),
        HumanMessagePromptTemplate.from_template('Me fale sobre a região {regiao}.'),
        AIMessage(content='Claro, vou começar coletando as informações sobre a região.'),
        HumanMessage(content='Certifique-se de incluir os dados...'),
        AIMessage(content='Entendido, aqui estão os dados:')

    ]
)

prompt = chat_template.format_messages(regiao='Sul')

response = model.invoke(prompt)

print(response.content)

