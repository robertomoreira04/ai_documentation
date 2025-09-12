# criando uma vector store com chunks de dados a partir de um pdf e guardando em um banco de dados chroma persistido
import os 
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

os.environ["OPENAI_API_KEY"] = 'sk-proj...'

pdf_path = 'caminho_do.pdf'
loader = PyPDFLoader(pdf_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

chunks = text_splitter.split_documents(
    documents=docs,
)

persist_directory = 'vectorStore' # é o local que vai ser persistido os dados

embedding = OpenAIEmbeddings()

vector_store = Chroma.from_documents( # aqui ele cria a partir dos documentos
    documents=chunks,
    embedding=embedding,
    persist_directory=persist_directory, # a diferença do persistido é somente esse parâmetro
    collection_name='nomedacoleção',
)

