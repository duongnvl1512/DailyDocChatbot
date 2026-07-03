# DailyDocChatbot

DailyDocChatbot is a Python-based Retrieval-Augmented Generation (RAG) project that scrapes OptiSigns Zendesk Help Center articles, converts them to Markdown, builds a searchable document index, and powers a chatbot that answers questions using only the scraped documentation.

---

## Features

- Scrapes Zendesk Help Center articles
- Converts article HTML into Markdown
- Saves processed Markdown documents under the docs folder
- Splits documents into smaller chunks for retrieval
- Generates embeddings with the Gemini Embedding API
- Stores vectors in FAISS for semantic search
- Supports similarity search over indexed documentation
- Provides a RAG chatbot that answers questions from retrieved content
- Includes citation support with article URLs
- Uploads processed documents via the Gemini API

---

## Project Structure

```text
DailyDocChatbot/
├── app/
│   ├── clients/          # API clients
│   ├── models/           # Data models
│   ├── processors/       # HTML cleaning, Markdown conversion, chunking
│   ├── services/         # Article, embedding, indexing, chat, and RAG services
│   ├── utils/            # Utility helpers
│   ├── vectorstore/      # FAISS index and metadata handling
│   └── writers/          # Markdown export logic
├── docs/                 # Exported Markdown documents
├── scripts/              # Scraping, indexing, and upload scripts
├── storage/              # FAISS index and metadata files
├── main.py               # Chatbot entry point
├── requirements.txt      # Python dependencies
├── Dockerfile            # Container definition
└── .env.sample           # Sample environment configuration
```

---

## Technologies Used

- Python
- Google Gemini API
- FAISS
- PyYAML
- BeautifulSoup
- Markdownify
- Requests

---

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd DailyDocChatbot
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a .env file:

```bash
copy .env.sample .env
```

---

## Environment Variables

Create a .env file with the following content:

```env
GOOGLE_API_KEY=your_google_api_key
```

---

## Running the Project

1. Scrape documents:

```bash
python -m scripts.scrape
```

2. Build the FAISS index:

```bash
python -m scripts.build_index
```

3. Start the chatbot:

```bash
python main.py
```

---

## Architecture

```text
Zendesk API
→ HTML
→ Markdown
→ Chunking
→ Gemini Embedding
→ FAISS Vector Store
→ Similarity Search
→ Gemini Answer Generation
```

---

## Chunking Strategy

Markdown content is split by paragraphs into chunks. Each chunk has a maximum size of approximately 1000 characters, and metadata is attached to every chunk. The metadata includes:

- article id
- article title
- article slug
- article url
- chunk index

This strategy is well suited for Retrieval-Augmented Generation because it preserves context within each passage while keeping each chunk small enough for efficient retrieval and embedding.

---

## Vector Store

Embeddings are generated with the Gemini Embedding API and stored in a FAISS index for similarity search. Metadata is stored in metadata.pkl, and the vector index is saved as index.faiss in the storage folder.

The indexing script logs:

- number of files
- number of chunks
- embedding dimension
- total vectors

---

## AI Assistant

The chatbot uses Gemini 2.5 Flash to answer user questions. Retrieved chunks are injected into the prompt so the assistant answers using only the indexed documentation. Responses include article URLs as citations to support traceability.

---

## Assignment Requirements

- [x] Scrape Zendesk articles
- [x] Convert HTML to Markdown
- [x] Save Markdown files
- [x] Chunk documents
- [x] Generate embeddings
- [x] Build FAISS vector store
- [x] Load vector store
- [x] Similarity search
- [x] RAG chatbot
- [x] Upload documents via API
- [x] AI Assistant
- [x] Citation support

---

## Screenshots

### Chatbot Demo

![chat](screenshot/chatbot.png)

### AI Assistant

![assistant](screenshot/assistant.png)

---

## Future Improvements

Potential next steps include:

- incremental indexing
- hybrid search (BM25 + FAISS)
- FastAPI REST API
- Streamlit web UI
- conversation memory
- reranking
- Docker deployment
