# Nyaya Saathi - Civic Docs on Apertus 🇨🇭🇵🇰

Sovereign offline AI that explains legal & civic docs in your own dialect - Swiss-German, French, Urdu & more - using open Apertus, no foreign cloud.

Built for **Hack Apertus** - Switzerland's sovereign LLM.

### Why?
In Bern, a tenant can't understand German rental contract. In Chakwal, a farmer can't read English land record. Both must upload sensitive CNIC/docs to US closed AIs, losing sovereignty.

### What it does
- Upload PDF: Swiss tenancy, tax notice, Pakistan domicile, SME compliance
- Choose dialect: Swiss-German, French, Italian, English, Urdu, Punjabi
- Get simple explanation + risks + next steps
- 100% offline via Ollama - no data leaves device

### Run Locally on low device
```bash
ollama pull apertus-8b-instruct
pip install gradio pymupdf ollama
python app.py
