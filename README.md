# pythonModules

Módulos (ou bibliotecas, ou pacotes - mais sobre essa nomenclatura em breve) são um recurso da linguagem Python para 
organizar código-fonte em unidades bem-organizadas e delimitadas.

Bibliotecas não são um recurso exclusivo da linguagem Python. Na linguagem C, por exemplo, a primeira biblioteca que 
aprendemos a usar é a `stdio.h` (**St**andard **I**n and **O**ut Library), que possui funções que, como o nome já diz, 
definem o fluxo de entrada e saída de dados de um programa.

## Sumário

* [Diferença entre bibliotecas, módulos e pacotes](#diferena-entre-bibliotecas-mdulos-e-pacotes)
* [Importando bibliotecas](#importando-bibliotecas)
* [Definindo módulos e pacotes](#definindo-módulos-e-pacotes)
* [Instalação](#instalação)

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

## Importando bibliotecas

Vamos dar um exemplo de **importação** de bibliotecas: calculando o seno de um ângulo nas linguagens C e Python.

Para importar e usar a função `sin` (seno) da biblioteca `math.h` em C, escrevemos o seguinte código:

```C
#include <stdio.h>
#include <math.h>

int main() {
   float resposta = sin(60);
   printf("%f\n", resposta);
   
   return 0;
}
```

Repare que, uma vez importadas as bibliotecas (com a palavra reservada `include`), não precisamos prefixar o nome das 
funções (por exemplo, escrevemos `printf` e `sin`, mas não escrevemos `stdio.printf`, e nem `math.sin`).

Em Python, um código-fonte equivalente seria 

```python
import math

resposta = math.sin(60)
print(resposta)
```

Perceba que no caso de Python, a função está prefixada pela biblioteca de onde ela vem (sendo a função `print` nativa de 
Python, não necessitando de nenhuma importação).

Contudo, Python é uma linguagem de programação muito flexível, e podemos usar a palavra reservada `from` para remover o 
prefixo `math` de `sin`:

```python
from math import sin

resposta = sin(60)
print(resposta)
```

A flexibilidade de Python não para por aí: podemos inclusive renomear a função `sin` usando um alias (apelido, em 
inglês), usando a palavra reservada `as`:

```python
from math import sin as seno

resposta = seno(60)
print(resposta)
```

## Definindo módulos e pacotes

Em breve.

## Instalação 

1. Clone este repositório na sua máquina
2. [Crie um ambiente virtual do anaconda para trabalhar](
   https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/venvs.md#criando-pela-linha-de-comando)
3. Após ter criado o ambiente virtual e o ativado, instale
   a biblioteca _lyricsgenius_: `pip install lyricsgenius`
4. Para executar os códigos-fontes, [abra a pasta deste repositório no Pycharm.](
   https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/venvs.md#usando-pelo-pycharm)
