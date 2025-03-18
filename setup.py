from setuptools import setup, find_packages

setup(
    name="openrouter_exception_handler",
    version="0.4.8",
    description="Handler for exceptions in Python with OpenRouter.ai",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Dannybombastic",
    author_email="dannybombastic@example.com",
    license="MIT",
    packages=find_packages(include=["openrouter_exception_handler*"]),
    python_requires=">=3.6",
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed"
    ],
    keywords=["openrouter", "exception", "handler"],
    project_urls={
        "Homepage": "https://github.com/dannybombastic/openrouter_exception_handler",
        "Repository": "https://github.com/dannybombastic/openrouter_exception_handler"
    }
)
