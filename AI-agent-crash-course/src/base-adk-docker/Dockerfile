# Use an official Python base image
FROM python:3.13-slim

# Install system dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .

# If ADK is not on PyPI, clone from GitHub or install from local path
# RUN pip install git+https://github.com/google/agent-development-kit.git
RUN pip install --no-cache-dir -r requirements.txt