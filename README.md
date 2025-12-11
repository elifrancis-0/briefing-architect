# Briefing Architect 🏛️

**Briefing Architect** is a Python-based automation tool that converts raw text transcripts into structured executive briefings. It functions as a lightweight **ETL (Extract, Transform, Load) pipeline**, reading local data, processing it through high-performance Large Language Models (LLM), and exporting polished Markdown reports.

### Key Features
* **AI-Powered Summarization:** Leverages the **Groq API** (supporting Llama 3 and Qwen 2.5) for ultra-fast inference.
* **Chain-of-Thought Parsing:** Implements custom logic to programmatically remove internal "thinking" traces (`<think>` tags) from reasoning model outputs.
* **Secure Configuration:** Uses environment variables (`.env`) to separate sensitive credentials from the codebase.
* **Automated File I/O:** Orchestrates reading from raw text files and writing to formatted Markdown.

**Tech Stack:** Python 3, Groq SDK, python-dotenv.