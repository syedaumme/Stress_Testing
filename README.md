# Stress_Testing

## Overview

This Python-based system stress testing tool performs comprehensive tests across multiple system resources, including memory, disk, CPU, network, and MySQL database performance. Additionally, it features automated logging and alerting functionalities to monitor and notify users of resource consumption.

## Features

- **Memory Stress Test**: Allocates a significant amount of memory to evaluate consumption levels and system response.
- **Disk Stress Test**: Writes large files to disk and tracks disk space usage to understand limits and response under storage stress.
- **Network Stress Test**: Simulates heavy network traffic to measure bandwidth usage and performance.
- **CPU Stress Test**: Executes intensive calculations to assess CPU utilization under load.
- **MySQL Stress Test**: Runs predefined SQL queries on a MySQL database to monitor performance under query load.
- **Automated Logging with AI Suggestions**: `ai_suggestionsfile.py` uses the ChatGPT API to analyze stress logs and save performance improvement suggestions to `suggestions.txt`.
- **WhatsApp Alerts**: `send_to_whatsapp.py` utilizes Twilio to send stress test suggestions and alerts directly to WhatsApp.

## Requirements

- Python 3.x
- `psutil` library
- `mysql-connector` library
- Docker (for containerized deployments)
- `requests` (for API calls to ChatGPT)
- `twilio` library (for WhatsApp messaging)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/syedaumme/Stress_Testing.git
   cd Stress_Testing
   ```

2. **Install Required Libraries**:

   Ensure all dependencies are installed:

   ```bash
   pip install psutil mysql-connector-python requests twilio
   ```

3. **Docker Setup**:

   A Dockerfile is included for easy deployment in a containerized environment.

   To build the Docker image:

   ```bash
   docker build -t stress_testing .
   ```

   Run the container:

   ```bash
   docker run -d --name stress_tester stress_testing
   ```

## Running the Script

Once all dependencies are installed, you can start the stress tests by running:

```bash
python app.py
```

## CI/CD Integration

The project includes a `Jenkinsfile` that triggers automatically using ngrok and webhooks, enabling continuous integration and deployment for this stress-testing tool.

---
