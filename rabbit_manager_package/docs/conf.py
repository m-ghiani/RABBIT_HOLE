import os
import sys

# Aggiungi il percorso della directory principale del progetto al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importa la classe SharedMemoryManager dal modulo shared_memory
from rabbithole.asyncio_rabbit_manager import AsyncioRabbitManager  # noqa: F401, E402
from rabbithole.rabbit_log_messages import RabbitLogMessages  # noqa: F401, E402
from rabbithole.config.config_file_manager import ConfigFileManager  # noqa: F401, E402
from rabbithole.config.asyncio_rabbit_config import RabbitConfig  # noqa: F401, E402


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Rabbit Hole"
copyright = "2023-2024, Massimo Ghiani"
author = "Massimo Ghiani"
release = "1.5"
master_doc = "index"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx.ext.viewcode"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "bizstyle"
html_static_path = ["_static"]
