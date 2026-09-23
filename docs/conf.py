numfig = True

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FISE'
copyright = '2026, docandaniela'
author = 'docandaniela'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",              # lets Sphinx read .md files
    "sphinxcontrib.mermaid",    # renders ```mermaid blocks
     "sphinx_design",
     "sphinx_copybutton",
              "sphinx_togglebutton",
              "sphinxcontrib.bibtex",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
# BIBTEX
bibtex_bibfiles = ['./_sharedFiles/eu_legislation.bib',
                   './_sharedFiles/bibliography.bib',]
bibtex_reference_style = 'author_year'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '*.txt']

# NUMBERING
# The separator must defined in a custom.css :-(
numfig = True
numfig_format = {
    'figure': 'Figure %s',       # Changes "Fig. 1" to "Figure 1"
    'table': 'Table %s',
    'code-block': 'Example %s',  # Changes "Listing 1" to "Example 1"
    'section': 'Section %s',
}

# MATH - Tell MyST to allow dollar signs and advanced math blocks
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "colon_fence",
    "linkify",
    "attrs_inline"
]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "logo": {
        "alt_text": "FISE Documentation (learning)",
        "text": "Forest Information System for Europe (FISE)",
    },
    "secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink"],
    "show_toc_level": 4,
    "use_edit_page_button": True,
    "navbar_align": "right"
}

html_context = {
    "github_user": "docandaniela",
    "github_repo": "my-doc",
    "github_version": "main",
    "doc_path": "docs",
}
html_logo = "_static/image.png"

html_sidebars = {
    "**": ["sidebar-collapse", "sidebar-nav-bs"],
}

html_static_path = ['_static']
html_css_files = [
    'customTable.css',
    'customTheme.css'
    ]

html_show_copyright = False

html_js_files = [
    "js/mermaid-zoom.js",
]

# MERMAID DIAGRAMS 
mermaid_init_js = """
mermaid.initialize({theme:"neutral"});
"""

# -- Draft marker ------------------------------------------------------------
# Every page of the revised Directive section is marked as a draft.

DRAFT_SECTION = "FISE-learning"
DRAFT_BANNER = (
    '<aside class="draft-banner" role="note">'
    'Draft \u2013 under review &amp; revision</aside>'
)


def add_draft_banner(app, pagename, templatename, context, doctree):
    if pagename == DRAFT_SECTION or pagename.startswith(DRAFT_SECTION + "/"):
        context["body"] = DRAFT_BANNER + context.get("body", "")


def setup(app):
    app.connect("html-page-context", add_draft_banner)