# Anotaciones Python

### Parte una cadena por los espacios
Se asignan dichos valores partidos a las variables correspondientes.
<pre>
valor = input().split(" ")
a, b, c = valor
</pre>

### Lista con numeros enteros directamente
Se asignan dichos valores partidos a una lista
<pre>
valores = [float(x) for x in input().split(" ")]
</pre>

### Potencia
<pre>
import math
math.pow(radius, 2)
</pre>

### Raiz cuadrada
<pre>
import math
math.sqrt(valor)
</pre>

### rango en if
Comparar un rango de dos valores
<pre>
if 0 <= valor <= 25
</pre>

### for con rango
Hacer un for x número de veces
<pre>
for x in range(6)
    valor = float(input())
</pre>

### imprimir valores que pueden ser decimales o no
<pre>
i = 1.0
print("I={:g}" .format(i))
</pre>

### ordenar listas
<pre>
lista = [5, 7, 3, 1]
lista.sort()
</pre>

### invertir listas
<pre>
lista = [5, 7, 3, 1]
lista.reverse()
</pre>
