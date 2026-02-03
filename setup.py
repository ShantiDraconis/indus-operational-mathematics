"""
Setup configuration for Harappa Operational Mathematics System
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="harappa",
    version="0.1.0",
    author="Harappa Project Contributors",
    author_email="",
    description="A formal system based on Indus Valley civilization principles for modern computational applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShantiDraconis/indus-operational-mathematics",
    packages=find_packages(exclude=["tests", "examples", "docs"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
from setuptools import setup, find_packages

setup(
    name="indus-operational-mathematics",
    version="0.1.0",
    description="A framework for analyzing ancient symbolic systems through universal cognitive operators",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="ShantiDraconis",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "matplotlib>=3.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
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
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Distributed Computing",
    ],
    keywords="formal-methods, symbolic-computation, smart-contracts, theorem-proving, unique-identifiers, archaeology, dao, semantic-database",
    python_requires=">=3.8",
    install_requires=[
        # No external dependencies for core functionality
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
            "sphinx>=6.0",
            "sphinx-rtd-theme>=1.2",
        ],
        "visualization": [
            "matplotlib>=3.5",
            "networkx>=3.0",
            "graphviz>=0.20",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/ShantiDraconis/indus-operational-mathematics/issues",
        "Source": "https://github.com/ShantiDraconis/indus-operational-mathematics",
        "Documentation": "https://github.com/ShantiDraconis/indus-operational-mathematics/tree/main/docs",
    },
    ],
)
