# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

RUN apt-get update
RUN apt-get install -y python-pip
RUN apt-get install -y default-libmysqlclient-dev

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
ADD . /app
COPY . /app

#COPY ./.env /app/.env
COPY env.example /app/.env

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
RUN mkdir -p /app/static
# RUN python manage.py collectstatic --noinput

#run migrations
RUN python manage.py makemigrations && python manage.py migrate --noinput
# RUN python manage.py initadmin 1 --admin
# RUN python manage.py load_data


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "finance_microapi.wsgi"]