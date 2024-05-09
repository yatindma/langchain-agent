from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_text_splitters import CharacterTextSplitter


# create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")



def setup_database():
    loader = TextLoader("/Users/yatin/Desktop/Agentic-workflow/wiki-cancer.txt")
    documents = loader.load()
    # split it into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    # load it into Chroma
    db = Chroma.from_documents(docs, embedding_function) 
    return db

def search_database(query: str):
    db = setup_database()
    results = db.similarity_search(query)
    return results[0].page_content
