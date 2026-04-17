from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

code = """
def add(a, b):
    return a + b

def multiply(a, b):
    result = 0
    for i in range(b):
        result += a
    return result

class Calculator:
    def divide(self, a, b):
        if b == 0:
            return "Error"
        return a / b
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 120,
    chunk_overlap = 0
)

chunks = splitter.split_text(code)
print(chunks[1])
print(len(chunks))