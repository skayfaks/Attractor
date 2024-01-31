# Python base. Recommended by https://pythonspeed.com/articles/base-image-python-docker-images/
FROM python:3.7-slim-buster

# Copy all working files into container
COPY ./app/ /app
# Change working directory
WORKDIR /app

# Install dependencies
RUN pip install -r /app/requirements.txt

ARG PRODUCTION_BUILD
ARG WORKERS=4
ARG HOST='0.0.0.0'
ARG PORT=5000
# If not production build -> make interactive
ARG INTERACTIVITY=${PRODUCTION_BUILD:-'--reload --log-level debug'}
ENV GUNICORN_CMD_ARGS="-w $WORKERS -b $HOST:$PORT $INTERACTIVITY"

# Run
EXPOSE 5000
ENTRYPOINT ["gunicorn", "wsgi:server"]
