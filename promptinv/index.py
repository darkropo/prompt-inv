from flask import Flask, jsonify, request, render_template
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/botchat', methods=['POST'])
def process_user_message():
    # Get the data from the request body
    data = request.get_json()
    message = data['message']
    prompt = f"""Tell me which language this is ```{message}```.
    Use this format: ```Language```"""
    # Get the language from the prompt
    language = get_prompt_language(prompt)

    prompt_ask = f"""You will be provided with text delimited by "<mess>" and "</mess>". Here is the text {message}.
    Make your response in {language}."""
    bot_response = get_prompt_response(prompt_ask)

    # Append the user's message to the chat conversation (optional)
    #incomes.append({
    #    "user": "User",
    #    "message": data['message']
    #})

    # Append the bot's response to the chat conversation (optional)
    # incomes.append({
    #     "user": "Bot",
    #     "message": bot_response
    # })

    # Return the bot response as a JSON object
    return jsonify({'bot_response': bot_response})

def get_prompt_response(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.4, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_prompt_language(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]