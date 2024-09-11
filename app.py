from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS library
import openai
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

# Configure OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get('prompt')
    
    # Ensure we have a valid prompt
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    messages = [
        {"role": "system", "content": "You are gonna be provided of a category. Choose the best element of that given category. Anything else. No explanations. Make your calculations and provide the result."},
        {"role": "user", "content": prompt}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Replace with the appropriate model as needed
            messages=messages,
            max_tokens=150
        )
        result = response.choices[0].message['content'].strip()
        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Open to all IPs

@app.route('/health')
def health_check():
    return "OK", 200