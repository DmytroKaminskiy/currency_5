FROM python:3.9

WORKDIR /code/build

COPY req.txt .

RUN pip install -r req.txt

COPY . .

CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=8081"]
