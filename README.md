
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

### Como rodar por linha de comando?

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

Para fazer o upload do aquivo você pode usar o seguinte comando:

```sh
curl -X POST -F "file=@/path/to/your/video.mp4" http://127.0.0.1:5000/upload
```
> mantenha o "@", somente após ele você informa o path do arquivo.

Para fazer o download do arquivo:

```sh
curl -X GET "http://localhost:5000/download?file_path=path/para/seu/arquivo.txt" -O
```

## COmo enviar a requisição via fetch?

Faz o upload do arquivo:

```js
const uploadFile = async () => {
  // Seleciona o arquivo do input (suponha que tenha um input file no HTML)
  const fileInput = document.querySelector('input[type="file"]');
  const file = fileInput.files[0];

  // Dados do formulário que o endpoint requer
  const sourceLanguage = 'en'; // Exemplo de língua fonte
  const destLanguage = 'es';   // Exemplo de língua de destino
  const user = 'user123';      // Exemplo de nome de usuário

  // Cria um FormData para enviar o arquivo e os dados do formulário
  const formData = new FormData();
  formData.append('file', file);                // Adiciona o arquivo
  formData.append('source_language', sourceLanguage);
  formData.append('dest_language', destLanguage);
  formData.append('user', user);

  // Faz a requisição `POST` para o endpoint
  try {
    const response = await fetch('http://127.0.0.1:5000/upload', {
      method: 'POST',
      body: formData, // Envia o FormData com o arquivo e os dados do formulário
    });

    if (!response.ok) {
      throw new Error('Erro ao enviar o arquivo');
    }

    const result = await response.json(); // Obtem a resposta como JSON
    console.log('Sucesso:', result);      // Exibe a resposta da API
  } catch (error) {
    console.error('Erro:', error);        // Lida com erros
  }
};
```

Faz o download do arquivo

```js
fetch('http://127.0.0.1:5000/download?file_path=result/result.mp4')
  .then(response => {
    if (!response.ok) {
      throw new Error('Erro ao baixar o arquivo');
    }
    return response.blob(); // Obtém o arquivo como um blob
  })
  .then(blob => {
    // Cria um link temporário para download
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.style.display = 'none';
    a.href = url;
    a.download = 'result.mp4'; // Nome do arquivo baixado
    document.body.appendChild(a);
    a.click();
    window.URL.revokeObjectURL(url); // Libera o objeto URL
  })
  .catch(error => {
    console.error('Erro ao baixar o arquivo:', error);
  });
```

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
