from setuptools import setup, find_packages

setup(
    name="web_search",
    version="0.1.0",
    description="Web search utility with DuckDuckGo and PDF/HTML content extraction",
    author="Nishio",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "pymupdf"
    ],
    python_requires=">=3.7",
)