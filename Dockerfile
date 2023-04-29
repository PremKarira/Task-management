# FROM python:3.9-slim-buster

# WORKDIR /app

# COPY . /app

# RUN pip install --trusted-host pypi.python.org -r requirements.txt


# EXPOSE 8000

# ENV MONGO_URL <URL>

# CMD ["python", "main.py"]

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY . /app

# ENV MONGO_URL <URL>

EXPOSE 8000

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# CMD ["uvicorn", "main:app", "--port", "8000"]
