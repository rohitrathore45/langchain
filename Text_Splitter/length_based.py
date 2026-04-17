from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# text = """
# Artificial Intelligence (AI) is transforming the way we interact with technology and shaping the future of industries across the globe. From healthcare to finance, education to entertainment, AI is becoming an integral part of modern life. At its core, AI refers to the ability of machines to perform tasks that typically require human intelligence, such as understanding language, recognizing patterns, solving problems, and making decisions.

# One of the most widely used applications of AI is machine learning, a subset of AI that allows systems to learn from data and improve their performance over time without being explicitly programmed. Machine learning algorithms analyze large amounts of data to identify patterns and make predictions. For example, recommendation systems used by platforms like streaming services and e-commerce websites rely heavily on machine learning to suggest content or products based on user behavior."""

loader = PyPDFLoader('dl-curriculum.pdf')
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

# result = splitter.split_text(text)
# print(result)

result = splitter.split_documents(docs)
print(result[1].page_content)