FROM python:3.7

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 80

COPY ./ ./

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
