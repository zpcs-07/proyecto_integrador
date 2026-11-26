# Especificación de la clase IntegralDefinida

Archivo donde va: clases/integral_definida.py

## 1. Identificación de la clase

**Nombre:** IntegralDefinida

**Objetivo:** Calcular el área bajo la curva con sumas de Riemann, siguiendo los mismos 4
pasos de mi libreta

**Responsabilidad:** Esta clase sabe del intervalo y de cómo partirlo en rectángulos No sabe
evaluar la función Para eso le pide ayuda al objeto FuncionPolinomial que trae guardado
Tampoco habla con el usuario

Cada método sale directo de un paso:

- Paso 1, la amplitud -> calcular_amplitud()
- Paso 2, el tamaño de los subintervalos -> calcular_delta_x(n)
- Paso 3, la coordenada x_i -> calcular_coordenada(i, n, tipo)
- Paso 4, evaluar f en x_i -> se lo pido a self.funcion.evaluar(x)
- Armar la suma -> suma_riemann(n, tipo)

## 2. Atributos

- funcion -> FuncionPolinomial -> El objeto de la función que voy a integrar -> Llega por el constructor
- limite_inferior -> float -> El valor de a -> Llega por el constructor
- limite_superior -> float -> El valor de b -> Llega por el constructor

El atributo funcion no es un número ni un texto, es **otro objeto** Eso es lo que hace que
las dos clases colaboren

## 3. Constructor __init__

**Qué recibe:** self, funcion, limite_inferior y limite_superior

**Qué hace:**

1. Revisa que funcion sea un objeto FuncionPolinomial Si no, lanza TypeError
2. Revisa que los dos límites sean números Si no, lanza TypeError
3. Guarda los tres

**Qué no hace:** No revisa si a es mayor que b De eso se encarga es_intervalo_valido() Así,
si el intervalo está al revés el objeto se crea igual y nadie pierde lo que ya escribió

## 4. Métodos

### calcular_amplitud(self)

**Objetivo:** Sacar el ancho total del intervalo Es el paso 1

**Entradas:** ninguna

**Atributos que usa:** los dos límites

**Algoritmo:**

```
devolver self.limite_superior - self.limite_inferior
```

**Resultado:** un float con la amplitud A

**Comprobación:** con a = -2 y b = 3 debe dar 5, igual que en mi libreta

### calcular_delta_x(self, n)

**Objetivo:** Sacar el ancho de cada rectángulo Es el paso 2

**Entradas:** n, en cuántos pedazos parto

**Atributos que usa:** los dos límites, a través de calcular_amplitud()

**Algoritmo:**

```
si n no es entero o es menor que 1:
    lanzar ValueError
devolver self.calcular_amplitud() / n
```

**Resultado:** un float con el delta x

**Validaciones:** n entero y de 1 para arriba

**Comprobación:** con a = -2, b = 3 y n = 5 debe dar 1.0

### calcular_coordenada(self, i, n, tipo)

**Objetivo:** Dar la coordenada x del rectángulo número i Es el paso 3

**Entradas:**

- i -> int -> el número de rectángulo, de 1 a n
- n -> int -> cuántos rectángulos hay
- tipo -> str -> derecho, izquierdo o medio

**Atributos que usa:** self.limite_inferior

**Algoritmo:**

```
delta = self.calcular_delta_x(n)
si tipo es "derecho":
    devolver self.limite_inferior + i * delta
si tipo es "izquierdo":
    devolver self.limite_inferior + (i - 1) * delta
si tipo es "medio":
    devolver self.limite_inferior + (i - 0.5) * delta
si no:
    lanzar ValueError
```

**Resultado:** un float con la coordenada x_i

**Validaciones:** el tipo tiene que ser uno de los tres, y la i tiene que estar entre 1 y n

**Comprobación:** con a = -2, n = 5 y tipo derecho, para i = 1 debe dar -1 Es la fórmula
x_i = -2 + (5/n)i de mi libreta

### suma_riemann(self, n, tipo)

**Objetivo:** Calcular el área sumando todos los rectángulos

**Entradas:** n y tipo El tipo por defecto es derecho

**Atributos que usa:** self.funcion y los dos límites

**Algoritmo:**

```
si limite_inferior es igual a limite_superior:
    devolver 0
delta = self.calcular_delta_x(n)
suma = 0
repetir con i de 1 hasta n:
    x = self.calcular_coordenada(i, n, tipo)
    suma = suma + self.funcion.evaluar(x)
devolver suma * delta
```

**Resultado:** un float con el área aproximada

**Validaciones:** las que ya hacen calcular_delta_x y calcular_coordenada, no las repito

**Comprobación:** con f(x) = x + 3, a = -2, b = 3 y tipo derecho debe dar 20.0 con n = 5,
18.75 con n = 10 y 17.625 con n = 100, acercándose al 17.5 que saqué a mano

**Nota:** el delta se multiplica hasta el final y no dentro del ciclo, porque es la misma
operación repetida n veces Da igual el resultado pero son menos cuentas

### detalle_rectangulos(self, n, tipo, cuantos)

**Objetivo:** Darme los primeros rectángulos uno por uno, para comprobar a mano

**Entradas:** n, tipo, y cuantos rectángulos quiero ver, por defecto 5

**Atributos que usa:** self.funcion

**Algoritmo:**

```
detalle = lista vacia
limite = el menor entre cuantos y n
delta = self.calcular_delta_x(n)
repetir con i de 1 hasta limite:
    x = self.calcular_coordenada(i, n, tipo)
    altura = self.funcion.evaluar(x)
    area = altura * delta
    agregar a detalle la lista [i, x, altura, area]
devolver detalle
```

**Resultado:** una lista de listas Cada renglón trae el número de rectángulo, su x, su altura
y su área

**Validaciones:** cuantos tiene que ser entero y mayor que 0

### es_intervalo_valido(self)

**Objetivo:** Decir si se puede calcular con el intervalo que tengo guardado

**Entradas:** ninguna

**Algoritmo:**

```
devolver self.limite_inferior <= self.limite_superior
```

**Resultado:** True o False

## 5. Reglas que no se pueden cambiar

- **RI1** La i va de 1 a n, no de 0 a n-1 Así está en mi libreta, porque la fórmula
  x_i = x_0 + i·Δx depende de eso
- **RI2** El tipo por defecto es derecho, que es el que usé en el ejercicio original
- **RI3** suma_riemann no redondea El redondeo se hace al imprimir, en main.py
- **RI4** Esta clase no evalúa la función por su cuenta Siempre le pide el valor a
  self.funcion.evaluar() Si se copia la fórmula aquí adentro, las dos clases dejan de
  colaborar
- **RI5** La clase nunca usa input ni print
- **RI6** No se agrega ningún método de antiderivada ni de cálculo exacto Aquí se trabaja
  solo con la definición de suma de Riemann
- **RI7** Si a es igual a b el resultado es 0, sin entrar al ciclo
