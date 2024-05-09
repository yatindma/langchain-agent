# AI Agent Service

This project is an AI agent service that uses the LangChain library to create a React-based agent. The agent is capable of answering queries by utilizing two tools: a keyword search tool and a calculator tool. The keyword search tool searches a database for relevant information based on the keywords extracted from the query, and the calculator tool performs mathematical calculations.

## Prerequisites

Before running the AI agent service, ensure you have the following prerequisites installed:

- Python 3.9+
- Required Python packages listed in the `requirements.txt` file
- An .env file containing your OpenAI API key (if using OpenAI as the language model)

You can install the required packages using the following command:

```
pip install -r requirements.txt
```

Additionally, you need to create an .env file in the project root directory with the following content:

```

OPENAI_API_KEY=your_openai_api_key_here

```
## Project Structure

The project consists of the following files:

1. `tools.py`: This file defines the `KeywordSearchTool` and `Calculator` classes, which are the tools used by the agent.
2. `agent.py`: This file contains functions to initialize and run the AI agent.
3. `main.py`: This is the entry point of the application, where the agent is initialized and the user interacts with it.
4. `database.py`: This file is responsible for setting up the database and providing a search function for the keyword search tool.
5. `wiki-cancer.txt`: This is a text file containing information about cancer, which serves as the database for the keyword search tool.
6. `requirements.txt`: This file lists the required Python packages and their versions.

## Usage

1. Ensure that you have installed the required Python packages by running the following command:

```
pip install -r requirements.txt
```

2. Run the `main.py` file to start the AI agent service:

```
python main.py
```

3. The application will prompt you with the message "Welcome to the AI agent service. Type 'quit' to exit."

4. Enter your query, and the agent will respond with the appropriate answer based on the tools it has available.

5. To exit the application, type `quit` and press Enter.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is not licensed under any specific license.

## Acknowledgments

This project utilizes the following open-source libraries:

- [LangChain](https://github.com/hwchase17/langchain)
- [Chroma](https://github.com/chroma-core/chroma)
- [Sentence-Transformers](https://github.com/UKPLab/sentence-transformers)