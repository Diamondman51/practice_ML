
# import os
# import wget
# from langchain.vectorstores import Qdrant
# from langchain.embeddings import OpenAIEmbeddings
# from langchain import OpenAI
# from langchain_community.document_loaders import BSHTMLLoader
# from langchain.chains import RetrievalQA
# import dotenv


# dotenv.load_dotenv()

# #download War and Peace by Tolstoy
# wget.download("http://az.lib.ru/t/tolstoj_lew_nikolaewich/text_0073.shtml")


# #load text from html
# loader = BSHTMLLoader("text_0073.shtml", open_encoding='ISO-8859-1')
# war_and_peace = loader.load()

# #init Vector DB
# embeddings = OpenAIEmbeddings(api_key=os.getenv('OPENAI_API_KEY'),)

# doc_store = Qdrant.from_documents(
#     war_and_peace, 
#     embeddings,
#     location=":memory:", 
#     collection_name="docs",
# )

# llm = OpenAI()
# # ask questions

# while True:
#     question = input('Ваш вопрос: ')
#     qa = RetrievalQA.from_chain_type(
#         llm=llm,
#         chain_type="stuff",
#         retriever=doc_store.as_retriever(),
#         return_source_documents=False,
#     )

#     result = qa(question)
#     print(f"Answer: {result}")






# from langchain_google_genai import GoogleGenerativeAIEmbeddings

# def get_google_embeddings():
#     # Initialize the Google Generative AI embedding model
#     gemini_embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
#     return gemini_embeddings

# def generate_embeddings():
#     # Get embeddings object
#     embeddings = get_google_embeddings()

#     # Example documents
#     documents = [
#         "The quick brown fox jumps over the lazy dog.",
#         "LangChain makes working with LLMs easier and more productive.",
#         "Google Generative AI is powerful for text embeddings."
#     ]

#     # Generate embeddings
#     document_embeddings = embeddings.embed_documents(documents)
#     return document_embeddings

# # Generate and print embeddings
# embeddings = generate_embeddings()
# for i, embedding in enumerate(embeddings):
#     print(f"Embedding for Document {i+1}: {embedding[:5]}... (truncated)")




# from transformers import AutoTokenizer, AutoModel
# import torch

# def generate_embeddings(sentences, model_name="distilbert-base-uncased"):
#     # Load the tokenizer and model
#     tokenizer = AutoTokenizer.from_pretrained(model_name)
#     model = AutoModel.from_pretrained(model_name)

#     # Tokenize the input sentences
#     inputs = tokenizer(sentences, return_tensors="pt", padding=True, truncation=True)

#     # Generate embeddings
#     with torch.no_grad():
#         outputs = model(**inputs)

#     # Use the CLS token's embedding (index 0)
#     embeddings = outputs.last_hidden_state[:, 0, :]

#     return embeddings

# # Example sentences
# sentences = ["Hugging Face is amazing!", "Transformers make NLP easy."]
# embeddings = generate_embeddings(sentences)

# Print the embeddings
# print(embeddings, '\n\n')



# from sentence_transformers import SentenceTransformer

# def generate_sentence_embeddings(sentences, model_name="all-MiniLM-L6-v2"):
#     model = SentenceTransformer(model_name)
#     embeddings = model.encode(sentences)
#     return embeddings

# # Example sentences
# sentences = ["Hugging Face is amazing!", "Transformers make NLP easy."]
# embeddings = generate_sentence_embeddings(sentences)

# Print the embeddings
# print(embeddings)



# from sentence_transformers import SentenceTransformer
# sentences = ["This is an example sentence", "Each sentence is converted"]

# model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
# embeddings = model.encode(sentences)
# print(embeddings)





# from langchain_openai import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate

# # Prompt
# template = """Answer the question based only on the following context:

# {context}

# Question: {question}"""

# prompt = ChatPromptTemplate.from_template(template['context':'context', 'question': 'question'])
# print(prompt)






import os
import sys
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

from langchain.document_loaders import Docx2txtLoader
import logging
logging.basicConfig(level=logging.INFO)



# Load document content
documents = []
docx_files = [os.path.join("vector_db", doc) for doc in os.listdir("vector_db") if doc.endswith('.docx')]
for file in docx_files:
    loader = Docx2txtLoader(file)
    documents.extend(loader.load())


# Step 1: Initialize Hugging Face embeddings
hf_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 2: Create a vector store
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=hf_embeddings,
)

# Step 3: Initialize a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 1})

# Step 4: Query the retriever
key = True
os.system('cls')
while key:
    query = input("Question: ")
    docs = retriever.get_relevant_documents(query)

    # Output the result
    # print(retriever, len(retriever))
    print("Number of retrieved documents:", len(docs))
    print("Retrieved document:", docs[0].page_content if docs else "No document found")
    if query == 'exit':
        key = False