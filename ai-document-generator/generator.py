from __future__ import annotations
from pathlib import Path
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv(override=False)

def load_template(name: str) -> str:
    p = Path("templates") / f"{name}.md"
    return p.read_text(encoding="utf-8")

def local_generate(template: str, raw: str) -> str:
    # Simple fallback: inject raw text into placeholders
    return template.replace("{{background}}", raw) \
                   .replace("{{goals}}", raw) \
                   .replace("{{features}}", raw) \
                   .replace("{{nfr}}", raw) \
                   .replace("{{risks}}", "TBD") \
                   .replace("{{scope}}", raw) \
                   .replace("{{strategy}}", raw) \
                   .replace("{{cases}}", raw) \
                   .replace("{{attendees}}", raw) \
                   .replace("{{points}}", raw) \
                   .replace("{{actions}}", "TBD")

def llm_generate(template: str, raw: str) -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        return local_generate(template, raw)

    client = OpenAI(api_key=key, base_url=os.getenv("OPENAI_BASE_URL"))
    prompt = f"""You are an assistant that fills structured templates.
Template:
{template}

Input:
{raw}

Fill the template sections clearly."""

    resp = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return resp.choices[0].message.content.strip()

def generate(doc_type: str, raw: str) -> str:
    template = load_template(doc_type)
    return llm_generate(template, raw)
