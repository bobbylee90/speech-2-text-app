FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-2025-06-30

WORKDIR /app

COPY applications/speech-2-text .

RUN apt-get update \
    && apt-get install -y ffmpeg \
    && pip install -r requirements.txt

# Pre-download the Whisper model
RUN python -c "import whisper; whisper.load_model('base.en')"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]