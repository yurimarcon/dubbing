FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    python3-dev \
    libffi-dev \
    libsndfile1 \
    libssl-dev \
    curl \
    git \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/* && \
    curl https://sh.rustup.rs -sSf | sh -s -- -y

ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Modificações nos arquivos da Coqui TTS
RUN sed -i '311s/"""Ask the user to agree to the terms of service"""/return True/' /usr/local/lib/python3.11/site-packages/TTS/utils/manage.py
RUN sed -i '5s/speaker_file_path/speaker_file_path, weights_only=False/' /usr/local/lib/python3.11/site-packages/TTS/tts/layers/xtts/xtts_manager.py
RUN sed -i '51s/kwargs/kwargs, weights_only=False/' /usr/local/lib/python3.11/site-packages/TTS/utils/io.py
RUN sed -i '54s/kwargs/kwargs, weights_only=False/' /usr/local/lib/python3.11/site-packages/TTS/utils/io.py

COPY . .

EXPOSE 5000
