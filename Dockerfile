FROM python:3.6
ADD . /code
WORKDIR /code

RUN pip install pipenv
RUN pipenv install --system --ignore-pipfile


CMD flask run --host 0.0.0.0
