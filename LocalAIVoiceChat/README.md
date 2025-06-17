# Local AI Voice Chat

This Python application enables real-time voice conversations with an AI assistant. It integrates Speech-to-Text (STT), Text-to-Speech (TTS), and Large Language Model (LLM) functionalities to create an interactive voice experience.

## Purpose

The primary goal of this project is to allow users to have fluid, real-time spoken conversations with an AI. The system listens to user speech, transcribes it to text, sends it to an LLM for a response, and then converts the LLM's text response back into speech for the user to hear.

## Core Components

The application is built around the following core components:

*   **Speech-to-Text (STT):** Converts spoken audio from the user into text. The `AudioToTextRecorder` class is responsible for this.
*   **Text-to-Speech (TTS):** Converts textual responses from the LLM into audible speech. The `TextToAudioStream` and `SystemEngine` classes handle this.
*   **Large Language Model (LLM) Interaction:** This is the brain of the assistant. The application sends the transcribed user input to an LLM and receives a textual response.

## Variants

The project offers two main variants for LLM interaction:

1.  **`main_local.py` (Local LLM Inference with `llama_cpp`):**
    *   This script utilizes the `llama_cpp` library to run LLMs locally on the user's machine.
    *   It's suitable for users who have a compatible LLM model downloaded and prefer to keep the inference process entirely offline.

2.  **`main_ollama.py` (Ollama API for LLM Inference):**
    *   This script interacts with an LLM through an Ollama API endpoint.
    *   Ollama provides a convenient way to run various open-source LLMs. This variant is useful if you have an Ollama server running (either locally or remotely) and want to connect to it.

## Configuration

The behavior of the voice chat assistant can be customized using JSON configuration files:

*   **`creation_params.json`:** Likely defines parameters for the initial setup or creation of AI models or resources.
*   **`completion_params.json`:** Contains settings related to how the LLM generates completions (e.g., temperature, max tokens).
*   **`chat_params.json`:** Stores parameters specific to the chat interaction itself (e.g., system prompts, user/assistant personas).

By modifying these files, users can tailor the AI's responses, voice characteristics, and overall interaction style.

## Ollama Reference

*   **`ollama_reference_code.py`:** This script serves as a basic client or example code for interacting with the Ollama API. It can be helpful for understanding how to send requests and receive responses from an Ollama server directly.

## Additional Features

*   **Dynamic Prompt Templating:** Prompts and responses can be customized by replacing placeholders in real-time with character names, user names, and scenarios.
*   **Conversation History Management:** The context of the entire previous dialogue with the user is maintained to ensure coherent conversations.
*   **Logging:** The Python logging module is used for application logging, which is helpful for debugging and monitoring.

[Installation Instructions](installation.md)
