from langchain_community.llms import LlamaCpp
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain.text_splitter import CharacterTextSplitter
import os
from dotenv import load_dotenv

load_dotenv()

# Load CSV as documents
loader = CSVLoader(file_path="data/Training Dataset.csv.xls")
documents = loader.load()

# Split into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

# Embedding Model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Vector Store
db = FAISS.from_documents(docs, embedding_model)
retriever = db.as_retriever()

# Load Local LLM
model_path = os.getenv("MODEL_PATH")

llm = LlamaCpp(
    model_path=model_path,
    n_ctx=2048,
    temperature=0.7,
    top_p=0.95,
    verbose=True,
    n_gpu_layers=-1  # use all GPU layers on Metal
)

# QA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=False
)