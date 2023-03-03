import os
import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

# Create a text area widget for user input
function = st.text_area("Enter your question about Interworks here:")

# Check if user input is not empty
if function:
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= f"You are an AI expert about https://interworks.com/ .\nYou help people understand InterWorks as a company and the services they provide.\nI'm sorry, I'm unsure about that, but you can contact us at https://interworks.com/contact-us/ . We'd be happy to answer any questions you may have\n{function}",
    temperature=0.5,
    max_tokens=527,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    # Get the generated doc string from the response
    doc_string = response["choices"][0]["text"]

    # Use streamlit.write or other widgets to display the generated doc string on your web app
    st.header('About InterWorks')
    st.markdown(doc_string)
