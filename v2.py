import os
import streamlit as st
from dotenv import load_dotenv
import pandas as pd
from llama_index.llms.gemini import Gemini

from llama_index.core.memory import ChatMemoryBuffer

# query library
from src.query import qp

# functions




# setting up streamlit UI
st.set_page_config(page_title="v2", page_icon="🐔")
st.title("v2")

# getting memory
pipeline_memory = ChatMemoryBuffer.from_defaults(token_limit=8000)

# Streamlit app layout
def main():
    if "messages" not in st.session_state.keys(): # Initialize the chat message history
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! Welcome to ChickIn Chat. How can I help you today?"}
        ]
    
   
    

    if query := st.chat_input("Your question"): # Prompt for user input and save to chat history
        st.session_state.messages.append({"role": "user", "content": query})
       

    for message in st.session_state.messages: # Display the prior chat messages
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # If last message is not from assistant, generate a new response
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Processing"):
                query_str = str(query)
                print(query_str)
                response = qp.run(query_str = query_str)
                st.write(response.message.content)
                message = {"role": "assistant", "content": response}
                st.session_state.messages.append(message) # Add response to message history


if __name__ == "__main__":
    load_dotenv()
    main()

