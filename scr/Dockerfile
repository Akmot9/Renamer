FROM python:3.8-slim-buster

WORKDIR /app


# Install the required dependencies
RUN apt-get update && apt-get install -y python3-tk
RUN apt-get update && apt-get install -y tk-dev


# Copy the rest of the application files
COPY . .

# Set the default command to run when the container starts
CMD ["python", "Renamer.py"]
