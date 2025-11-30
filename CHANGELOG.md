# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2025-11-30
### Added
- Initial implementation of `DeribitHistoryClient`
- Low-level HTTP interface (`read.py`)
- JSON schema validation for:
  - `get_instrument`
  - `get_instruments`
  - `get_trades_by_sequence`
- Bundled JSON schemas stored in the package
- Maintenance script `generate_schemas.py` to rebuild API schemas
- Unit tests (mock-based)
- Optional integration tests (`@pytest.mark.external`)
- Full Sphinx documentation setup
- GitHub Actions workflows (lint, CI, docs)

---

## [Unreleased]
