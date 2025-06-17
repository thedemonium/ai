# Telegram Bot with CrewAI Integration

This project integrates a AI agent, powered by the `crewai` library and an Ollama LLM, with a Telegram bot. The bot can understand user messages and provide intelligent responses in Russian.

## Purpose

The primary goal is to create an interactive Telegram bot that leverages the capabilities of a `crewai` agent to engage in conversations. Each user message triggers the creation of a dedicated agent that processes the request and generates a response.

## Functionality (`telegram-bot.py` and `Docker/main.py`)

The core logic of the Telegram bot is implemented in `telegram-bot.py`. A version adapted for Docker deployment, `Docker/main.py`, offers the same functionality but accepts configuration via environment variables.

Key features include:

1.  **Message Handling:**
    *   The bot uses the `python-telegram-bot` library to listen for and handle incoming messages from users on the Telegram platform.

2.  **CrewAI Agent per Message:**
    *   For each new message received from a user, the bot dynamically creates a `crewai` agent.
    *   This agent is defined as an "interactive assistant" (`интерактивный ассистент`).
    *   Its predefined goal is to "provide comprehensive and informative answers to user questions, maintaining a friendly and helpful tone. The answer must be in Russian."
    *   The task assigned to the agent is based on the user's message content.

3.  **Ollama LLM Integration:**
    *   The `crewai` agent is configured to use a Large Language Model (LLM) served via an Ollama instance.
    *   The Ollama URL (e.g., `http://localhost:11434`) needs to be configured for the bot to connect to the LLM. The model used by the agent is also specified (e.g., `openhermes2.5-mistral-7b-4k`).

4.  **Response Generation:**
    *   The agent processes the user's message (as its task) and utilizes the Ollama LLM to generate a relevant and contextually appropriate response in Russian.
    *   This response is then sent back to the user via the Telegram chat.

5.  **Conversation Logging:**
    *   All interactions, including user messages and bot responses, are logged to a file named `dialog.txt`. This helps in tracking conversations and debugging.

## Docker Setup (`Telegram/Docker/`)

The `Telegram/Docker/` subdirectory provides a containerized solution for deploying the bot, ensuring a consistent environment.

*   **`Dockerfile`:**
    *   Defines the steps to build a Docker image for the bot.
    *   It starts from a Python base image, copies the application code, and installs the necessary Python dependencies listed in `requirements.txt`.

*   **`requirements.txt`:**
    *   Lists all Python packages required for the bot to run, such as `python-telegram-bot`, `crewai`, and `ollama`.
    *   These dependencies are installed during the Docker image build process.

*   **`compose.yaml` (formerly `docker-compose.yml`):**
    *   Defines a Docker Compose service for the Telegram bot.
    *   It specifies how to build the Docker image (using the `Dockerfile` in the current directory) and how to run the container.
    *   Crucially, it allows passing environment variables like `OLLAMA_BASE_URL` and `TELEGRAM_BOT_TOKEN` to the container, which are then used by `Docker/main.py`.

*   **`Docker/main.py`:**
    *   This is a version of the main bot script (`telegram-bot.py`) specifically adapted for Docker.
    *   It reads configuration parameters such as the Ollama base URL and the Telegram bot token from environment variables. This is a common practice for configuring applications in Docker containers, making the deployment more flexible and secure by not hardcoding sensitive information.

This Docker setup simplifies deployment and management of the Telegram bot, especially when moving between different environments.
