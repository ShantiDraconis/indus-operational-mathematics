"""
Setup configuration for Indus Operational Mathematics.

Dois pacotes vão para a instalação:
- os de src/ (analysis, models, symbolic_systems, visualization), que os testes em
  tests/ importam com src/ no sys.path;
- harappa/ (o sistema operacional Harappa: Symbol, Operator, State, Record, ...).

python/ é outra distribuição (indus-analysis), com seu próprio setup.py.
"""

from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

packages = find_packages(where="src") + find_packages(include=["harappa", "harappa.*"])

setup(
    name="indus-operational-mathematics",
    version="0.1.0",
    description="A framework for analyzing ancient symbolic systems through universal cognitive operators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ShantiDraconis",
    url="https://github.com/ShantiDraconis/indus-operational-mathematics",
    packages=packages,
    package_dir={"": "src", "harappa": "harappa"},
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "matplotlib>=3.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
        ],
        "visualization": [
            "networkx>=3.0",
            "graphviz>=0.20",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    project_urls={
        "Bug Reports": "https://github.com/ShantiDraconis/indus-operational-mathematics/issues",
        "Source": "https://github.com/ShantiDraconis/indus-operational-mathematics",
    },
)
