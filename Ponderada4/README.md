# Construção de um chatbot com LLM

## Descrição do projeto

Essa atividade tem como objetivo a construção de um chatbot utilizando o modelo de linguagem de linguagem de máquina (LLM). Para isso, foi utilizado a biblioteca OpenAI, que permite a utilização de modelos de LLM pré-treinados, além de permitir o treinamento de modelos próprios. A partir disso, foi possível criar um chatbot utilizando a linguagem Python, que responde a perguntas sobre a disciplina de Inteligência Artificial. Para a interação com o usuário, foi utilizado a biblioteca Gradio, que permite a criação de interfaces gráficas para a interação com o usuário. Com o intuito de universalizar a utilização da aplicação em diferentes plataformas, foi utilizado o Docker, que permite a criação de ambientes isolados para a execução de aplicações.

## Como utilizar o projeto

Para executar o projeto, primeiramente é preciso inserir a sua chave de acesso à API da OpenAI, que está dentro da variável openai.api_key, no script main.py.

Após isso, é necessário ter o Docker instalado na máquina. Para isso, basta seguir as instruções de instalação disponíveis no site oficial do Docker: https://docs.docker.com/get-docker/. Após a instalação, basta executar o comando abaixo para criar o ambiente de execução da aplicação:

```bash
docker build -t ponderada4 .
```

Após a criação do ambiente, basta executar o comando abaixo para iniciar a aplicação:

```bash
docker run ponderada4
```

A partir disso, a aplicação estará disponível no endereço http://localhost:7860/.

Adicionalmente, também foi inserido um link público para a aplicação, que pode será disponibilizado poucos segundos após a execução do comando acima. O link público tem valiadade de 72 horas.

## Demonstração

Abaixo, é possível visualizar um vídeo demonstrando a utilização da aplicação.

<div style="position:relative;width:fit-content;height:fit-content;">
            <a style="position:absolute;top:20px;right:1rem;opacity:0.8;" href="https://clipchamp.com/watch/kxk1McbQF7p?utm_source=embed&utm_medium=embed&utm_campaign=watch">
                <img loading="lazy" style="height:22px;" src="https://clipchamp.com/e.svg" alt="Made with Clipchamp" />
            </a>
            <iframe allow="autoplay;" allowfullscreen style="border:none" src="https://clipchamp.com/watch/kxk1McbQF7p/embed" width="640" height="360"></iframe>
</div>