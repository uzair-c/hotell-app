FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get install -y default-libmysqlclient-dev && \
    pip3 install --trusted-host pypi.python.org -r ./requirements.txt

# Set the command to run the application
CMD [ "python", "./app.py" ]
