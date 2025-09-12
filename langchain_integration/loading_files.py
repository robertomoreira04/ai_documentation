import os 
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import textLoader, PyPDFLoader, CSVLoader

os.environ['OPENAI_API_KEY'] = 'sk...'

model = ChatOpenAI(model='gpt-3.5-turbo')

# text loader 

# loader = textLoader('base_conhecimento.txt') # caminho do arquivo
# documents = loader.load()

# pdf loader (pip install pypdf)

# loader = PyPDFLoader('base_conhecimento.pdf')
# documents = loader.load()

# CSV loader
loader = CSVLoader('base_conhecimento.csv')
documents = loader.load()

prompt_base_conhecimento = PromptTemplate(
    input_variables=['contexto', 'pergunta'],
    template='''Use o seguinte contexto para responder à pergunta.
    Responda apenas com base nas informações fornecidas.
    Não utilize informações externas ao contexto:
    Contexto: {contexto}
    Pergunta: {pergunta}'''
)

chain = prompt_base_conhecimento | model | StrOutputParser()

response = chain.invoke(
    {
        'contexto': '\n'.join(doc.page_content for doc in documents),
        'pergunta': 'Qual óleo de motor devo usar?',
    }
)

print(response)

