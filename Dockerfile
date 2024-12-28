FROM python:3.10-slim

WORKDIR /app

COPY main.py db_maker.py /app/

VOLUME /data

ENV DATABASE_PATH=/data/expenses.db

RUN python db_maker.py

CMD ["python", "main.py"]
