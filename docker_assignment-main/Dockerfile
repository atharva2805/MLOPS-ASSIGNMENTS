# Stage 1: Builder - Install dependencies in a separate stage
FROM python:3.11-slim AS builder

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file to take advantage of Docker's layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the application files
COPY . .

# Expose the port FastAPI will use
EXPOSE 8001

# Command to start the FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
