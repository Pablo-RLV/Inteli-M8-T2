# Perceptron e portas lógicas

## Descrição do Projeto

Essa atividade tem como objetivo implementar um perceptron de portas lógicas AND, OR, NAND e XOR. Para que a solução tenha uma execução mais fácil, a aplicação foi containerizada utilizando o Docker.

## Como executar

Para executar a aplicação, é necessário ter o Docker instalado na máquina. Após isso, basta adentrar a pasta do projeto e executar o comando:

```bash
docker build -t ponderada6 .
```

Após a criação da imagem, basta executar o comando:

```bash
docker run ponderada6
```

## Resultados

Os resultados obtidos foram os seguintes:

    Testing AND gate:
    in (0, 0), out: 0
    in (0, 1), out: 0
    in (1, 0), out: 0
    in (1, 1), out: 1

    Testing OR gate:
    in (0, 0), out: 0
    in (0, 1), out: 1
    in (1, 0), out: 1
    in (1, 1), out: 1

    Testing NAND gate:
    in (0, 0), out: 1
    in (0, 1), out: 1
    in (1, 0), out: 1
    in (1, 1), out: 0

    Testing XOR gate:
    in (0, 0), out: 1
    in (0, 1), out: 0
    in (1, 0), out: 0
    in (1, 1), out: 0

## Observação

Para essa atividade, foi implementada também uma aplicação manual de perceptrons, que pode ser encontrada no diretório `alternative`, que faz uso da biblioteca numpy. Dessa forma, é possível perceber os parâmetros que são utilizados para a criação de um perceptron, para cada uma das portas lógicas.

## Demonstração

Abaixo, segue uma demonstração da execução da aplicação:

<div style="position:relative;width:fit-content;height:fit-content;">
            <a style="position:absolute;top:20px;right:1rem;opacity:0.8;" href="https://clipchamp.com/watch/kLC9GNVmxsp">
                <img loading="lazy" style="height:22px;" src="https://clipchamp.com/e.svg" alt="Made with Clipchamp" />
            </a>
</div>
