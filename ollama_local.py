#! usr/bin/env/python 3 // fix this to be acurate.

# This was written by: David Metcalf
# This was written on May, 04, 2024
# This was updated on:

import os
import ollama

# NOTE:
# you found this easy to follow how to, from the following youtube video.
# https://youtu.be/etHl_bEfQ0c?si=dAzY1Z-Hrzmh3QG4

# Note:
# The code below is heavily baised on the code in that video.

# NOTE:
# In general ollama must already be installed along wih any llm
# model that you wish to use before running this python program.

# NOTE:
# You can download and install ollama from the following website.
# https://ollama.com/download
 
# NOTE:
# It is also worth mentioning that you will need to have the
# python module "ollama" installed as well.

# NOTE
# To install this ollama module, in a command prompt type the following:
#       python -m pip install ollama
# If you're using python 3 type the following instead:
#       python3 -m pip install ollama

# NOTE:
# Make sure that you have the llm model you want to use already installed.
# To do this simply type into a command prompt the following: 
#       ollama run llama3
#
# The breakdown of the above goes like this
#       ollama run "name of you're model goes here"


# Uncomment one of the following lines below to choose a 'llm model'.
#
#llm_model = "dolphin-mixtral"
#llm_model = "everythinglm"
#llm_model = "gemma"
#llm_model = "llama3"
#llm_model = "llava"
#llm_model = "meditron"
#llm_model = "mistral"
#llm_model = "mixtral"
#llm_model = "samantha-mistral"
#llm_model = "wizard-vicuna-uncensored"
#llm_model = "wizardcoder:"
llm_model = "llama3" # This is the default llm model that we will be using.

# Uncomment one of the following lines below to choose a 'persona'
#
#persona =  "princess"
#persona =  "orc"
persona = " " # This is the default persona that we will be using.

hidden_pre_prompts = " "
query_input = " "

if persona == "princess":
    pre_prompt_1 = "Answer in 25 words or less."
    pre_prompt_2 = "Answer as a sexy ditzy college girl might."
    pre_prompt_3 = "Have a ditzy college girl persona."
    pos_pre_prompts = pre_prompt_1 + pre_prompt_2 + pre_prompt_3
    #
    neg_pre_prompt_1 = "Avoid using 'bats eyelashes', 'winks', 'brushes hair back', or other traits that would be visable and visual."
    neg_pre_prompt_2 = "Avoid using 'Ohmygod' , 'Omigosh' , 'hunty' and 'hiya'. If you have to use these, make sure their is proper spacing for easy readability."
    neg_pre_prompt_3 = "Avoid using 'hunny'."
    neg_pre_prompt_4 = "Avoid using incomprehensible or unintelligible words."
    neg_pre_prompts =  neg_pre_prompt_1 + neg_pre_prompt_2 + neg_pre_prompt_3 + neg_pre_prompt_4
    #
    hidden_pre_prompts = pos_pre_prompts + neg_pre_prompts
    query_input = "Like, OMG! How can i like help you and junk?"
    
if persona == "orc":
    pre_prompt_1 = "Answer in 18 words or less."
    pre_prompt_2 = "Answer as violent orc might."
    pre_prompt_3 = "Have a violent orc persona."
    pos_pre_prompts = pre_prompt_1 + pre_prompt_2 + pre_prompt_3
    #
    neg_pre_prompt_1 = "Avoid using 'smash', 'pow', 'biff'." 
    neg_pre_prompt_2 = "Avoid using traits that would be visable and visual as well as onamonapea."
    neg_pre_prompt_3 = ""
    neg_pre_prompt_4 = ""
    neg_pre_prompts =  neg_pre_prompt_1 + neg_pre_prompt_2 + neg_pre_prompt_3 + neg_pre_prompt_4
    #
    hidden_pre_prompts = pos_pre_prompts + neg_pre_prompts
    query_input = "How me do for you?"

if persona == " " or persona == "":
    pre_prompt_1 = "Answer in 25 words or less."
    pos_pre_prompts = pre_prompt_1
    #
    neg_pre_prompt_1 = ""
    neg_pre_prompts = neg_pre_prompt_1
    #
    hidden_pre_prompts = pos_pre_prompts + neg_pre_prompts
    query_input = "How may I help you?"
    
def ask(query):
    query = f"{query} - " + hidden_pre_prompts
    response = ollama.chat(model= llm_model, messages =[
    {
        'role': 'user',
        'content': query,
    },
    ])
    response = response['message']['content']
    return response

os.system('clear')
while True:
    query = input(query_input)
    os.system('clear')
    answer = ask(query)
    #print(f'Question: {query}')
    print("")
    print(answer)
    print("")
