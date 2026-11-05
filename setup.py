#!/usr/bin/env python3
"""Setup script for AetherGit."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [
        line.strip()
        for line in fh
        if line.strip() and not line.startswith("#")
    ]

setup(
    name="aethergit",
    version="1.0.0",
    author="Samir Baladi",
    author_email="gitdeeper@gmail.com",
    description="AetherGit: Scalable Source Control for Autonomous AI Agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests", "tests.*", "docs", "docs.*", "PUBLICATION", "PUBLICATION.*", "ANALYSIS", "ANALYSIS.*", "REPORTS", "REPORTS.*"]),
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.11",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Version Control",
        "Topic :: Scientific/Engineering",
        "Topic :: Documentation",
    ],
    keywords="version control, distributed systems, agentic software engineering, changesets, derived data, repository architecture, scalability, aethergit",
    project_urls={
        "Homepage": "https://aethergit.netlify.app",
        "GitHub": "https://github.com/gitdeeper15/AetherGit",
        "GitLab": "https://gitlab.com/gitdeeper15/AetherGit",
        "Codeberg": "https://codeberg.org/gitdeeper15/AetherGit",
        "Bitbucket": "https://bitbucket.org/gitdeeper15/AetherGit",
        "Zenodo": "https://doi.org/10.5281/zenodo.23966896",
        "Figshare": "https://doi.org/10.6084/m9.figshare.34922532",
        "OSF": "https://osf.io/zk532",
    },
)
