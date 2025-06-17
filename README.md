# AI Projects Repository

This repository contains a collection of AI-related projects, including:

* **CrewAI Agent Examples:** This section showcases examples of autonomous agents built using the CrewAI framework. These examples demonstrate various capabilities and use cases of CrewAI agents.
    * `CrewAI/crewai-local-expert.py`
    * `CrewAI/crewai-system-administrator.py`

* **Local AI Voice Chat Assistant:** This project implements a voice chat assistant that runs locally. It allows users to interact with an AI model using voice commands and receive spoken responses.
    * `LocalAIVoiceChat/`

* **Telegram Bot:** This project features a Telegram bot integrated with AI functionalities. The bot can interact with users on the Telegram platform, providing AI-powered responses and services.
    * `Telegram/`

The code within this repository may consist of code from other developers, which has been tailored to fulfill specific requirements. Each project directory may contain its own README file with more detailed information about that specific project.

## Core Technologies Used

This repository utilizes a variety of technologies and libraries to power its AI projects:

*   **Python:** The primary programming language used for developing all the projects.
*   **Ollama:** Employed for running and managing local Large Language Models (LLMs), providing the core intelligence for the AI agents and assistants.
*   **CrewAI:** A framework used for orchestrating autonomous AI agents, enabling them to collaborate on complex tasks. This is notably used in the `CrewAI` and `Telegram` projects.
*   **RealtimeTTS/RealtimeSTT:** These or similar Python libraries are used in the `LocalAIVoiceChat` project for real-time Speech-to-Text (STT) and Text-to-Speech (TTS) functionalities, enabling voice-based interaction.
*   **llama_cpp (via `llama-cpp-python`):** Python bindings for `llama.cpp`, used in the `LocalAIVoiceChat` project (`main_local.py`) to run Llama family models directly on local hardware.
*   **python-telegram-bot:** The library used to create and manage the Telegram bot in the `Telegram` project, handling communication with the Telegram API.
*   **Docker:** Used in the `Telegram` project for containerizing the bot application, including its dependencies and runtime environment, ensuring consistent deployment.
