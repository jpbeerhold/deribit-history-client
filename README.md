# deribit-history-client

[![Docs](https://img.shields.io/badge/docs-online-blue)](https://jpbeerhold.github.io/deribit-history-client/)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![CI](https://github.com/jpbeerhold/deribit-history-client/actions/workflows/ci.yaml/badge.svg)
![Docs Build](https://github.com/jpbeerhold/deribit-history-client/actions/workflows/docs.yaml/badge.svg)
![Docker](https://img.shields.io/badge/GHCR-image-blue?logo=docker)
![Lint](https://github.com/jpbeerhold/deribit-history-client/actions/workflows/lint.yaml/badge.svg)

A lightweight and structured Python client for the **Deribit Historical Public API**, providing clean access to instruments and trade data — with an optional **schema-based API change detection system**.

This project is intentionally simple, dependency-light, and easy to integrate into trading analytics pipelines, automation scripts, or monitoring systems.

---

## 🗄️ Key Features

- High-level `DeribitHistoryClient` for Deribit historical data
- Low-level HTTP request layer (`read.py`)
- JSON Schema validation for API shape consistency
- Pre-generated schemas included with the package
- Script to **regenerate schemas automatically**
- Fully mocked **unit tests**
- Optional **integration test** using real Deribit live API (`@pytest.mark.external`)
- Sphinx documentation for the entire library  
- GitHub Actions for linting, testing, and documentation deployment

---

## 📦 Project Structure

```text
src/deribit_history_client/
    client.py
    read.py
    schemas/
        get_instrument.json
        get_instruments.json
        get_trades_by_sequence.json

scripts/
    generate_schemas.py

tests/
    unit/
    integration/

docs/
    conf.py
    index.rst
    api.rst

.github/workflows/
    ci.yaml
    lint.yaml
    docs.yaml

pyproject.toml
README.md
```

---

## 📥 Installation

### From source

```bash
pip install -e .
```

### From GitHub

```bash
pip install git+https://github.com/jpbeerhold/deribit-history-client.git
```

---

## ⚡ Quickstart Example

```python
from deribit_history_client.client import DeribitHistoryClient

client = DeribitHistoryClient()

instrument = client.get_instrument("BTC-PERPETUAL")
print(instrument)

trades = client.get_trades_by_sequence("BTC-PERPETUAL", 1, 5000)
print(trades)
```

---

## 🧪 Running Tests

Unit tests:

```bash
pytest
```

Integration tests using the live Deribit API:

```bash
pytest -m external
```

---

## 🧩 API Shape Validation (Schema Checking)

This project includes JSON schema files under:

```text
src/deribit_history_client/schemas/
```

To verify that Deribit’s API has not changed its response structure:

```python
client.perform_api_check()
```

If the structure deviates from expectations, the validator prints warnings and details.

---

## 🛠 Regenerating JSON Schemas

A development-only script is included:

```bash
python scripts/generate_schemas.py
```

This script:

- Calls the live Deribit API  
- Builds JSON Schemas using **Genson**
- Writes new schemas with metadata (`$schema_generated_from`, `$generated_at`)

Use this **only when the API format changes** and the schemas need to be updated.

---

## 📚 Documentation

[Online documentation](https://jpbeerhold.github.io/deribit-history-client/)

Build locally:

```bash
cd docs
make html
```

Open:

```bash
docs/_build/html/index.html
```

---

## 🧑‍💻 Development

Install dev dependencies:

```bash
pip install -e .[dev]
```

Run Ruff:

```bash
ruff check .
```

Build documentation:

```bash
cd docs
make html
```

---

## 📄 License

MIT License  
© 2025 Jannis Philipp Beerhold