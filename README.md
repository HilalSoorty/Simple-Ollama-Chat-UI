# Simple-Ollama-Chat-UI
Simple Ollama Chat UI is a lightweight and user-friendly web interface built with Gradio for interacting with Ollama's chat models. It allows users to have seamless conversations with their locally running Ollama model without needing complex setup or additional dependencies.

Simple Ollama Chat UI

A minimalistic chat interface for interacting with an Ollama model using Gradio. This project provides a clean and simple UI for conversing with an AI model served by Ollama.

❗❗Switch to master branch for the Code.

Features

Chat with an Ollama model through a web-based UI.

Supports conversation history.

Built with Gradio for ease of use.

Requirements

Python 3.8+

Poetry package manager

Ollama installed and running

Installation

Clone the repository

git clone https://github.com/HilalSoorty/Simple-Ollama-Chat-UI.git
cd gradui

Install dependencies using Poetry

poetry install

Run Ollama (if not already running)

ollama serve

Start the Chat UI

poetry run python gradui.py

Configuration

Ensure that your Ollama model is downloaded and ready. You can check available models with:

ollama list

By default, the chat UI uses qwen2.5-coder:0.5b. To change this, update the model parameter in app.py.

Usage

Once the server is running, open the provided Gradio link in your browser and start chatting!
