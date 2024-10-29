# Stress_Testing

## Overview

This Python script performs various system stress tests, including memory, disk, CPU, network, and MySQL database stress tests. It provides a percentage of usage for each resource, helping to evaluate the performance and limits of the system.

## Features

- **Memory Stress Test**: Allocates memory and measures usage.
- **Disk Stress Test**: Writes large files to disk and measures usage.
- **Network Stress Test**: Simulates network traffic and measures usage.
- **CPU Stress Test**: Performs heavy calculations to measure CPU usage.
- **MySQL Stress Test**: Executes a predefined SQL query and displays the results.

## Requirements

- Python 3.x
- `psutil` library
- `mysql-connector` library

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/system-stress-test.git
   cd system-stress-test
   ```

2. **Install Required Libraries**:

   Ensure you have `psutil` and `mysql-connector` installed. You can install them using pip:

   ```bash
   pip install psutil mysql-connector-python
   ```

## Usage

Run the script:

```bash
python stress_test.py
```

