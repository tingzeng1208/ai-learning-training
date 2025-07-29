# Tool Agent Runner

This directory contains a tool agent that can use Google Search to help answer questions.

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up Environment Variables**:
   Make sure you have a `.env` file with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   GOOGLE_GENAI_MODEL=gemini-2.0-flash
   GOOGLE_GENAI_USE_VERTEXAI=FALSE
   ```

## Usage

### Interactive Mode
Run the agent in interactive mode where you can have a conversation:

```bash
python runagent.py
```

This will start an interactive session where you can type questions and get responses from the agent.

### Single Query Mode
Run the agent with a single query:

```bash
python runagent.py "What is the current weather in New York?"
```

The agent will process your query and provide a response using Google Search if needed.

## Features

- **Google Search Integration**: The agent can search the web to find current information
- **Interactive Session**: Have a conversation with the agent
- **Single Query Support**: Run one-off queries from the command line
- **Error Handling**: Graceful handling of errors and interruptions

## Example Queries

- "What are the latest news about AI?"
- "Find information about Python programming best practices"
- "Search for recent developments in machine learning"
- "What is the current stock price of Apple?"

## Agent Capabilities

The tool agent is configured with:
- **Model**: Gemini 2.0 Flash
- **Tools**: Google Search
- **Additional Tools**: Current time function (commented out)

## Troubleshooting

1. **Missing API Key**: Make sure your `GOOGLE_API_KEY` is set in the `.env` file
2. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
3. **Permission Issues**: Make sure the script has execute permissions

## Exit Commands

In interactive mode, you can exit using:
- `quit`
- `exit`
- `bye`
- `q`
- `Ctrl+C`
