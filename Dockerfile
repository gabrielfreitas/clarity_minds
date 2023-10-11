FROM python:3.9

COPY .  /app/
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "clarity_minds.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "--reload"]
