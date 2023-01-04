from pathlib import Path

from setuptools import find_packages, setup

setup(
    name="metovlogs",
    version="0.1.6",
    description="Dead simple Python logging.",
    url="https://github.com/metov/metovlogs",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Azat Akhmetov",
    author_email="azatinfo@yandex.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages(),
    install_requires=["coloredlogs"],
)
