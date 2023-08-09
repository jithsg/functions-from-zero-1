# Use the official Python image from the Docker Hub
# Use the official Python image from the Docker Hub
# Use the official Python image from the Docker Hub
FROM python:3.8-slim-buster

# Set the working directory inside the container. Creates /app if it doesn't exist.
WORKDIR /app

# Copy the requirements.txt file into the container
COPY . /app

# Install the packages listed in requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy your local `app.py` file to the container's working directory


# Command to run the application using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
