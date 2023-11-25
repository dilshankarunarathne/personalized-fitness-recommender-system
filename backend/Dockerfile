# Back-end Dockerfile
# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory in the container to /app
WORKDIR /app

# Copy requirements.txt into the directory
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Bundle app source inside Docker image (by copying from your local directory)
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the app when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]