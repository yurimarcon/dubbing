
## Como pegar videos no YouTube?

instalar o "yt-dlp" e rodar o comando:
```sh
yt-dlp <url do video do youtube>
```

o video pode não vir em form ato MP4, então usar o programa "ffmpeg" para converte-lo.

```sh
ffmpeg -i <video baixado do youtube> <nome do novo video colocando a extenção .mp4>
```

Rodar com python 3.11.0
Criar diretório result/ na raiz e temp/ dentro de result

### como rodar por linha de comando?

Basta ir para a raiz do projeto pelo terminal e rodar:

```sh
python main.py result/<nome do arquivo .mp4 que você quer traduzir.>
```

### Como rodar a API

Precerará ter o Redis instalado na maquina, ele serve para receber informações do gerenciamento de tarefas em background.
Após o redis estar rodando rode seguinte comando para iniciar o Celer que é o worker que gerencia o processamento em Background:

Rodar o Redis:

```sh
redis-server
````

Rodar o Celery:

```sh
celery -A app.celery worker --loglevel=info
```

Agora rode a API:

```sh
flask run
```

Caso queira acompanhar os processamentos por uma painel web, rode em outro terminal:
(Precisará ter o flower instalado)

```sh
celery -A app.celery flower
```

## Como enviar requisições via curl?

Você pode usar o seguinte comando:

```sh
curl -X POST -F "file=@/path/to/your/video.mp4" http://127.0.0.1:5000/upload
```
> mantenha o "@", somente após ele você informa o path do arquivo.

Você também pode enviar arquivos chamando a API de outra forma ou via Swagger pela URL:
__http://127.0.0.1:5000/apidocs/#/default__

## Você também pode rodar via docker:

Criar a imagem:

```sh
docker-compose build
```

Subir o container:

```sh
docker-compose up
````

## Possíveis erros:

### Porta em uso:

confira qual porta está em uso com o seguinte comando:

```sh
sudo lsof -i :6379  
````

Para desligar o serviço basta usar o seguinte comando:

```sh
sudo kill -9 <PID>
````

### Como acessar o container?

Para acessar o container você pode usar o seguinte comando:

```sh
docker exec -it dubbing-web-1 /bin/bash
```

## Como recriar containers?

Se precisar fazer alguma alteração, vai precisar deletar os containers e criar novamente:

```sh
docker-compose down
````

recriar:

```sh
docker-compose up --build
```