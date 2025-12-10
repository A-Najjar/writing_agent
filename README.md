# Writing Agent

## Overview
The Writing Agent is an AI-powered research assistant designed to help users gather structured information on any topic. By leveraging advanced language models and tools, the agent provides concise summaries, sources, and insights, making it an invaluable tool for researchers, students, and professionals.

## Features
- **Interactive Streamlit Web Interface**: A user-friendly interface to interact with the AI agent.
- **Structured Research Output**: Provides topic summaries, sources, and tools used.
- **Tool Integration**: Utilizes tools like DuckDuckGo search, Wikipedia queries, and file-saving capabilities.
- **Customizable**: Easily extendable to include additional tools or modify the agent's behavior.

## Installation

### Prerequisites
- Python 3.8 or higher
- `pip` (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/A-Najjar/writing_agent.git
   cd writing_agent
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Copy the `sample.env` file to `.env`:
     ```bash
     cp sample.env .env
     ```
   - Add your API keys for OpenAI and Anthropic in the `.env` file:
     ```plaintext
     OPENAI_API_KEY="your_openai_api_key"
     ANTHROPIC_API_KEY="your_anthropic_api_key"
     ```

## Usage

### Running the Streamlit App
1. Start the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```
2. Open the app in your browser (usually at `http://localhost:8501`).
3. Enter your research topic and click "Run Research" to get structured results.

### Example Output
- **Topic**: Artificial Intelligence
- **Summary**: AI refers to the simulation of human intelligence in machines that are programmed to think and learn.
- **Sources**:
  - [Wikipedia](https://en.wikipedia.org/wiki/Artificial_intelligence)
  - [DuckDuckGo Search Results](https://duckduckgo.com)
- **Tools Used**: search, wiki_tool

## File Structure
```
writing_agent/
├── main.py               # Entry point for the agent
├── tools.py              # Custom tools for the agent
├── streamlit_app.py      # Streamlit web interface
├── requirements.txt      # Python dependencies
├── sample.env            # Environment variable template
├── README.md             # Project documentation
```

## Extending the Agent
To add new tools or modify the agent's behavior:
1. Define a new tool in `tools.py`.
2. Import and include the tool in the `tools` list in `main.py`.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- [LangChain](https://github.com/hwchase17/langchain) for the agent framework.
- [Streamlit](https://streamlit.io/) for the web interface.

- OpenAI and Anthropic for their powerful language models.
