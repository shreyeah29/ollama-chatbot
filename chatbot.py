import subprocess

def ask_ollama(question):
    try:
        # Run the ollama model 'llama3.2:latest' with the question as input
        result = subprocess.run(
            ["ollama", "run", "llama3.2:latest", question],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def main():
    print("Welcome to your local Ollama Chatbot! Type 'exit' to quit.")
    while True:
        question = input("You: ").strip()
        if question.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        answer = ask_ollama(question)
        print(f"Bot: {answer}")

if __name__ == "__main__":
    main()
