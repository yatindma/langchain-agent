# main.py
from agent import initialize_agent, run_agent
#load env
from dotenv import load_dotenv
load_dotenv()

def main():
    print("Welcome to the AI agent service. Type 'quit' to exit.")
    agent = initialize_agent()
    while True:
        user_input = input("Enter your query: ")
        if user_input.lower() == 'quit':
            break
        response = run_agent(agent, user_input)
        print("AI Response:", response['output'])

if __name__ == "__main__":
    main()
