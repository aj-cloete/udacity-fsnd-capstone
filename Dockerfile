FROM python:3.8-slim AS base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base AS python-deps

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

# Install pipenv and compilation dependencies
RUN pip install --upgrade pip && pip install pipenv

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv sync

FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends wget

# Download and install dockerize.
# Needed so that containers wait on their dependencies before they start.
ENV DOCKERIZE_VERSION v0.6.1
RUN wget --no-verbose https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Create and switch to a new user
RUN useradd --create-home udacity
USER udacity

# Copy the application to the `app` directory
WORKDIR /home/udacity
COPY . .

# Be a web server
EXPOSE 5000
ENV GUNICORN_CMD_ARGS "--reload --log-level=debug --bind 0.0.0.0:5000"
CMD ["gunicorn", "wsgi:app"]
