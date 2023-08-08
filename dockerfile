FROM python:3.8

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

# docker build -t myapp .
# docker run -p 8000:8000 myapp