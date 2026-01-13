# FROM python:3.11-slim

# WORKDIR /app

# COPY . .

# COPY requirements.txt .
# RUN pip install -r requirements.txt

# # CMD["uvicorn","main:app","--reload"]
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]