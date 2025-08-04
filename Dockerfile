# 1. Use official Python base image
FROM python:3.10-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy all files from your machine to Docker container
COPY . .

# 4. Install system dependencies (required for newspaper, matplotlib etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# 5. Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 6. Download spaCy model
RUN python -m spacy download en_core_web_sm

# 7. Expose the port Streamlit will run on
EXPOSE 8501

# 8. Command to run your app
CMD ["streamlit", "run", "app/ui/streamlit_app.py", "--server.port=8501", "--server.enableCORS=false"]
