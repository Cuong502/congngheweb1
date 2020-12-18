#Use an official Python runtime as parent image
FROM python:3.6-slim

# Set the working directory to /app
ADD . /app

# Install any needed packagees specified in requireements.txt
RUN pip install --trusted-host pyoi.python.ord -r requireements.txt

#Make port 8080 available to the word outsize this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "app.py"]