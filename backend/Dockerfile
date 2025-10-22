FROM python:3.12

RUN apt-get update

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /backend

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]
