FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r backend/requirements.txt

EXPOSE 7860

ENV PORT=7860

CMD ["gunicorn", "-b", "0.0.0.0:7860", "wsgi:app"]