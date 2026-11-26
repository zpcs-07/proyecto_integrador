# Especificación del programa principal (main.py)

## 1. Qué hace main.py

Es el único archivo que habla con el usuario Muestra el menú, pide los datos, crea los
objetos, les llama sus métodos e imprime lo que devuelven

Las clases no usan input ni print nunca Toda la conversación con la persona pasa por aquí

## 2. El menú

```
==========================================
  AREA BAJO LA CURVA - SUMAS DE RIEMANN
==========================================
1. Definir la funcion
2. Ver la funcion
3. Definir el intervalo
4. Ver la amplitud y el delta x
5. Calcular el area con suma de Riemann
6. Ver el detalle de los rectangulos
7. Ver el historial
8. Salir
==========================================
```

## 3. Objetos que se crean

- historial -> HistorialCalculos -> Se crea una sola vez, antes de entrar al ciclo del menú -> Vive toda la sesión
- funcion -> FuncionPolinomial -> Empieza valiendo None y se crea en la opción 1 -> Se reemplaza si el usuario vuelve a entrar a la opción 1
- integral -> IntegralDefinida -> Empieza valiendo None y se crea en la opción 3 -> Necesita que funcion ya exista

**Por qué funcion e integral empiezan en None:** porque al abrir el programa todavía no hay
nada definido Si el usuario se va directo a la opción 5, el programa tiene que avisarle en
vez de tronar

## 4. Funciones de apoyo (no son métodos, van sueltas en main.py)

### mostrar_menu()

Imprime el menú de arriba No devuelve nada

### pedir_entero(mensaje, minimo, maximo)

Pide un número entero y no suelta al usuario hasta que meta uno válido

```
repetir para siempre:
    texto = input(mensaje)
    intentar convertir texto a int
    si falla la conversion:
        imprimir "Eso no es un numero entero, intenta otra vez"
        seguir con la siguiente vuelta
    si el numero esta fuera del rango minimo-maximo:
        imprimir el rango permitido
        seguir con la siguiente vuelta
    devolver el numero
```

### pedir_decimal(mensaje)

Igual que la anterior pero con float y sin rango

```
repetir para siempre:
    texto = input(mensaje)
    intentar convertir texto a float
    si falla la conversion:
        imprimir "Eso no es un numero, intenta otra vez"
        seguir con la siguiente vuelta
    devolver el numero
```

### pedir_tipo()

Pide qué punto del rectángulo usar y devuelve derecho, izquierdo o medio

```
mostrar las tres opciones numeradas
opcion = pedir_entero("Elige: ", 1, 3)
si opcion es 1 devolver "derecho"
si opcion es 2 devolver "izquierdo"
si opcion es 3 devolver "medio"
```

El 1 es derecho porque es el que usé en el ejercicio original, así queda de primero

## 5. Qué hace cada opción

### Opción 1 - Definir la función

1. Pide el grado con pedir_entero("Grado del polinomio: ", 0, 10)
2. Arma una lista vacía de coeficientes
3. Repite grado + 1 veces, pidiendo con pedir_decimal el coeficiente de cada potencia,
   empezando por la más alta
4. Crea el objeto: funcion = FuncionPolinomial(coeficientes)
5. Si ya existía un objeto integral, lo vuelve a None, porque la función cambió y el
   intervalo viejo ya no corresponde a nada
6. Imprime la función con funcion.a_texto()

### Opción 2 - Ver la función

1. Si funcion es None, imprime "Primero define una funcion con la opcion 1" y regresa al menú
2. Si no, imprime funcion.a_texto() y el grado

### Opción 3 - Definir el intervalo

1. Si funcion es None, avisa y regresa al menú
2. Pide a con pedir_decimal("Limite inferior (a): ")
3. Pide b con pedir_decimal("Limite superior (b): ")
4. Crea el objeto: integral = IntegralDefinida(funcion, a, b)
5. Llama integral.es_intervalo_valido() Si devuelve False, avisa que a no puede ser mayor
   que b, deja integral en None y regresa al menú
6. Si está bien, confirma el intervalo

### Opción 4 - Ver la amplitud y el delta x

1. Si integral es None, avisa y regresa al menú
2. Pide n con pedir_entero("Numero de rectangulos (n): ", 1, 1000000)
3. Llama integral.calcular_amplitud() y lo imprime como paso 1
4. Llama integral.calcular_delta_x(n) y lo imprime como paso 2

Los imprimo nombrando el paso para que se vea que son los mismos pasos de la libreta

### Opción 5 - Calcular el área con suma de Riemann

1. Si integral es None, avisa y regresa al menú
2. Pide n con pedir_entero("Numero de rectangulos (n): ", 1, 1000000)
3. Pide el tipo con pedir_tipo()
4. Llama resultado = integral.suma_riemann(n, tipo)
5. Imprime el resultado redondeado a 6 decimales
6. Guarda el cálculo: historial.agregar(funcion.a_texto(), a, b, n, tipo, resultado)

El redondeo se hace aquí al imprimir, nunca dentro de la clase

### Opción 6 - Ver el detalle de los rectángulos

1. Si integral es None, avisa y regresa al menú
2. Pide n y el tipo igual que en la opción 5
3. Pide cuántos rectángulos quiere ver con pedir_entero("Cuantos quieres ver: ", 1, 20)
4. Llama detalle = integral.detalle_rectangulos(n, tipo, cuantos)
5. Recorre la lista con un ciclo e imprime cada renglón: el número de rectángulo, su x, su
   altura y su área

Esta opción es la que me deja comprobar el resultado a mano con la calculadora

### Opción 7 - Ver el historial

1. Si historial.esta_vacio() devuelve True, imprime "Todavia no has calculado nada" y regresa
2. Si no, recorre historial.listar() con un ciclo e imprime cada cálculo con su función, su
   intervalo, su n, su tipo y su resultado
3. Al final imprime cuántos van, usando historial.contar()

### Opción 8 - Salir

1. Imprime un mensaje de despedida
2. Corta el ciclo del menú

## 6. Secuencia general del programa

```
crear historial = HistorialCalculos()
funcion = None
integral = None

repetir mientras no se elija salir:
    mostrar_menu()
    opcion = pedir_entero("Elige una opcion: ", 1, 8)
    segun la opcion, hacer lo que dice la seccion 5
    si la opcion es 8, cortar el ciclo

imprimir despedida
```

## 7. Condiciones de salida

- El programa solo termina con la opción 8
- Ninguna otra opción corta el ciclo Si algo sale mal, se avisa y se regresa al menú
- El programa no debe terminar nunca por un error de Python Todas las entradas pasan por
  pedir_entero o pedir_decimal, que no dejan pasar texto que no sea número

## 8. Reglas que no se pueden cambiar

- **RM1** Las opciones del menú son 8 y están en ese orden No se agregan ni se quitan
- **RM2** Ninguna clase usa input ni print, solo main.py
- **RM3** El redondeo para imprimir es de 6 decimales, y solo al imprimir
- **RM4** Antes de usar funcion o integral siempre se revisa que no sean None
- **RM5** Todas las entradas de números pasan por pedir_entero o pedir_decimal, no se usa
  input directo para números
- **RM6** No se agrega ninguna opción de cálculo exacto por antiderivada El programa trabaja
  solo con sumas de Riemann

## 9. Cómo colaboran las tres clases

```
main.py
   |
   |-- crea --> FuncionPolinomial (guarda los coeficientes)
   |                    ^
   |                    | le pide evaluar(x)
   |-- crea --> IntegralDefinida (guarda la funcion y los limites)
   |
   |-- crea --> HistorialCalculos (guarda la lista de resultados)
```

El objeto integral trae adentro al objeto funcion Cuando integral necesita la altura de un
rectángulo no la calcula, se la pide a funcion Esa es la colaboración entre las dos clases y
es lo que tengo que poder explicar
