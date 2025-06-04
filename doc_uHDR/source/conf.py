# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'doc_uHDR'
copyright = '2025, n0upi & Leeexyy4'
author = 'n0upi & Leeexyy4'
release = 'v5'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',    # Documentation automatique du code
    'sphinx.ext.viewcode',   # Liens vers le code source
    'sphinx.ext.githubpages', # Optimisation pour GitHub Pages
    'sphinx.ext.todo',       # Support des TODO
    'sphinx.ext.ifconfig',   # Conditions dans la documentation
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# Configuration pour les extensions
todo_include_todos = True
html_show_sourcelink = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Configuration du thème RTD
html_theme_options = {
    'analytics_id': '',  # ID Google Analytics (optionnel)
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',  # Couleur de l'en-tête
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Logo et favicon (optionnel)
# html_logo = '_static/logo.png'
# html_favicon = '_static/favicon.ico'

# Titre de la documentation dans la barre latérale
html_title = "uHDRv6 Documentation"

# Informations de copyright dans le pied de page
html_show_copyright = True
html_show_sphinx = True

# CSS personnalisé
html_css_files = [
    'custom.css',
]
