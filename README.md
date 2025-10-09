# Simple Decimal Misconceptions Chatbot

A simple chatbot application that simulates a 13-year-old student struggling with decimal concepts, built with Streamlit and OpenAI.

## Features

- 🔐 **Login System**: Secure login with identifier validation
- 🤖 **AI Chatbot**: Interactive chatbot using the decimal misconceptions prompt
- 💬 **Chat Interface**: Clean, modern chat interface with streaming responses
- 📊 **Session Management**: Tracks conversation history and response limits

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Secrets**:
   Update `.streamlit/secrets.toml` with your API keys:
   ```
   OPENAI_API_KEY = "your-openai-api-key"
   MONGODB_CONNECTION_STRING = "your-mongodb-connection-string"
   ```

3. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Login**: Enter a valid identifier (3+ characters) to access the chatbot
2. **Chat**: Ask questions about decimals and interact with the AI student
3. **Logout**: Click the logout button to end your session

## Architecture

- `app.py`: Main application with login and chat functionality
- `utils/mongodb.py`: Database utilities for identifier validation
- `requirements.txt`: Python dependencies
- `.streamlit/secrets.toml`: Configuration secrets

## Notes

- The chatbot uses the prompt from `../prompts/prompt.txt`
- Maximum 50 responses per session
- MongoDB connection is optional - falls back to simple validation if unavailable
