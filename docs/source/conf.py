# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from __future__ import annotations

import os
import sys
from datetime import datetime

# -- Path setup --------------------------------------------------------------

# Add the "src" directory to sys.path so Sphinx can find the package.
sys.path.insert(0, os.path.abspath("../src"))

# -- Project information -----------------------------------------------------

project = "deribit-history-client"
author = "Jannis Philipp Beerhold"
copyright = f"{datetime.now().year}, {author}"
release = "0.1.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",           # Auto-generate API docs from docstrings
    "sphinx.ext.napoleon",          # Support for Google/NumPy style docstrings
    "sphinx_autodoc_typehints",     # Show type hints nicely in the docs
    "sphinx_rtd_dark_mode",         # Dark mode support for Read the Docs theme
]

templates_path = ["_templates"]
exclude_patterns: list[str] = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]

# -- Autodoc options ---------------------------------------------------------

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

autodoc_typehints = "description"
