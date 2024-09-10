# Flask Chat App with OpenAI Integration

This Flask app is designed to interact with the OpenAI API. It allows users to send prompts via the `/chat` endpoint, and the app will return a response based on the provided prompt using OpenAI's GPT model. CORS is enabled to allow cross-origin requests.

## Features
- `/`: A simple "Hello, World!" route.
- `/chat`: A POST endpoint to send prompts to the OpenAI API and receive responses.
- `/health`: A health check endpoint that returns "OK" with a 200 status code.

## Requirements
- Python 3.x
- Flask
- Flask-CORS
- OpenAI API Key

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/everfields/thebest-flask.git
    cd thebest-flask
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file and add your OpenAI API key:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    ```

5. Run the app:
    ```bash
    python app.py
    ```

## API Endpoints

### 1. `GET /`
Returns a simple message:

**Response:**
```plaintext
Hello, World!
```

### 2. `POST /chat`
Send a prompt to the OpenAI API and receive a response.

**Request:**
```json
{
  "prompt": "What is the best fruit?"
}
```

**Response:**
```json
{
  "result": "Mango"
}
```

### 3. `GET /health`
A simple health check endpoint that returns:

**Response:**
```plaintext
OK
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
