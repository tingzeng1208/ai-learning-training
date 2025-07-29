# Use an official Python base image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the agent code
COPY greeting_agent/ ./greeting_agent/

# Expose the ADK web server port
EXPOSE 8081

# Run the agent using ADK's web server
CMD ["adk", "web", "--port", "8081", "--agent", "greeting_agent"]