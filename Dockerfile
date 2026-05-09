FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    ffmpeg \
    build-essential \
    libssl-dev \
    # Added for SciPy compilation
    gfortran \
    pkg-config \
    libopenblas-dev \
    liblapack-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Upgrade pip and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Start the bot
CMD ["python3", "-m", "VIVAANXMUSIC"]
