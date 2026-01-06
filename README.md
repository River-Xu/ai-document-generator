# AI Document Generator

An AI application for **automatically generating structured business and technical documents**
from unstructured text using **template-driven prompting**.

This project focuses on applying LLMs to **document automation scenarios** commonly found in product, QA, and project management workflows.

---

## Why this project

In real-world work environments, documents such as:
- Product Requirement Documents (PRD)
- Test Plans
- Meeting Summaries

often follow fixed structures, but are still written manually.
This leads to:
- Low efficiency
- Inconsistent quality
- High dependency on individual experience

This project explores how LLMs can be used to **standardize and accelerate document creation**.

---

## What it does

- Converts raw text (notes, requirements, discussions) into structured documents
- Supports multiple document types:
  - Product Requirement Document (PRD)
  - Test Plan
  - Meeting Summary
- Uses editable Markdown templates
- Provides:
  - **Web UI (Streamlit)**
  - **CLI tool**
- Works **without API key** using a local fallback mode

---

## Architecture Overview

