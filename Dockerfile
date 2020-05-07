FROM python:3-alpine
FROM tensorflow/tensorflow:1.15.0-py3

# RUN apt-get update -y
# RUN apt-get install -y python-pip

COPY . /app

# Create and change to the app directory.
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod 444 app.py
RUN chmod 444 requirements.txt

# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 8080

# Run the web service on container startup.
CMD [ "python", "app.py" ]
