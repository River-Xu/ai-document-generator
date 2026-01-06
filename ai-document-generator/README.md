# AI Document Generator

An AI application that generates **structured documents and reports** from unstructured input using prompt-driven templates.

## Why this project
Many business and technical documents follow fixed structures but are still written manually.
This project explores how large language models can assist in producing **consistent, reusable documents**.

## Features
- Template-based document generation
- Multiple document types (PRD, Test Plan, Meeting Summary)
- CLI + Streamlit Web UI
- Works without API key using local fallback mode

## Quick Start (Windows)
```bash
cd ai-document-generator
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

streamlit run app.py
```

## Templates
- PRD (Product Requirement Document)
- Test Plan
- Meeting Summary

## Project Positioning
AI application project focusing on **document automation and structured output**, not model training.
