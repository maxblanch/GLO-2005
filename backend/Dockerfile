FROM python:3.7.2

RUN mkdir app

WORKDIR /app

COPY ./src/requirements.txt .

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]