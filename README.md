# Área bajo la curva con sumas de Riemann

Aplicación de consola en Python que calcula el área bajo la curva de una función polinomial
usando la definición de integral definida, o sea el límite de una suma de Riemann

Proyecto Integrador de Programación II

## De dónde salió el problema

**Asignatura original:** Cálculo

Es un ejercicio que resolví en la libreta cuando vimos integrales definidas Lo que se pedía
era calcular la integral de -2 a 3 de (x + 3) dx, pero sin usar la antiderivada: había que
partir el intervalo en n rectángulos, sumarlos todos y tomar el límite cuando n tiende a
infinito El resultado que me dio fue 35/2, o sea 17.5 u²

La foto del ejercicio original está en
evidencias/problema_original/ejercicio_original_integral_definida.jpg

## Objetivo

Que el programa haga los mismos cuatro pasos que hice yo a mano, pero con cualquier
polinomio, cualquier intervalo y cualquier cantidad de rectángulos:

1. Definir la amplitud del intervalo, A = x_f - x_i
2. Escoger el tamaño de los subintervalos, Δx = A / n
3. Establecer la coordenada x del rectángulo i, x_i = x_0 + i·Δx
4. Expresar f(x) en términos de x_i y sumar

## Qué hace

- Pide una función polinomial de hasta grado 10 y el intervalo de integración
- Escribe la función de forma legible, por ejemplo f(x) = x + 3
- Calcula la amplitud y el Δx y los muestra nombrando el paso del que vienen
- Calcula la suma de Riemann con extremo derecho, extremo izquierdo o punto medio
- Muestra los primeros 5 rectángulos con su coordenada, su altura y su área, para poder
  comprobar el resultado a mano
- Valida todo lo que se escribe, así que no truena aunque le metas texto donde van números

Lo que no hace: funciones que no sean polinomios, integrales impropias ni gráficas El
cálculo exacto por antiderivada tampoco, porque el chiste es trabajar con la definición

## Las clases

### FuncionPolinomial

Vive en clases/funcion_polinomial.py

Representa la función y sabe evaluarse en un punto No sabe nada de integrales

- Atributos: coeficientes (una lista, de mayor a menor potencia) y grado
- Métodos: evaluar(x) y a_texto()

### IntegralDefinida

Vive en clases/integral_definida.py

Parte el intervalo en rectángulos y los suma Guarda adentro un objeto FuncionPolinomial, y
cuando necesita la altura de un rectángulo se la pide a él en vez de calcularla por su
cuenta

- Atributos: funcion, limite_inferior y limite_superior
- Métodos: calcular_amplitud(), calcular_delta_x(n), calcular_coordenada(i, n, tipo),
  suma_riemann(n, tipo), detalle_rectangulos(n, tipo, cuantos) y es_intervalo_valido()

Las especificaciones completas de las dos, con atributos, algoritmos y reglas, están en la
carpeta especificaciones/

## Requisitos

- Python 3.10 o más nuevo
- Nada más La aplicación usa solo la biblioteca estándar, por eso requirements.txt no lista
  ninguna dependencia

## Instalación

```
git clone https://github.com/zpcs-07/proyecto_integrador.git
cd proyecto_integrador
python -m venv .venv
```

Y para activar el entorno, en Windows:

```
.\.venv\Scripts\Activate.ps1
```

## Cómo se ejecuta

```
python main.py
```

Sale este menú:

```
  AREA BAJO LA CURVA - SUMAS DE RIEMANN
1. Definir la funcion y el intervalo
2. Calcular el area
3. Salir
```

## Ejemplo: el ejercicio original

Con la opción 1 se mete grado 1 y los coeficientes 1 y 3, que es f(x) = x + 3, y los límites
-2 y 3 Luego con la opción 2 se pide n = 5 y tipo derecho

```
f(x) = x + 3
Intervalo definido: -2.0 a 3.0
Paso 1 - Amplitud: 5.0
Paso 2 - Delta x: 1.0
Rectangulo 1 - x: -1.0 - altura: 2.0 - area: 2.0
Rectangulo 2 - x: 0.0 - altura: 3.0 - area: 3.0
Rectangulo 3 - x: 1.0 - altura: 4.0 - area: 4.0
Rectangulo 4 - x: 2.0 - altura: 5.0 - area: 5.0
Rectangulo 5 - x: 3.0 - altura: 6.0 - area: 6.0
Resultado: 20.0
```

Las alturas 2, 3, 4, 5 y 6 son exactamente f(x_i) = 1 + (5/n)i evaluada para i de 1 a 5, que
es lo que escribí en la libreta La suma 2+3+4+5+6 da 20

Si se sube la n, el resultado se va acercando al 17.5 del ejercicio original:

```
n = 10     ->  18.75
n = 100    ->  17.625
n = 1000   ->  17.5125
n = 10000  ->  17.50125
```

Nunca va a dar 17.5 clavado con el extremo derecho, porque el límite es cuando n tiende a
infinito Pero con el punto medio sí da exacto desde n = 5, porque la función es una recta

## Pruebas

Son 10 casos documentados en documentacion/02_pruebas.md, con sus entradas, lo que se
esperaba, lo que salió y las observaciones Incluyen el ejercicio original, otras funciones,
casos límite, entradas inválidas y una función que da resultado negativo

Las capturas de las ejecuciones están en evidencias/ejecuciones/

## Documentación

- documentacion/01_analisis_problema.md -> el análisis del problema, de dónde salió y qué tiene que hacer el programa
- documentacion/02_pruebas.md -> los 10 casos de prueba
- documentacion/03_uso_copilot.md -> cómo usé GitHub Copilot y qué le revisé
- especificaciones/ -> un archivo por clase más el del programa principal

## Estructura del repositorio

```
proyecto-integrador/
├── README.md
├── .gitignore
├── requirements.txt
├── main.py
├── clases/
│   ├── __init__.py
│   ├── funcion_polinomial.py
│   └── integral_definida.py
├── especificaciones/
│   ├── especificacion_funcion_polinomial.md
│   ├── especificacion_integral_definida.md
│   └── especificacion_main.md
├── documentacion/
│   ├── 01_analisis_problema.md
│   ├── 02_pruebas.md
│   └── 03_uso_copilot.md
└── evidencias/
    ├── problema_original/
    └── ejecuciones/
```
