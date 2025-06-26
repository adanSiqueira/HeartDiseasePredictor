FROM python:3.10-slim

# Setting environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Setting working directory
WORKDIR /app

# Installing system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy app files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Exposing port used by Dash
EXPOSE 8050

# Run the app
CMD ["python", "main.py"]
