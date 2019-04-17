FROM python:3.7.2

RUN mkdir app

WORKDIR /app

COPY ./app .

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 5000

RUN chmod 644 app.py
CMD ["python", "app.py"]