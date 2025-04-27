# Use an official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your app code into the container
COPY api/ /app/api/
COPY data/ /app/data/
COPY docker_requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r docker_requirements.txt

# Expose the port uvicorn will run on
EXPOSE 8000

# Start uvicorn server when container launches
CMD ["uvicorn", "api.api:app", "--host", "0.0.0.0", "--port", "8000"]