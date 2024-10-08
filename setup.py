# setup.py

from setuptools import setup

def read_requirements():
    with open("requirements.txt") as fp:
        content = fp.readlines()
    return [line.strip() for line in content if not line.startswith("#")]

setup(
    name="talk2pdfs",
    version="0.0.1",
    author="Eshan Sud",
    author_email="eshansud22@gmail.com",
    description="A chatbot interface to ask questions from custom PDFs and URLs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/eshan-sud/talk2pdfs",
    python_requires=">=3.12",
    install_requires=read_requirements(),
    include_package_data=True,
)