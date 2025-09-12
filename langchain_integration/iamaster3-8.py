# route chain (usado para vários chains que mudam de acordo com a pergunta)

import os 
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ['OPENAI_API_KEY'] = 'sk...'

model = ChatOpenAI(model='gpt-3.5-turbo')

classification_chain = (
    PromptTemplate.from_template(
        '''
        Classifique a pergunta do usuário em um dos seguintes setores:
        - Financeiro 
        - Suporte técnico 
        - Outras informações

        Pergunta: {pergunta}
        '''
    )
    | model
    |StrOutputParser()
)

financial_chain = (
    PromptTemplate.from_template(
        '''
        Você é um especialista financeiro.
        Sempre responda as perguntas começando com "Bem vindo ao setor financeiro".
        Responda à pergunta do usuário:
        Pergunta: {pergunta}
        '''
    )
    | model
    |StrOutputParser()
)

tech_support_chain = (
    PromptTemplate.from_template(
        '''
        Você é um especialista em suporte técnico.
        Sempre responda as perguntas começando com "Bem vindo ao suporte técnico".
        Responda à pergunta do usuário:
        Pergunta: {pergunta}
        '''
    )
    | model
    |StrOutputParser()
)

other_info_chain = (
    PromptTemplate.from_template(
        '''
        Você é um especialista de informações gerais.
        Sempre responda as perguntas começando com "Bem vindo ao setor central de informações".
        Responda à pergunta do usuário:
        Pergunta: {pergunta}
        '''
    )
    | model
    |StrOutputParser()
)
 
def route(classification):
    classification = classification.lower()
    if 'financeiro' in classification:
        return financial_chain
    elif 'técnico' in classification:
        return tech_support_chain
    else:
        return other_info_chain
    
pergunta = 'Como faço para alterar a minha senha?'

classification = classification_chain.invoke(
    {'pergunta': pergunta}
    )

response_chain = route(classification=classification)

response = response_chain.invoke(
    {'pergunta': pergunta}
)

print(response)

