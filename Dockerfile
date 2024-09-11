# Usar uma imagem base do Python
FROM python:3.11-slim

# Instalar dependências do sistema necessárias para construir pacotes
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    python3-dev \
    libffi-dev \
    libsndfile1 \
    libssl-dev \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Instalar o compilador Rust
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de dependências para o contêiner
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o contêiner
COPY . .

# Expôr as portas que serão usadas
EXPOSE 5000 6379 5555

# Comando padrão para o contêiner
CMD ["redis-server"]
