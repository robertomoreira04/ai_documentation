# criando uma vector store com chunks de dados a partir de um pdf e guardando em um banco de dados chroma (sem ser persistido)
import os 
from langchain_chroma import Chroma
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter # para fazer chunks

os.environ["OPENAI_API_KEY"] = 'sk-proj...'

model = ChatOpenAI(
    model='gpt-4',
)

pdf_path = 'caminho_do.pdf'
loader = PyPDFLoader(pdf_path)

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter( # chama a função para dar "split (dividir)"
    chunk_size=1000, # tamanho do chunk
    chunk_overlap=200, #200 tokens de sobreposição
)

chunks = text_splitter.split_documents( # divide os documentos passando eles por parâmetro
    documents=docs,
)

print(chunks)

embedding = OpenAIEmbeddings()

vector_store = Chroma.from_documents(
    documents=chunks, #documentos estão prontos em chunks
    embedding=embedding, 
    collection_name='nomedacoleção',
)

retriever = vector_store.as_retriever() #recuperador de dados, para buscar os dados

# result = retriever.invoke(       result vira todos os pedaços de informação que conseguir encontrar com relação à pergunta
 #   'Pergunta sobre o documento'
# )

prompt = hub.pull('rlm/rag-prompt')

rag_chain = (
    {
        'context': retriever,
        'question': RunnablePassthrough(), # usado só para passar direto
    }
    | prompt
    | model 
    | StrOutputParser()
)

try:
    while True:
        question = input('Pergunta sobre o documento')
        response = rag_chain.invoke(question)
        print(response)
except KeyboardInterrupt:
    exit()

