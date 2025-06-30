from setuptools import setup, find_packages

setup(
    name="web_search",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "PyMuPDF"
    ],
    author="Nishio",
    #author_email="your.email@example.com",
    description="A tool to perform DuckDuckGo search and extract contents.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/west0714/web_search",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.7',
)
