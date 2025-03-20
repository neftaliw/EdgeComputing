# Use an official Ubuntu base image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /srv/

# Copy the Python script into the container at /srv/
COPY mycode.py .

# Install Dependencies
RUN apt-get -y update && apt-get -y  install python3 && apt-get -y install python3-pip

# Run the Python script when the container launches
CMD ["python3", "mycode.py"]
