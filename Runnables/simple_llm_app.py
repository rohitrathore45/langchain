from langchain.llms import OpenAI
from langchain_core.prompts import PromptTemplate

llm = OpenAI(model_name = 'gpt-4o-mini')

prompt = PromptTemplate(
    template='Suggest a catchy blog title about {topic}',
    input_variables=['topic']
)

topic = input('Enter a topic')

formatted_input = prompt.format(topic=topic)

blog_title = llm.predict(formatted_input)

print("Generated blog title : ", blog_title)