# Especificación de la clase HistorialCalculos

Archivo donde va: clases/historial_calculos.py

## 1. Identificación de la clase

**Nombre:** HistorialCalculos

**Objetivo:** Guardar todos los cálculos que voy haciendo en la sesión para poder
consultarlos después

**Responsabilidad:** Esta clase solo guarda y entrega No calcula nada, no valida números y
no imprime Confía en que lo que le pasan ya viene bien calculado por IntegralDefinida

Es la clase más simple de las tres, y es la que cumple el requisito de usar una lista para
manejar varios registros

## 2. Atributos

- calculos -> list -> La lista donde se van guardando los cálculos, cada uno es un diccionario -> Empieza vacía, o sea []

**Por qué un diccionario y no una lista dentro de la lista:** porque cuando lo lea después
quiero escribir calculo["resultado"] y no calculo[5] Si uso posiciones, a la semana ya no me
acuerdo cuál era cuál

## 3. Constructor __init__

**Qué recibe:** solo self, no recibe nada más

**Qué hace:**

```
self.calculos = []
```

Nada más Arranca con la lista vacía porque al abrir el programa todavía no he calculado nada

## 4. Métodos

### agregar(self, texto_funcion, a, b, n, tipo, resultado)

**Objetivo:** Meter un cálculo nuevo al final de la lista

**Entradas:**

- texto_funcion -> str -> la función escrita, tipo f(x) = x + 3
- a -> float -> el límite inferior que usé
- b -> float -> el límite superior que usé
- n -> int -> cuántos rectángulos usé
- tipo -> str -> derecho, izquierdo o medio
- resultado -> float -> el área que salió

**Atributos que usa:** self.calculos

**Algoritmo:**

```
armar un diccionario con las llaves:
    "funcion", "a", "b", "n", "tipo", "resultado"
agregar ese diccionario al final de self.calculos con append
```

**Resultado:** no devuelve nada, solo modifica la lista

**Validaciones:** ninguna, a propósito Si validara aquí estaría repitiendo lo que ya hizo
IntegralDefinida

### listar(self)

**Objetivo:** Entregar todos los cálculos guardados

**Entradas:** ninguna

**Algoritmo:**

```
devolver self.calculos
```

**Resultado:** la lista completa de diccionarios

### contar(self)

**Objetivo:** Decir cuántos cálculos llevo

**Entradas:** ninguna

**Algoritmo:**

```
devolver len(self.calculos)
```

**Resultado:** un entero

### esta_vacio(self)

**Objetivo:** Saber si todavía no he calculado nada, para que el menú avise en vez de
mostrar una lista vacía

**Entradas:** ninguna

**Algoritmo:**

```
devolver len(self.calculos) == 0
```

**Resultado:** True o False

### obtener_ultimo(self)

**Objetivo:** Darme el último cálculo que hice

**Entradas:** ninguna

**Algoritmo:**

```
si la lista esta vacia:
    devolver None
devolver self.calculos[-1]
```

**Resultado:** el último diccionario, o None si no hay nada

## 5. Reglas que no se pueden cambiar

- **RH1** Los cálculos se guardan en el orden en que se hicieron, siempre con append al
  final Nada de ordenarlos por resultado ni por n
- **RH2** La lista no se borra sola nunca No se agrega ningún método de limpiar o vaciar
- **RH3** Las llaves del diccionario se llaman exactamente funcion, a, b, n, tipo y
  resultado Si se les cambia el nombre, main.py deja de encontrarlas
- **RH4** La clase nunca usa input ni print El que imprime el historial es main.py
- **RH5** No se guarda nada en archivo El historial vive solo mientras el programa está
  abierto, y eso está bien para lo que necesito
