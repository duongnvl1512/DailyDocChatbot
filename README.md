# DailyDocChatbot

DailyDocChatbot is a lightweight RAG-based support assistant for OptiSigns documentation. It scrapes help-center articles, converts them into markdown, builds a searchable FAISS index, and answers user questions using Gemini-powered retrieval and generation.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/duongnvl1512/DailyDocChatbot.git
   cd DailyDocChatbot
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a local environment file:
   ```bash
   copy .env.sample .env
   ```
   Then set your Google API key in `.env`:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

## Run locally

Run the scraper to refresh markdown files from the support site:

```bash
python -m scripts.scrape
```

Build the FAISS index from the generated docs:

```bash
python -m scripts.build_index
```

Start the local assistant:

```bash
python testmain.py
```

You can also pass a question directly:

```bash
python testmain.py --question "How do I add a YouTube video?"
```

## Daily job

The repository includes a GitHub Actions workflow at:
https://github.com/duongnvl1512/DailyDocChatbot/actions

The job runs once per day and:

- detects newly added articles,
- detects updated articles,
- detects skipped articles,
- rebuilds the index only when content changes are detected.

## Chunking strategy

The indexing pipeline follows this flow:

Markdown → header-aware chunks → about 500–800 characters per chunk → 20 chunks per embedding request → FAISS IndexFlatIP

## Sample assistant response

![Sample assistant response](screenshot/Screenshot%20AI's%20answer.png)

Example:

Question: How do I add a YouTube video?

Answer: The assistant responds with a concise answer based on the indexed documentation.

## Repository

https://github.com/duongnvl1512/DailyDocChatbot
