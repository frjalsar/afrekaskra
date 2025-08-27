# syntax=docker/dockerfile:1
FROM python:3.12

# Set environment variables to prevent Python from writing .pyc files and to ensure output is sent straight to the terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies for ODBC and MS SQL Server
RUN apt-get update && apt-get install --no-install-recommends --assume-yes tdsodbc unixodbc
#RUN apt-get install -y tdsodbc
#RUN apt-get install -y unixodbc
#RUN apt-get install -y unixodbc-dev

# Set up the working directory
WORKDIR /code
# Copy the requirements file
COPY requirements.txt /code/
# Install Python dependencies
RUN pip install -r requirements.txt
# Copy the rest of the application code
COPY . /code/

# Expose the port that the application will run on
EXPOSE 8000
# Set the entrypoint for the container
# Use Gunicorn to serve the Django application
ENTRYPOINT ["gunicorn", "-c", "/code/config/gunicorn.conf.py", "Sif.wsgi"]
