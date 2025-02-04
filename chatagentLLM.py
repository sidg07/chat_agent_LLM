import streamlit as st

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from langchain_ollama import OllamaLLM


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant . Please response to the queries"),
        ("user", "Question:{question}")
    ]
)

st.title("Langchin Demo with OpenAPI")
input_text = st.text_input("Search the topic you want")


llm = OllamaLLM(model='llama3.2')
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if (input_text):
    st.write(chain.invoke({'question': input_text}))
