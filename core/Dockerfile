FROM python:3.11
WORKDIR /core
RUN pip install poetry
COPY . .

RUN poetry install --no-root

EXPOSE 8001
ENTRYPOINT [ "poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001" ]
