# Use an official Python runtime as a parent image
FROM python:3.11

ENV PYTHONUNBUFFERED=1

# Set the working directory to /app
WORKDIR /app

# Install system dependencies required for mysqlclient
RUN apt-get update && apt-get install -y python3-dev default-libmysqlclient-dev gcc

# Copy the application files into the image
COPY . /app/

# Install application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 on the container
EXPOSE 8000

# Command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
