# from flask import Flask, render_template, request, jsonify, session
# import subprocess
# import os

# app = Flask(__name__)
# app.secret_key = os.urandom(24)  # For session management

# def get_ollama_response(messages, model_name):
#     try:
#         system_instruction = (
#             "You are a helpful assistant. "
#             "You understand common Indian city short forms like hyd for Hyderabad, blr for Bangalore, etc. "
#             "Be clear, concise, and organized.\n"
#         )

#         prompt = system_instruction
#         for msg in messages:
#             role = msg['role']
#             content = msg['content']
#             prompt += f"{'User' if role == 'user' else 'Assistant'}: {content}\n"
#         prompt += "Assistant:"

#         result = subprocess.run(
#             ["ollama", "run", model_name, prompt],
#             capture_output=True,
#             text=True,
#             timeout=60
#         )

#         return result.stdout.strip()[:10000]  # truncate if needed

#     except Exception as e:
#         return f"Error: {str(e)}"


# @app.route('/')
# def index():
#     # Initialize chat history in session if not present
#     if 'chat_history' not in session:
#         session['chat_history'] = []
#     return render_template('index.html')

# @app.route('/ask', methods=['POST'])
# def ask():
#     data = request.get_json(force=True)
#     question = data.get('question', '').strip()
#     model = data.get('model', 'llama3:latest')  # default fallback

#     if not question:
#         return jsonify({'error': 'Empty question'}), 400

#     # Load chat history from session
#     chat_history = session.get('chat_history', [])

#     # Append user's question
#     chat_history.append({'role': 'user', 'content': question})

#     # Get AI response with selected model
#     answer = get_ollama_response(chat_history, model)

#     # Append AI's answer to history
#     chat_history.append({'role': 'assistant', 'content': answer})

#     # Save back to session
#     session['chat_history'] = chat_history

#     return jsonify({'answer': answer})


# @app.route('/reset', methods=['POST'])
# def reset():
#     session.pop('chat_history', None)
#     return jsonify({'status': 'reset'})

# if __name__ == '__main__':
#     app.run(debug=True)

















# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from flask import Flask, render_template
# import subprocess

# app = Flask(__name__)
# CORS(app)

# # Auto-select best model based on user message content
# def choose_model_by_question(question):
#     question_lower = question.lower()

#     # Basic keyword-based model selection
#     if any(keyword in question_lower for keyword in ['code', 'python', 'bug', 'error', 'function', 'logic', 'program']):
#         return "codellama:latest"
#     elif any(keyword in question_lower for keyword in ['story', 'poem', 'summarize', 'explain', 'talk', 'write', 'love']):
#         return "gemma:latest"
#     elif any(keyword in question_lower for keyword in ['ai', 'news', 'latest', 'technology', 'analysis', 'world']):
#         return "mistral:latest"
#     else:
#         return "llama3:latest"  # default fallback

# # Handle the chat interaction
# def get_ollama_response(messages):
#     try:
#         # System-level prompt instruction
#         system_instruction = (
#             "You are a helpful assistant. "
#             "You understand common Indian city short forms like hyd for Hyderabad. "
#             "Answer concisely using lists or line breaks. Avoid large paragraphs.\n"
#         )

#         # Build full prompt history
#         prompt = system_instruction
#         for msg in messages:
#             role = msg['role']
#             content = msg['content']
#             prompt += f"{'User' if role == 'user' else 'Assistant'}: {content}\n"
#         prompt += "Assistant:"

#         # Pick model based on most recent user message
#         last_question = [msg['content'] for msg in messages if msg['role'] == 'user'][-1]
#         model_name = choose_model_by_question(last_question)

#         # Call the appropriate model via ollama
#         result = subprocess.run(
#             ["ollama", "run", model_name, prompt],
#             capture_output=True,
#             text=True,
#             timeout=60
#         )

#         answer = result.stdout.strip()
#         return answer[:10000] + ("\n\n[Response truncated]" if len(answer) > 10000 else "")

#     except Exception as e:
#         return f"Error: {str(e)}"

# # API endpoint for handling chat
# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.get_json()
#     messages = data.get('messages', [])
#     reply = get_ollama_response(messages)
#     return jsonify({'response': reply})

# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)






# from flask import Flask, request, jsonify, render_template
# from flask_cors import CORS
# import subprocess

# app = Flask(__name__)
# CORS(app)

# def choose_model_by_question(question):
#     question = question.lower()
    
#     if any(word in question for word in ['code', 'function', 'bug', 'debug', 'error', 'python', 'logic', 'program', 'build']):
#         return 'codellama:latest'
#     elif any(word in question for word in ['poem', 'story', 'write', 'romantic', 'love', 'sad', 'happy', 'lyrics']):
#         return 'gemma:latest'
#     elif any(word in question for word in ['news', 'current', 'latest', 'analysis', 'world', 'tech']):
#         return 'mistral:latest'
#     elif any(word in question for word in ['llama3.2', 'simple', 'chat', 'babybot', 'general']):
#         return 'llama3.2:latest'
#     else:
#         return 'llama3:latest'  # fallback

# def get_ollama_response(messages):
#     try:
#         # Build the prompt with a base instruction
#         system_prompt = "You are Babybot, a smart assistant that replies in clear, helpful, and concise format.\n"
#         prompt = system_prompt
#         for msg in messages:
#             prompt += f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}\n"
#         prompt += "Assistant:"

#         last_user_message = [msg['content'] for msg in messages if msg['role'] == 'user'][-1]
#         model = choose_model_by_question(last_user_message)

#         result = subprocess.run(
#             ["ollama", "run", model, prompt],
#             capture_output=True,
#             text=True,
#             timeout=60
#         )

#         return result.stdout.strip()[:10000]
#     except Exception as e:
#         return f"Error: {str(e)}"

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.get_json()
#     messages = data.get('messages', [])
#     reply = get_ollama_response(messages)
#     return jsonify({'response': reply})

# @app.route('/reset', methods=['POST'])
# def reset():
#     return jsonify({'message': 'Chat reset'})

# if __name__ == '__main__':
#     app.run(debug=True)












# ok good
# from flask import Flask, render_template, request, jsonify
# import subprocess

# app = Flask(__name__)

# # === MODEL CHOOSER ===
# def choose_model_by_question(user_input):
#     user_input = user_input.lower()

#     if any(kw in user_input for kw in ['code', 'python', 'java', 'error', 'bug', 'html', 'css', 'javascript']):
#         return "tinyllama"
#     elif any(kw in user_input for kw in ['poem', 'story', 'write', 'creative']):
#         return "phi"
#     elif any(kw in user_input for kw in ['ai', 'explain', 'what is', 'define']):
#         return "neural-chat"
#     else:
#         return "tinyllama"

# # === OLLAMA CALLER ===
# def get_ollama_response(messages):
#     try:
#         user_input = messages[-1]['content']
#         selected_model = choose_model_by_question(user_input)

#         result = subprocess.run(
#             ["ollama", "run", selected_model],
#             input=user_input,
#             capture_output=True,
#             text=True,
#             timeout=60
#         )

#         reply = result.stdout.strip()
#         return reply if reply else "Hmm... I didn't catch that."

#     except Exception as e:
#         return f"Error: {str(e)}"

# # === ROUTES ===
# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_message = request.json.get("message")
#     messages = [{"role": "user", "content": user_message}]
#     bot_reply = get_ollama_response(messages)
#     return jsonify({"reply": bot_reply})

# if __name__ == "__main__":
#     app.run(debug=True)









# ok


# from flask import Flask, request, jsonify, render_template
# from flask_cors import CORS
# import subprocess

# app = Flask(__name__)
# CORS(app)

# # Model Choice Prediction (MCP) function based on user input keywords
# def choose_model_by_question(question):
#     question_lower = question.lower()

#     if any(keyword in question_lower for keyword in ['code', 'python', 'bug', 'error', 'function', 'logic', 'program']):
#         return "codellama:latest"
#     elif any(keyword in question_lower for keyword in ['story', 'poem', 'summarize', 'explain', 'talk', 'write', 'love']):
#         return "gemma:latest"
#     elif any(keyword in question_lower for keyword in ['ai', 'news', 'latest', 'technology', 'analysis', 'world']):
#         return "mistral:latest"
#     else:
#         # fallback to llama3.2 since it's smallest and versatile
#         return "llama3.2:latest"

# def get_ollama_response(messages):
#     try:
#         system_instruction = (
#             "You are a helpful assistant. "
#             "You will give fast replies"
#             "Answer concisely using lists or line breaks. Avoid large paragraphs.\n"
#         )

#         prompt = system_instruction
#         for msg in messages:
#             role = msg['role']
#             content = msg['content']
#             prompt += f"{'User' if role == 'user' else 'Assistant'}: {content}\n"
#         prompt += "Assistant:"

#         # Pick model based on last user message
#         last_user_message = [msg['content'] for msg in messages if msg['role'] == 'user'][-1]
#         model_name = choose_model_by_question(last_user_message)

#         # Run Ollama CLI with the chosen model
#         result = subprocess.run(
#             ["ollama", "run", model_name, prompt],
#             capture_output=True,
#             text=True,
#             timeout=60
#         )

#         answer = result.stdout.strip()
#         return answer[:10000] + ("\n\n[Response truncated]" if len(answer) > 10000 else "")

#     except Exception as e:
#         return f"Error: {str(e)}"

# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.get_json()
#     messages = data.get('messages', [])
#     reply = get_ollama_response(messages)
#     return jsonify({'response': reply})

# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)

















#  MCP DONE
# from flask import Flask, request, jsonify, render_template
# from flask_cors import CORS
# import subprocess

# app = Flask(__name__)
# CORS(app)

# # 🔁 Model Choice Prediction (MCP) logic based on question type
# def choose_model_by_question(question):
#     question_lower = question.lower()

#     if any(keyword in question_lower for keyword in ['code', 'python', 'bug', 'function', 'logic', 'program', 'error']):
#         return "llama3.2:latest"
#     elif any(keyword in question_lower for keyword in ['story', 'poem', 'write', 'novel', 'creative', 'rhymes', 'love']):
#         return "llama3.2:latest"
#     elif any(keyword in question_lower for keyword in ['short', 'fact', 'answer', 'data', 'quiz', 'define',]):
#         return "phi:latest"
#     elif any(keyword in question_lower for keyword in ['chat', 'hello', 'how are you', 'talk', 'who are you', 'babybot']):
#         return "tinyllama:latest"
#     elif any(keyword in question_lower for keyword in ['what','fast', 'quick', 'light', 'respond fast']):
#         return "neural-chat:latest"
#     else:
#         return "llama3.2:latest"  # safe fallback model

# # 🔁 Construct prompt and get model response from Ollama
# def get_ollama_response(messages):
#     try:
#         system_instruction = (
#             "You are Babybot, a helpful assistant.\n"
#             "Respond clearly, quickly, and concisely.\n"
#             "Use short lists or line breaks. Avoid long paragraphs.\n"
#         )

#         prompt = system_instruction
#         for msg in messages:
#             role = msg['role']
#             content = msg['content']
#             prompt += f"{'User' if role == 'user' else 'Assistant'}: {content}\n"
#         prompt += "Assistant:"

#         last_user_message = [msg['content'] for msg in messages if msg['role'] == 'user'][-1]
#         model_name = choose_model_by_question(last_user_message)

#         result = subprocess.run(
#             ["ollama", "run", model_name, prompt],
#             capture_output=True,
#             text=True,
#             timeout=120
#         )

#         answer = result.stdout.strip()
#         return answer[:10000] + ("\n\n[Response truncated]" if len(answer) > 10000 else "")

#     except Exception as e:
#         return f"Error: {str(e)}"

# # 🔁 API route
# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.get_json()
#     messages = data.get('messages', [])
#     reply = get_ollama_response(messages)
#     return jsonify({'response': reply})

# # 🔁 Home route
# @app.route('/')
# def home():
#     return render_template('index.html')

# # 🔁 Main entry
# if __name__ == '__main__':
#     app.run(debug=True)














# from flask import Flask, request, jsonify, render_template
# from flask_cors import CORS
# import subprocess
# import requests

# app = Flask(__name__)
# CORS(app)

# # Local knowledge base (replace or extend as needed)
# LOCAL_KB = [
#     "Python is a high-level programming language.",
#     "Flask is a lightweight web framework for Python.",
#     "Ollama is a CLI to run LLM models locally.",
# ]

# # Model Choice Prediction (MCP) logic based on question type
# def choose_model_by_question(question):
#     question_lower = question.lower()

#     if any(keyword in question_lower for keyword in ['code', 'python', 'bug', 'function', 'logic', 'program', 'error']):
#         return "llama3.2:latest"
#     elif any(keyword in question_lower for keyword in ['story', 'poem', 'write', 'novel', 'creative', 'rhymes', 'love']):
#         return "llama3.2:latest"
#     elif any(keyword in question_lower for keyword in ['short', 'fact', 'answer', 'data', 'quiz', 'define']):
#         return "phi:latest"
#     elif any(keyword in question_lower for keyword in ['chat', 'hello', 'how are you', 'talk', 'who are you', 'babybot']):
#         return "tinyllama:latest"
#     elif any(keyword in question_lower for keyword in ['what', 'fast', 'quick', 'light', 'respond fast']):
#         return "neural-chat:latest"
#     else:
#         return "llama3.2:latest"  # safe fallback model

# # Simple local document retriever
# def retrieve_local_docs(query):
#     relevant = [doc for doc in LOCAL_KB if any(word in doc.lower() for word in query.lower().split())]
#     return relevant if relevant else ["Sorry, no local documents matched your query."]

# # Web snippet retriever using DuckDuckGo Instant Answer API
# def retrieve_web_snippet(query):
#     try:
#         res = requests.get("https://api.duckduckgo.com/",
#                            params={"q": query, "format": "json", "no_redirect": 1, "skip_disambig": 1},
#                            timeout=3)
#         data = res.json()
#         snippet = data.get('AbstractText', '') or data.get('Answer', '')
#         return snippet if snippet else "No relevant web info found."
#     except Exception:
#         return "Web search failed."

# # Combine local + web retrieval
# def retrieve_docs(query):
#     local_results = retrieve_local_docs(query)
#     web_result = retrieve_web_snippet(query)
#     return local_results + [web_result]

# # Construct prompt and get response from Ollama with retrieval context
# def get_ollama_response(messages):
#     try:
#         last_user_message = [msg['content'] for msg in messages if msg['role'] == 'user'][-1]
#         model_name = choose_model_by_question(last_user_message)

#         # Retrieve relevant context
#         retrieved_docs = retrieve_docs(last_user_message)
#         retrieval_context = "\n".join(retrieved_docs)

#         system_instruction = (
#             "You are Babybot, a helpful assistant.\n"
#             "Use the following information to answer the user's question.\n"
#             "Answer questions based on context and recent messages.\n"
#             "If user asks about recent events, try to use retrieved info or search results.\n"
#             "Respond clearly, quickly, and concisely.\n"
#             "Remember previous conversation and answer accordingly.\n"
#             "Use short lists or line breaks. Avoid long paragraphs.\n\n"
#             f"Context:\n{retrieval_context}\n\n"
#             f"User: {last_user_message}\n"
#             "Assistant:"
#         )

#         result = subprocess.run(
#             ["ollama", "run", model_name, system_instruction],
#             capture_output=True,
#             text=True,
#             timeout=120
#         )

#         answer = result.stdout.strip()
#         return answer[:10000] + ("\n\n[Response truncated]" if len(answer) > 10000 else "")

#     except Exception as e:
#         return f"Error: {str(e)}"

# # API route
# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.get_json()
#     messages = data.get('messages', [])
#     reply = get_ollama_response(messages)
#     return jsonify({'response': reply})

# # Home route
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Main entry point
# if __name__ == '__main__':
#     app.run(debug=True, port=5001)










# from flask import Flask, request, jsonify, render_template
# from flask_cors import CORS
# import subprocess
# import requests

# app = Flask(__name__)
# CORS(app)

# # Local knowledge base (replace or extend as needed)
# LOCAL_KB = [
#     "Python is a high-level programming language.",
#     "Flask is a lightweight web framework for Python.",
#     "Ollama is a CLI to run LLM models locally.",
# ]

# # Model Choice Prediction (MCP) logic based on question type
# def choose_model_by_question(question):
#     question_lower = question.lower()

#     if any(keyword in question_lower for keyword in ['code', 'python', 'bug', 'function', 'logic', 'program', 'error']):
#         return "llama3.2:latest"
#     elif any(keyword in question_lower for keyword in ['story', 'poem', 'write', 'novel', 'creative', 'rhymes', 'love']):
#         return "llama3.2:latest"
#     elif any(keyword in question_lower for keyword in ['short', 'fact', 'answer', 'data', 'quiz', 'define']):
#         return "phi:latest"
#     elif any(keyword in question_lower for keyword in ['chat', 'hello', 'how are you', 'talk', 'who are you', 'babybot']):
#         return "tinyllama:latest"
#     elif any(keyword in question_lower for keyword in ['what', 'fast', 'quick', 'light', 'respond fast']):
#         return "neural-chat:latest"
#     else:
#         return "llama3.2:latest"  # safe fallback model

# # Simple local document retriever
# def retrieve_local_docs(query):
#     relevant = [doc for doc in LOCAL_KB if any(word in doc.lower() for word in query.lower().split())]
#     return relevant if relevant else ["Sorry, no local documents matched your query."]

# # Web snippet retriever using DuckDuckGo Instant Answer API
# def retrieve_web_snippet(query):
#     try:
#         res = requests.get("https://api.duckduckgo.com/",
#                            params={"q": query, "format": "json", "no_redirect": 1, "skip_disambig": 1},
#                            timeout=3)
#         data = res.json()
#         snippet = data.get('AbstractText', '') or data.get('Answer', '')
#         return snippet if snippet else "No relevant web info found."
#     except Exception:
#         return "Web search failed."

# # Combine local + web retrieval
# def retrieve_docs(query):
#     local_results = retrieve_local_docs(query)
#     web_result = retrieve_web_snippet(query)
#     return local_results + [web_result]

# # Construct prompt and get response from Ollama with retrieval context and full conversation
# # def get_ollama_response(messages):
# #     try:
# #         if not messages or all(msg.get('role') != 'user' for msg in messages):
# #             return "No user messages found."

# #         last_user_message = [msg['content'] for msg in messages if msg['role'] == 'user'][-1]
# #         model_name = choose_model_by_question(last_user_message)

# #         retrieved_docs = retrieve_docs(last_user_message)
# #         retrieval_context = "\n".join(retrieved_docs) if retrieved_docs else "No relevant context found."

# #         system_instruction = (
# #             "You are Babybot, a helpful assistant.\n"
# #             "Use the following information to answer the user's question.\n"
# #             "Answer questions based on context and recent messages.\n"
# #             "If user asks about recent events, try to use retrieved info or search results.\n"
# #             "Respond clearly, quickly, and concisely.\n"
# #             "Remember previous conversation and answer accordingly.\n"
# #             "Use short lists or line breaks. Avoid long paragraphs.\n\n"
# #             f"Context:\n{retrieval_context}\n\n"
# #         )

# #         # Build conversation history in prompt format
# #         conversation_history = ""
# #         for msg in messages:
# #             role = "User" if msg['role'] == 'user' else "Assistant"
# #             conversation_history += f"{role}: {msg['content']}\n"

# #         prompt = system_instruction + conversation_history + "Assistant:"

# #         result = subprocess.run(
# #             ["ollama", "run", model_name, prompt],
# #             capture_output=True,
# #             text=True,
# #             timeout=120
# #         )

# #         answer = result.stdout.strip()
# #         return answer[:10000] + ("\n\n[Response truncated]" if len(answer) > 10000 else "")

# #     except Exception as e:
# #         return f"Error: {str(e)}"


# def get_ollama_response(messages):
#     try:
#         if not messages or all(msg.get('role') != 'user' for msg in messages):
#             return "No user messages found."

#         last_user_message = [msg['content'] for msg in messages if msg['role'] == 'user'][-1]
#         model_name = choose_model_by_question(last_user_message)

#         retrieved_docs = retrieve_docs(last_user_message)
#         retrieval_context = "\n".join(retrieved_docs) if retrieved_docs else "No relevant context found."

#         system_instruction = (
#             "You are Babybot, a helpful assistant.\n"
#             "Answer user questions clearly and concisely.\n"
#             "Use retrieved context only to improve accuracy.\n"
#             "Avoid lengthy explanations or unrelated content.\n"
#             "If unsure, say you don't know instead of guessing.\n"
#             "Use short sentences or bullet points.\n\n"
#             f"Context:\n{retrieval_context}\n\n"
#         )

#         # Use only last 6 messages to limit prompt size and confusion
#         recent_msgs = messages[-6:]
#         conversation_history = ""
#         for msg in recent_msgs:
#             role = "User" if msg['role'] == 'user' else "Assistant"
#             conversation_history += f"{role}: {msg['content']}\n"

#         prompt = system_instruction + conversation_history + "Assistant:"

#         result = subprocess.run(
#             ["ollama", "run", model_name, prompt],
#             capture_output=True,
#             text=True,
#             timeout=120
#         )

#         answer = result.stdout.strip()
#         return answer[:10000] + ("\n\n[Response truncated]" if len(answer) > 10000 else "")

#     except Exception as e:
#         return f"Error: {str(e)}"

# # API route
# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.get_json()
#     messages = data.get('messages', [])
#     reply = get_ollama_response(messages)
#     return jsonify({'response': reply})

# # Home route
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Main entry point
# if __name__ == '__main__':
#     app.run(debug=True, port=5001)










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









