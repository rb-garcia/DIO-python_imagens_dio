from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-package",
    version="0.0.1",
    author="Ricardo B Garcia",
    author_email="ricardobgarcia@outlook.com",
    description="Projeto exemplo em Python: criação de pacotes de processamento de imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rb-garcia/python_imagens_dio",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)