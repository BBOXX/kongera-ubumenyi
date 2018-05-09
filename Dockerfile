FROM python:3.6
ADD . /code
WORKDIR /code
RUN pip install pipenv
RUN pipenv install --system --ignore-pipfile
ENTRYPOINT ["python"]
CMD ["run.py"]