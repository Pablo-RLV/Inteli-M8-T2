# Tradutor de áudio

## Descrição do Projeto

Essa atividade tem como objetivo implementar um tradutor de áudio, que recebe como entrada um arquivo de áudio em português, faz a transcrição desse áudio e sua posterior tradução, para de e retorna um arquivo de áudio em português. Para isso, foi utilizado a biblioteca whisper do OpenAI, que é uma API de conversão de texto para fala. Posteriormente, foi utilizado a biblioteca deep-translator, que é uma API de tradução de texto, utilizando o Google Translate. Finalmente, foi utilizado a API da openai para a transcrição do áudio traduzido.

O arquivo de áudio utilizado para a demonstração é um trecho da música "Como Tudo Deve Ser", da banda Charlie Brown Jr. O arquivo de áudio original é chamado de "audio.mp3", e o arquivo de áudio traduzido é chamado de "translated_audio.mp3".

Para que a solução tenha uma execução mais fácil, a aplicação foi containerizada utilizando o Docker.

## Como executar

Para executar a aplicação, primeiramente é preciso criar um arquivo `.env` na raiz do projeto, com as seguintes variáveis de ambiente:

```bash
OPENAI_API_KEY=<sua chave de API do OpenAI>
```

Posteriormente, tem se como requisito ter o Docker instalado na máquina. Então, basta adentrar a pasta do projeto e executar o comando:

```bash
docker build -t ponderada8 .
```

Após a criação da imagem, execute o comando:

```bash
docker run ponderada8
```

## Demonstração

Abaixo, segue uma demonstração da execução da aplicação:

<div style="position:relative;width:fit-content;height:fit-content;">
            <a style="position:absolute;top:20px;right:1rem;opacity:0.8;" href="https://clipchamp.com/watch/EauZHdME40n">
                <img loading="lazy" style="height:22px;" src="https://clipchamp.com/e.svg" alt="Made with Clipchamp" />
            </a>
</div>