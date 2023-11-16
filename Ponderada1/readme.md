# Implementação de SLAM

Essa atividade tem como objetivo implementar o mapeamento e a navegação de ambientes através do robô móvel Turtlebot3. Para isso, foi utilizado o simulador Gazebo e o ROS (Robot Operating System). A partir disso, foi possível criar pacotes ROS para a navegação e mapeamento do ambiente, além de criar um mapa do ambiente e realizar a navegação autônoma do robô.

## Setup do ambiente

Para a realização dessa atividade, foi utilizado um container Docker com o ROS e o Gazebo instalados, utilizando uma imagem do ROS Humble, disponibilizado no seguinte repositório: <https://github.com/Tiryoh/docker-ros2-desktop-vnc>.

A partir disso, foi necessário instalar o Turtlebot3 e o Nav2, cujas instalações foram realizadas no pr´oprio container.

## Como buildar o projeto

Para buildar o projeto, é necessário adentrar a pasta de workspace e executar o seguinte comando:

```bash
colcon build && source install/setup.bash
```

## Mapeamento

Para o mapeamento do ambiente, foi utilizado o `turtlebot3_cartographer`, que é um pacote ROS que permite a criação de mapas 2D do ambiente. A partir disso, foi necessário utilizar o pacote de teleoperação do Turtlebot3 para controlar o robô enquanto realiza o mapeamento do ambiente. Para integrar os pacotes, foi utilizado um launcher, que permite a execução de múltiplos pacotes ao mesmo tempo.

Para executar o mapeamento, é necessário executar o seguinte comando:

```bash
ros2 launch controller_package mapping_launch.py
```

A demonstração da execução do mapeamento está disponível no seguinte link: <https://youtu.be/hlZBTrVtTo8>

## Navegação

Para a navegação, é necessário utilizar o pacotes do ROS de navegação, o `nav2_bringup`. Após isso, também é necessário lançar o Rviz, que é uma ferramenta de visualização do ROS, que permite a visualização do mapa e da navegação do robô. Para o acionamento do robô, foi criado um pacote de controle, que permite a navegação do robô através de pontos de navegação em um script em python.

Para executar a navegação, é necessário executar o seguinte comando:

```bash
ros2 launch controller_package navigation_launch.py
```

A demonstração da execução da navegação está disponível no seguinte link: <https://youtu.be/63rhUyVb8ck>
