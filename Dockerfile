# pull oficial base image
FROM python:3.9.1-slim-buster

# set workinng directory

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


ADD . /code
WORKDIR /code

COPY poetry.lock pyproject.toml /tmp/


RUN pip install poetry
RUN cd /tmp && poetry export -f requirements.txt --output /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt


# copy entrypoint.sh
#COPY entrypoint.sh /usr/src/app/entrypoint.sh
#RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
#ENTRYPOINT ["entrypoint.sh"]