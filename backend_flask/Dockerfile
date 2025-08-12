FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE ${BACKEND_PORT}

CMD ["sh", "-c", "flask run --host=0.0.0.0 --port=${BACKEND_PORT}"]

