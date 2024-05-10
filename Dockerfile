# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the contents of the 'src' directory into the container at /app
COPY src /app/

# Make port 80 available to the world outside this container
EXPOSE 3100

# Set environment variables
ENV NAME verbifyai-backend-fast-api-docker

# Run uvicorn with the correct path to your FastAPI application in the 'src' directory
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3100"]
