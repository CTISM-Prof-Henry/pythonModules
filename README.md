# Módulos

Módulos (ou bibliotecas, ou pacotes - mais sobre essa nomenclatura em breve) são um recurso da linguagem Python para 
organizar código-fonte em unidades bem-organizadas e delimitadas.

Bibliotecas não são um recurso exclusivo da linguagem Python. Na linguagem C, por exemplo, a primeira biblioteca que 
aprendemos a usar é a `stdio.h` (**St**andard **I**n and **O**ut Library), que possui funções que, como o nome já diz, 
definem o fluxo de entrada e saída de dados de um programa.

## Sumário

* [Diferença entre bibliotecas, módulos e pacotes](#diferena-entre-bibliotecas-mdulos-e-pacotes)
* [Importando bibliotecas](capítulos/importando_bibliotecas.md)
* [Definindo módulos e pacotes](capítulos/definindo_módulos_e_pacotes.md)
* [Instalação](#instalação)
* [Exercícios](#exercícios)

## Diferença entre bibliotecas, módulos e pacotes

No contexto da linguagem Python, os seguintes termos são usados:

* **Módulo:** é um **arquivo Python** (ou seja, um arquivo que termina com .py) que possui diversas definições, seja de
  constantes, ou de funções.
  * O arquivo [songs.py](artistas/kanye/songs.py) é um exemplo de um módulo
* **Pacote:** é uma **pasta que contém diversos arquivos Python** (ou, em outras palavras, é uma coleção de módulos). 
  Para uma pasta ser considerada um pacote, ela deve conter um arquivo `__init__.py`
  * A pasta [kanye](artistas/kanye) é um exemplo de um pacote
* **Biblioteca:** geralmente usamos esse termo para nos referirmos ora à módulos, ora à pacotes. Não existe uma 
  definição formal e rígida para o termo biblioteca, podendo significar qualquer coisa que **importamos** para realizar 
  um trabalho.
  * Na seção [Importando bibliotecas](#importando-bibliotecas), nos referimos à `math` como uma biblioteca, mas ela pode 
    ser tanto um módulo quanto um pacote
  
## Instalação 

Você precisará seguir esse passo-a-passo para fazer o tutorial da seção 
[Definindo módulos e pacotes](capítulos/definindo_módulos_e_pacotes.md), bem como os [Exercícios](#exercícios). 

1. Clone este repositório na sua máquina
2. [Crie um ambiente virtual do anaconda para trabalhar](
   https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/venvs.md#criando-pela-linha-de-comando)
3. Após ter criado o ambiente virtual e ativado-o, instale
   a biblioteca _lyricsgenius_: `pip install lyricsgenius`
4. Para executar os códigos-fontes, [abra a pasta deste repositório no Pycharm.](
   https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/venvs.md#usando-pelo-pycharm)

## Exercícios

1. Execute o arquivo [artistas/main.py](artistas/main.py). Identifique de qual arquivo cada um dos prints saiu. Por que eles são
   impressos nesta ordem?
2. Execute o arquivo [artistas/kanye/\_\_main\_\_.py](artistas/kanye/__main__.py). Por que os prints do arquivo 
   [artistas/kanye/\_\_init\_\_.py](artistas/kanye/__init__.py) não são impressos na tela?
3. Execute o arquivo [artistas/kanye/songs.py](artistas/kanye/songs.py). Por que os prints do arquivo 
   [artistas/kanye/\_\_init\_\_.py](artistas/kanye/__init__.py) não são impressos na tela?
4. Execute o arquivo [artistas/taylor/\_\_init\_\_.py](artistas/taylor/__init__.py). Por que nada acontece?
