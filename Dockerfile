# 1. Use a lightweight Python 3.13 image
FROM python:3.13-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Install system dependencies (Required for FAISS and C++ builds)
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy the requirements file first (for better caching)
COPY requirements.txt .

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of your application code
COPY . .

# 7. Expose the port FastAPI runs on
EXPOSE 8000

# 8. Command to run the API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]