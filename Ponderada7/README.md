# Classificação MNIST

## Descrição do projeto

O projeto consiste em classificar imagens de dígitos manuscritos em 10 classes (0-9) utilizando uma rede neural convolucional. O dataset utilizado é o MNIST, que consiste em imagens de números manuscritos em escala de cinza com tamanho 28x28. A rede neural convolucional foi implementada na linguagem Python utilizando a biblioteca Keras, que por sua vez utiliza o TensorFlow como backend. O projeto foi desenvolvido utilizando o Google Colab, que é uma plataforma de desenvolvimento de projetos em Python que roda na nuvem. A solução pode ser acessada através do seguinte link: <https://colab.research.google.com/drive/1BDS6BnsHYUKx6u-9qhHb3ujZMy2U7UWN?usp=sharing>, ou através da visualização do arquivo `notebook.ipynb`, disponível no repositório desse projeto.

## Descrição da rede neural convolucional

A rede neural convolucional apresenta a seguinte arquitetura:

## Camada Flatten:
    Essa camada serve para transformar os dados de entrada em um formato unidimensional. Em redes neurais convolucionais (CNNs), a entrada geralmente é uma matriz multidimensional (como uma imagem). A camada Flatten converte essa matriz em um vetor unidimensional para ser processado pelas camadas subsequentes.

## Camadas Dense (Densamente Conectadas):
    Três camadas Dense seguidas são adicionadas após a camada Flatten. Cada camada Dense possui 128 neurônios (ou unidades) com função de ativação ReLU (Rectified Linear Unit). Isso significa que cada neurônio nessas camadas está conectado a todos os neurônios da camada anterior. A função de ativação ReLU (Rectified Linear Unit) introduz não linearidade na rede, ajudando-a a aprender relações mais complexas nos dados.

## Camada de Saída (Dense com ativação Softmax):
    A última camada Dense tem 10 neurônios, indicando que essa rede é utilizada para classificação em 10 classes diferentes (nesse caso, reconhecer os dígitos de 0 a 9). A função de ativação Softmax é usada na camada de saída para atribuir probabilidades às diferentes classes. Ela garante que a soma das saídas para todas as classes seja igual a 1, permitindo que a saída seja interpretada como probabilidades.

Essa arquitetura é uma rede neural básica com várias camadas densamente conectadas, usada principalmente para tarefas de classificação. Ela recebe dados unidimensionais após a camada Flatten, processa esses dados através de três camadas escondidas com ativação ReLU e gera probabilidades de pertencer a cada uma das 10 classes possíveis na camada de saída, usando a ativação Softmax.

## Treinamento da rede neural convolucional

A rede neural convolucional foi treinada por 3 épocas, utilizando o otimizador Adam e a função de perda Sparse Categorical Crossentropy. O otimizador Adam é um algoritmo de otimização estocástica que é baseado em estimações adaptativas de momentos de primeira e segunda ordem. A função de perda Sparse Categorical Crossentropy é utilizada para classificação multiclasse, e é definida como a média da perda de entropia cruzada categórica para cada classe.

## Resultados

A rede neural convolucional obteve uma acurácia de 97,45%, como solicitado para a elaboração do projeto.

A partir disso, é possível apontar que caso houvesse a utilização de mais épocas para o treinamento da rede neural convolucional, a acurácia poderia ser ainda maior.

## Demonstração 

Abaixo está a demonstração em vídeo do projeto:

<div style="position:relative;width:fit-content;height:fit-content;">
            <a style="position:absolute;top:20px;right:1rem;opacity:0.8;" href="https://clipchamp.com/watch/C8V0jCRckaH">
                <img loading="lazy" style="height:22px;" src="https://clipchamp.com/e.svg" alt="Made with Clipchamp" />
            </a>
</div>
