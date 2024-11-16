FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

RUN apt update && apt install -y \
 libgl1  \
 tesseract-ocr tesseract-ocr-jpn \
 && apt clean

COPY requirements.txt .
RUN cat requirements.txt
RUN pip install -r requirements.txt

RUN chsh -s /bin/bash vscode
