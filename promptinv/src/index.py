from flask import Flask, jsonify, request, render_template
import openai
import os
from flask import send_from_directory
from dotenv import load_dotenv, find_dotenv
from src.dataprocess import *

_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

app = Flask(__name__, template_folder='../templates', static_folder='../static' )
app.use_static = True
@app.route('/')
def index():
    return render_template('index.html')


# Handle the GET request for the CSS file
@app.route('/static/css/<path:filename>')
def get_css(filename):
    return send_from_directory('../static/css', filename)

# Handle the GET request for the JavaScript file
@app.route('/static/js/<path:filename>')
def get_js(filename):
    return send_from_directory('../static/js', filename)
# Handle the GET request for the JavaScript file
@app.route('/static/files/<path:filename>')
def get_files(filename):
    return send_from_directory('../static/files', filename)

@app.route('/botchat', methods=['POST'])
def process_user_message():
    # Get the data from the request body
    chat_data = request.get_json()
    message = chat_data['message']
    prompt = f"""Tell me which language this is ```{message}```.
    Use this format: ```Language```"""
    # Get the language from the prompt
    language = get_prompt_language(prompt)

    #convert to json data for the chat
    #json_data = convert_csv_to_json()
    
    prompt_ask = f"""{message}.
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
