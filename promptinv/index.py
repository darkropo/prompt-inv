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
    message = "<mess>"+data['message']+"</mess>"
    prompt = f"""You will be provided with text delimited by "<mess>" and "</mess>". """
    # Assuming you have a function that processes user messages and generates a bot response
    bot_response = get_prompt_response(prompt,message)

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
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]