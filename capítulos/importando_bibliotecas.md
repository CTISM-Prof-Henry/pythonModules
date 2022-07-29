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
