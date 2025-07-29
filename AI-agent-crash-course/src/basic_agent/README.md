# ADK Greeting Agent Docker Setup

This directory contains the Docker configuration for running the ADK greeting agent as a web service.

## Prerequisites

- Docker and Docker Compose installed
- Google AI API credentials (if using Google AI models)

## Quick Start

1. **Build and run the container:**
   ```bash
   docker-compose up -d
   ```

2. **Check if the service is running:**
   ```bash
   docker-compose ps
   ```

3. **View logs:**
   ```bash
   docker-compose logs -f adk-web-agent
   ```

4. **Test the agent:**
   ```bash
   python requests-docker-agent.py
   ```

## Configuration

### Environment Variables

Create a `.env` file in this directory with the following variables (if needed):

```env
# ADK Agent Environment Variables
PORT=8081
HOST=0.0.0.0

# Google AI API Configuration (if needed)
# GOOGLE_API_KEY=your_api_key_here
# GOOGLE_PROJECT_ID=your_project_id_here

# Database Configuration (if using ADK with database)
# DATABASE_URL=your_database_url_here

# Logging Configuration
LOG_LEVEL=INFO
```

### Port Configuration

The agent runs on port 8081 by default. You can change this by modifying:
- `docker-compose.yml` - Update the port mapping
- `Dockerfile` - Update the EXPOSE directive and CMD
- `.env` file - Update the PORT variable

## API Endpoints

Once running, the agent will be available at:
- **Health Check:** `http://localhost:8081/health`
- **Agent Message:** `http://localhost:8081/agent/greeting_agent/message`

## Troubleshooting

1. **Container won't start:**
   - Check logs: `docker-compose logs adk-web-agent`
   - Ensure all dependencies are in `requirements.txt`

2. **Port already in use:**
   - Change the port in `docker-compose.yml`
   - Or stop other services using port 8081

3. **Agent not responding:**
   - Check if the agent is healthy: `docker-compose ps`
   - Verify the agent code in `greeting_agent/agent.py`

## Stopping the Service

```bash
docker-compose down
```

To remove all containers and images:
```bash
docker-compose down --rmi all --volumes --remove-orphans
``` 