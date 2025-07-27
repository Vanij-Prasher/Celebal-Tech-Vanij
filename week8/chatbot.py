import os
import pandas as pd
from dotenv import load_dotenv

from langchain_community.document_loaders import CSVLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Ensure the CSV is read from the same directory
CSV_PATH = os.path.join(os.path.dirname(__file__), "dataset.csv")

# Load with LangChain for RAG
loader = CSVLoader(file_path=CSV_PATH)
documents = loader.load()

# Load with pandas for stats
import pandas as pd
df = pd.read_csv(CSV_PATH)

# Split into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

# Embedding and vector store
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.from_documents(docs, embedding_model)
retriever = db.as_retriever()

# LLM from Groq
llm = ChatGroq(model_name="llama3-8b-8192")

# RAG chain setup
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=False
)

# Helper: stats from the dataset
def get_loan_stats() -> str:
    total = len(df)
    approved = len(df[df["Loan_Status"] == "Y"])
    rejected = len(df[df["Loan_Status"] == "N"])
    return f"There are {approved} approved loans and {rejected} rejected loans out of {total} total applications."

# Main function for UI
def get_answer(question: str) -> dict:
    q = question.lower()

    # Handle simple questions without LLM
    if "approved" in q and "loan" in q:
        return {"result": get_loan_stats()}
    elif "rejected" in q:
        return {"result": get_loan_stats()}
    elif "total" in q and "loan" in q:
        return {"result": get_loan_stats()}
    elif "approval rate" in q:
        total = len(df)
        approved = len(df[df["Loan_Status"] == "Y"])
        if total > 0:
            rate = round((approved / total) * 100, 2)
            return {"result": f"The approval rate is approximately {rate}% ({approved}/{total})."}
        else:
            return {"result": "No loan data available to calculate approval rate."}

    # Otherwise use RAG + LLM
    return qa_chain.invoke({"query": question})