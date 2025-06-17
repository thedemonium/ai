# CrewAI Project: AI Agent Crews

This project showcases examples of AI agent crews built using the `crewai` library. These examples demonstrate how multiple AI agents can collaborate to perform complex tasks. The agents leverage Large Language Models (LLMs) for their intelligence, in these cases, by connecting to an Ollama instance. Task outputs from the crews can be saved to files for review.

## `crewai-local-expert.py`

This script defines a crew of AI agents designed to research and write about a specific topic. In this particular example, the crew focuses on generating content about **St. Petersburg, Russia**.

**Purpose:** To demonstrate a simple research and writing workflow where agents with different specializations collaborate.

**Agents and their Roles:**

1.  **Researcher Agent (`local_expert`):**
    *   **Role:** Local Expert
    *   **Goal:** To gather and provide insightful and accurate information about St. Petersburg.
    *   **Task:** "Provide insightful and accurate information about St. Petersburg. Focus on its historical significance, cultural landmarks, and unique atmosphere. Your response should be detailed, engaging, and reflect a deep understanding of the city."

2.  **Writer Agent (`writer`):**
    *   **Role:** Senior Writer
    *   **Goal:** To compose compelling and well-structured content based on the information provided by the researcher.
    *   **Task:** "Compose a compelling and well-structured narrative about St. Petersburg based on the insights from the local expert. The content should be engaging, informative, and suitable for a blog post or travel guide. Ensure a coherent flow and captivating language."

**Workflow:**
The Researcher Agent first gathers information about St. Petersburg. This information is then passed to the Writer Agent, who crafts a narrative based on the provided details. The final output is a piece of content about the city.

## `crewai-system-administrator.py`

This script defines an AI agent that acts as a Linux system administrator, specifically focused on providing advice for Kernel-based Virtual Machine (KVM) configurations.

**Purpose:** To showcase how a CrewAI agent can be tasked with providing specialized technical advice.

**Agent and its Role:**

1.  **Linux Sysadmin Agent (`sysadmin_agent`):**
    *   **Role:** Linux System Administrator
    *   **Goal:** To provide expert advice on KVM configuration for specific scenarios.
    *   **Task:** "Provide detailed KVM configuration advice for the following scenario: Running Windows with 1C and MSSQL, including NVMe passthrough for storage. The advice should cover CPU pinning, memory allocation, disk I/O optimization, and network configuration for optimal performance and stability."

**Workflow:**
The Sysadmin Agent takes the specified KVM configuration scenario as input and generates detailed advice. This can include recommendations for XML configuration snippets, kernel parameters, and best practices for the described setup.

## LLM Connection

Both scripts (`crewai-local-expert.py` and `crewai-system-administrator.py`) are configured to connect to an **Ollama LLM instance**. This means that the intelligence and decision-making capabilities of the agents are powered by a language model served through Ollama. Users need to have an Ollama instance running and accessible for these scripts to function correctly.

## Output

The tasks executed by the crews in both scripts can produce textual output. The scripts are generally set up so that this output can be printed to the console and/or saved to files for later inspection. For example, the `crewai-local-expert.py` script might save the generated article about St. Petersburg to a Markdown file.
