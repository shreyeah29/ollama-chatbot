from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import subprocess
import requests
from datetime import datetime
import json
import pytz

app = Flask(__name__)
CORS(app)

# Replace with your actual SerpAPI key
SERP_API_KEY = "7ebcd9ac0333f4c9c79d1dac8e93c2677b708231a383ea1ab92699769003cbd4"

# Local knowledge base (can extend as needed)
LOCAL_KB = [
    "Python is a high-level programming language.",
   "Flask is a lightweight web framework for Python.",
  "Ollama is a CLI to run LLM models locally.",
]

# Model Choice Prediction (MCP)
def choose_model_by_question(question):
    question_lower = question.lower()

    if any(word in question_lower for word in ['code', 'python', 'program', 'bug', 'error']):
        return "llama3.2:latest"
    elif any(word in question_lower for word in ['story', 'poem', 'creative', 'love']):
        return "llama3.2:latest"
    elif any(word in question_lower for word in ['quiz', 'fact', 'data']):
        return "phi:latest"
    elif any(word in question_lower for word in ['chat', 'hello', 'who are you']):
        return "tinyllama:latest"
    elif any(word in question_lower for word in ['latest', 'today', 'news', 'won', 'ipl', 'update']):
        return "neural-chat:latest"
    else:
        return "llama3.2:latest"

# Retrieve from local documents
def retrieve_local_docs(query):
    relevant = [doc for doc in LOCAL_KB if any(word in doc.lower() for word in query.lower().split())]
    return relevant if relevant else ["No local documents matched your query."]

# Retrieve from SerpAPI (real-time news and answers)
def retrieve_serpapi_snippet(query):
    try:
        response = requests.get(
            "https://serpapi.com/search",
            params={"q": query, "api_key": SERP_API_KEY, "engine": "google", "num": 3},
            timeout=5
        )
        results = response.json()
        answer_box = results.get("answer_box", {})
        if "answer" in answer_box:
            return answer_box["answer"]
        elif "snippet" in answer_box:
            return answer_box["snippet"]

        # Try organic results as fallback
        organic_results = results.get("organic_results", [])
        if organic_results:
            return organic_results[0].get("snippet", "No real-time info found.")
        return "No real-time info found."
    except Exception:
        return "Real-time web search failed."

# Combine local and real-time retrieval
def retrieve_docs(query):
    local_results = retrieve_local_docs(query)
    web_result = retrieve_serpapi_snippet(query)
    return local_results + [web_result]

# Helper to get current India time
def get_india_time():
    india_tz = pytz.timezone('Asia/Kolkata')
    now_india = datetime.now(india_tz)
    return now_india.strftime('%I:%M %p')  # e.g., "11:46 AM"
def get_ollama_response(messages):
    try:
        last_user_message = [msg['content'] for msg in messages if msg['role'] == 'user'][-1].strip()
        last_user_message_lower = last_user_message.lower()

        greetings = ['hi', 'hello', 'hey', 'good morning', 'good afternoon', 'good evening']
        if any(greet == last_user_message_lower for greet in greetings):
            return "Hello! How can I assist you today?"

        if 'time in india' in last_user_message_lower or 'india time' in last_user_message_lower:
            return f"The current time in India is {get_india_time()}."

        model_name = choose_model_by_question(last_user_message_lower)
        retrieved_docs = retrieve_docs(last_user_message)
        retrieval_context = "\n".join(retrieved_docs)

        system_instruction = (
            "You are Babybot, a helpful assistant.\n"
            "Use the following information to answer the user's question.\n"
            "Answer questions based on context and recent messages.\n"
            "If user asks about recent events, use real-time info.\n"
            "Keep responses short, accurate, and friendly.\n\n"
            "remember the previous questions and answer accordingly.\n"
            "When the user asks programming-related questions or coding problems, always:\n"
            "- Provide clean, properly indented code\n"
            "- Use triple backticks with the language (e.g., ```python)\n"
            "- Keep the code ready to run and easy to copy-paste\n"
            "- Add brief explanation only if needed, not long theory and provide with comments.\n\n"
            f"Context:\n{retrieval_context}\n\n"
            f"User: {last_user_message}\n"
            "Assistant:"
        )

        # ✅ Use localhost, enable streaming, and join parts
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model_name,
                "prompt": system_instruction,
                "stream": True
            },
            stream=True,
            timeout=120
        )

        final_response = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line)
                final_response += data.get("response", "")

        return final_response.strip()[:10000] + ("\n\n[Response truncated]" if len(final_response) > 10000 else "")

    except Exception as e:
        return f"Error: {str(e)}"

# Chat route
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    messages = data.get('messages', [])
    reply = get_ollama_response(messages)
    return jsonify({'response': reply})

# Home route
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')









