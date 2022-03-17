# coding=utf-8
# This is a sample Python script.
import openai
import streamlit as st
import os.path
import json
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import os


# API call to openAI
#from typing import List

openai.organization = "org-fH9F3VZEWvBphHnp3ixuJkqN"  #  Get this from openai
openai.api_key = st.secrets["api_token"]   # Get this from openai


# Set up bot interface with streamlit
st.markdown('# 🤖 *Sandy*, The Expert AWS BOT')
st.header('Sandy will answer relevant questions about Machine Learning and EC2 on AWS')
 #                        max_chars=120,
  #                       placeholder= "knowledge_ESG.txt")
#kf_name = st.text_input(label="Knowledge base",
              #           max_chars=120,
              #           placeholder= "knowledge_ESG.txt")
#getfile = st.button("Acquire Knowledge")
question = st.text_area('Questions..')
button = st.button("Ask me")

# Set filepaths for knowledge bank
filepath = r"/Users/dfrankle/downloads/"
jsonlname = "knowledge_jsonl.jsonl"  # Do not change
knowledge_jsonl = os.path.join(filepath, jsonlname)
#knowledge = os.path.join(filepath, kf_name)

# Process knowledge file
#if getfile:
    # Delete existing file from API
 #   count = len(openai.File.list()['data'])
  #  if count >= 1:
    #    openai.File.delete(openai.File.list()['data'][0]['id'])
    #    openai.File.list()

    # Process generating knew knowldege file
  #  lines = []
  #  with open(knowledge, encoding="utf8") as f:
    #    for line in f.read().splitlines():
       #     if line:
         #       lines.append({"text": line})

    # Convert to a list of JSON strings
       #         json_lines = [json.dumps(l) for l in lines]

    # Join lines and save to .jsonl file
#    json_data = '\n'.join(json_lines)
 #   with open(knowledge_jsonl, 'w') as f:
   #     f.write(json_data)

    # Open knowledge base
   # openai.File.create(file=open(knowledge_jsonl, encoding="utf8"), purpose='answers')


# Knowledge engine question and answer
#if button:
 #   response_json = openai.Answer.create(
  #      search_model="ada",
  #      model="davinci",
   #     question=question,
   #     file=openai.File.list()['data'][-1]['id'],  # Get latest file
   #     examples_context= "In 2017, U.S. life expectancy was 78.6 years." ,
   #     examples=[["What is human life expectancy in the United States?", "78 years."]],
   #     max_rerank=500,
    #    max_tokens=100,
    #    stop=["\n", "<|endoftext|>"]
   # )
if button:
    response_json = openai.Answer.create(
        search_model="text-curie-001",
        model="text-davinci-002",
        question=question,
      #  question="I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What do Peons do?\nA: Peons are worker processes that execute submitted tasks.\n\nQ: What are some issues with enhanced IP in Druid?\nA: There are some issues with enhanced IP in Druid that can affect query execution. These issues can include:\n\nNot being able to connect to the data server\nThe data server not being able to connect to the coordinator\nThe data server not having the correct data\n\nQ: What is Druid?\nA: Druid is a data store that is used to store data for analysis.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: What are the benefits of columnar storage?\nA: Columnar storage formats are highly optimized for linear scans, meaning that they can quickly scan through all the data in a column. This makes them a good choice for analytics applications.\n\nQ: Why doesn't Druid support JOINs?\nA: Druid doesn't support JOINs because they can be expensive and can slow down your queries.\n\nQ: How many squigs are in a bonk?\nA: Unknown" + question,
        temperature=0,
        file="file-wGQK3BJOwwg6c0Ldt6HLZ8MZ",
        examples_context="In 2017, U.S. life expectancy was 78.6 years.",
        examples=[["What is human life expectancy in the United States?", "78 years."]],
        max_rerank=100,
        max_tokens=320,
        n=1,
        stop=["<|endoftext|>"]
    )

    # Return answer to UI
    st.markdown(response_json["answers"][0], unsafe_allow_html=False)
#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
  #  print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
  #  print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
