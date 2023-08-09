# Use the official Python image from the Docker Hub
# Use the official Python image from the Docker Hub
FROM python:3.8-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Copy your local `app.py` file to the container
COPY ./app.py /app.py

# Command to run the application using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
