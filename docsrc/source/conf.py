# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import io
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
sys.setrecursionlimit(1500)

# -- Project information -----------------------------------------------------

project = 'CMS-GEN'
copyright = '2021, cms-generator'
author = 'cms-generator'

# The full version, including alpha/beta/rc tags
release = '1'

# The short X.Y version.
#version = "{major}.{minor}".format(**_version_info)
# The full version, including alpha/beta/rc tags.
#release = "{major}.{minor}.{patch}{tag}".format(**_version_info)


_docs_path = os.path.dirname(__file__)
_version_path = os.path.abspath(
    os.path.join(_docs_path, "..", "source", "__init__.py")
)
#with open(_version_path, encoding="utf-8") as fp:
#    try:
#        _version_info = re.search(
#            r'^__version__ = "'
#            r"(?P<major>\d+)"
#            r"\.(?P<minor>\d+)"
#            r"\.(?P<patch>\d+)"
#            r'(?P<tag>.*)?"$',
#            fp.read(),
#            re.M,
#        ).groupdict()
#    except IndexError:
#        raise RuntimeError("Unable to determine version.")

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc' , 
    'sphinx.ext.mathjax',  
    'recommonmark',
    'rinoh.frontend.sphinx',
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

#html_theme = "aiohttp_theme"
#html_theme_path = ["_theme"]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "logo": "cmslogo.png",
    "description": "CMS Generator Group",
    #"canonical_url": "http://docs.aiohttp.org/en/stable/",
    "github_user": "SiewYan",
    "github_repo": "cmsgen.github.io",
    "github_button": True,
    "github_type": "star",
    "github_banner": True,
    "badges": [
        {
            "image": "https://github.com/SiewYan/cmsgen.github.io/workflows/CI_push/badge.svg",
            "target": "https://github.com/SiewYan/cmsgen.github.io/actions?query=CI+and+CD+Sphinx",
            "height": "20",
            "alt": "Github Pipelines CI/CD status",
        },
        {
            "image": "https://codecov.io/gh/SiewYan/cmsgen.github.io/branch/main/graph/badge.svg?token=P1D24USZ7B",
            "target": "https://codecov.io/gh/SiewYan/cmsgen.github.io",
            "height": "20",
            "alt": "Code coverage status",
        },
        #{
        #    "image": "https://img.shields.io/discourse/status?server=https%3A%2F%2Faio-libs.discourse.group",
        #    "target": "https://aio-libs.discourse.group",
        #    "height": "20",
        #    "alt": "Discourse status",
        #},
        #{
        #    "image": "https://badges.gitter.im/Join%20Chat.svg",
        #    "target": "https://gitter.im/aio-libs/Lobby",
        #    "height": "20",
        #    "alt": "Chat on Gitter",
        #},
    ],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

latex_elements = {
    'papersize' : 'letterpaper' ,
    'pointsize' : '10pt' ,
    'preamble'  : '',
    'figure_align' : 'htbp'
}

html_sidebars = {
    '**': [
        'about.html',
        'badges.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
    ]
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',    
}
