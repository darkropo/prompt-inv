from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

incomes = [
    { 'description': 'salary', 'amount': 5000 }
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/botchat')
def get_botchat():
    return jsonify(incomes)
